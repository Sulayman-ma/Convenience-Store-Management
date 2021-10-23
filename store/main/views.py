from flask import render_template, url_for, redirect, request, flash, current_app
from . import main
from .. import db
from .forms import CreateItem, RestockItems, ModifyItem
from ..models import Item, CartRow



@main.route('/favicon.ico')
def favicon():
    """Adding a favicon to the app. This method is stress. Flask should be ashamed."""
    return current_app.send_static_file('img/favicon.ico')


def filter_low_stock(items):
    return [item for item in items if item.low_stock]


@main.route('/', methods=['GET', 'POST'])
def index():
    items = Item.query.all()
    low_stock_items = filter_low_stock(items)

    if request.method == 'POST':
        # take the form's ID and quantity fields
        id = int(request.form.get('id'))
        quantity = int(request.form.get('quantity'))

        # prevent invalid entries
        if quantity <= 0:
            flash('⚠ Please enter a valid purchase quantity', 'misc')
            return redirect(url_for('.index'))

        # query id from both tables
        item = Item.query.get(id)
        cart_product = CartRow.query.get(id)
        
        # item exists in the cart
        if cart_product:
            if (quantity + cart_product.purchase_quantity) > item.stock:
                flash('⚠ Insufficient quantity in stock', 'misc')
                return redirect(url_for('.index'))
            cart_product.purchase_quantity += quantity
            cart_product.calculate_sub_total(item.price)
            db.session.add(cart_product)
            flash('ℹ {}\'s purchase quantity increased'.format(item.name), 'info')
        # item does not exist in the cart
        else:
            if quantity > item.stock:
                flash('⚠ Insufficient quantity in stock', 'misc')
                return redirect(url_for('.index'))
            # create cart item from above data and add to DB session and commit
            cart_row = CartRow(id = id,
                                name = item.name,
                                purchase_quantity = quantity,
                                sub_total = quantity * item.price)
            db.session.add(cart_row)
            flash('ℹ {} added to cart'.format(item.name), 'info')
        db.session.commit()
        return redirect(url_for('.index'))
    
    if low_stock_items:
        flash('⚠ Some items are low on stock. Please restock as soon as possible ⚠', 'warning')
    return render_template('main/home.html', items = items)


@main.route('/cart', methods=['GET', 'POST'])
def cart():
    cart_rows = CartRow.query.all()
    cart_total = sum([row.sub_total for row in cart_rows])

    if request.method == 'POST':
        row_ids = request.form.getlist('remove_item')

        # no items are selected for deletion
        if row_ids == []:
            # cart table contains items, proceed to checkout
            if cart_rows:
                """Confirm checkout logic. 
                
                Basically applies purchase quantities and updates item stock counts, then proceeds to empty cart table"""
                for row in cart_rows:
                    # query respective items
                    item = Item.query.get(row.id)
                    # apply purchase to stock
                    item.stock -= row.purchase_quantity
                    item.verify_stock_status()
                    # update item in DB
                    db.session.add(item)
                
                # empty cart table
                for row in cart_rows:
                    db.session.delete(row)

                # commit session and redirect
                db.session.commit()
                flash('Checkout Complete! Return to Store Front ✔🧾', 'success')
                return redirect(url_for('.cart'))
            else:
                flash('Cart is empty 🛒✖', 'error')
                return redirect(url_for('.cart'))
        else:
            """Delete items from cart"""
            # loop though list and delete each item from DB
            for row in row_ids:
                cart_row = CartRow.query.get(int(row))
                db.session.delete(cart_row)
            db.session.commit()
            return redirect(url_for('.cart'))

    return render_template('main/cart.html', cart_rows = cart_rows, cart_total = cart_total)


@main.route('/create', methods=['GET', 'POST'])
def create_item():
    items = Item.query.all()
    # most recent item ID
    if items == []:
        next_id = 1
    else:
        next_id = [x.id for x in items][-1] + 1

    create = CreateItem()
    if create.validate_on_submit():
        # ensure user enter valid stock amount
        if create.stock.data < 0 or create.price.data < 0:
            flash('Invalid stock or price amount', 'error')
            return redirect(url_for('.create_item'))
        item = Item(id = next_id, 
                    name = create.name.data,
                    price = create.price.data,
                    stock = create.stock.data,
                    post_restock = create.stock.data)
        item.verify_stock_status()
        db.session.add(item)
        db.session.commit()
        flash('Item successfully added ✔', 'success')
        return redirect(url_for('.create_item'))
    return render_template('main/create.html', create = create)


@main.route('/restock', methods=['GET', 'POST'])
def restock():
    items = Item.query.all()
    low_stock_items = filter_low_stock(items)
    item_names = [x.name for x in items]
    modded_item = None
    restock_form = RestockItems()

    if restock_form.validate_on_submit():
        name = request.form.get('item-name').strip()
        addition = restock_form.addition.data

        # ensure user does not restock a negative number
        if addition < 1 or name not in item_names:
            flash('Sorry, you have entered an invalid stock amount ❌', 'error')
            return redirect(url_for('.restock'))

        for item in items:
            if item.name == name:
                modded_item = item
                break

        modded_item.restock(addition)
        db.session.add(modded_item)
        db.session.commit()
        flash('ℹ {} {} added to stock'.format(addition, item.name), 'info')
        return redirect(url_for('.restock'))

    if low_stock_items:
        flash('⚠ Kindly restock the following items:', 'warning')
    return render_template('main/restock.html', items = items, restock_form = restock_form, low_stock_items = low_stock_items)


@main.route('/manage_items', methods=['GET', 'POST'])
def manage_items():
    items = Item.query.all()
    low_stock_items = filter_low_stock(items)
    modded_item = None

    if request.method == 'POST':
        # item(s) selected for deletion
        selected_ids = request.form.getlist('delete')
        if selected_ids != []:
            to_be_removed = [Item.query.get(id) for id in selected_ids]
            for item in to_be_removed:
                db.session.delete(item)
            db.session.commit()
            flash('Item(s) removed ✔', 'success')
            return redirect(url_for('.manage_items'))
        # if no items selected, check if a modification was made
        else:
            item_id = (request.form.get('item_id'))

            # either form has been submitted incorrectly
            if item_id is None:
                flash('No action was performed', 'misc')
                return redirect(url_for('.manage_items'))
            modded_stock = int(request.form.get('modded_stock'))
            modded_price = request.form.get('modded_price')

            # prevent invalid entiries
            try:
                modded_price = float(modded_price)
            except ValueError:
                flash('Invalid entry ❌', 'error')
                return redirect(url_for('.manage_items'))

            # query item
            item = Item.query.get(item_id)
            old_details = (item.price, item.stock)
            # check if no changes were made
            if item.price == modded_price and item.stock == modded_stock:
                flash('⚠ No changes were made', 'misc') 
                return redirect(url_for('.manage_items'))
            else:
                # make changes otherwise
                modded_item = item
                modded_item.price = modded_price
                modded_item.stock = modded_stock
                modded_item.post_restock = modded_stock
                modded_item.verify_stock_status()

                # add to DB and commit
                db.session.add(modded_item)
                db.session.commit()
                flash('ℹ Changes applied to {}:'.format(item.name), 'info')
                # if price was changed
                if old_details[0] != modded_price:
                    flash('\tPrice change [ NGN {:,} to NGN {:,} ]'.format(old_details[0], modded_price), 'info')
                # if stock was changed
                if old_details[1] != modded_stock:
                    flash('\tStock change [ {} to {} ]'.format(old_details[1], modded_stock), 'info')
                return redirect(url_for('.manage_items'))

    if low_stock_items:
        flash('⚠ Some items are low on stock. Please restock as soon as possible ⚠', 'warning')
    return render_template('main/manage.html', items = items)
