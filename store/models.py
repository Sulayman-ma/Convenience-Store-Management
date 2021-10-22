"""
Database models file
"""

from . import db



class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique = True, nullable = False)
    price = db.Column(db.Float, default = 0)
    stock = db.Column(db.Integer, default = 0)
    sold_out = db.Column(db.Boolean, default = False)
    # helps somewhere I don't know where yet
    post_restock = db.Column(db.Integer)
    low_stock = db.Column(db.Boolean, default = False)


    def __repr__(self):
        return '<Item #{} - {}>'.format(self.id, self.name)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.stock == 0:
            self.sold_out = True

    def verify_stock_status(self):
        if self.stock <= (0.2 * self.post_restock):
            self.low_stock = True
        if self.stock == 0:
            self.sold_out = True

    def restock(self, addition):
        self.stock += addition
        # set post restock to keep track of how low stock is
        self.post_restock = self.stock
        self.sold_out = False
        self.low_stock = False


class CartRow(db.Model):
    __tablename__ = 'cart'

    """The cart row model is a table with a few columns. Stores the ID and name of the product, the purchase quantity and the sub total price. These will then be used in the `Checkout` button to fetch the items and apply the changes in stock and whatever else."""
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    purchase_quantity = db.Column(db.Integer)
    sub_total = db.Column(db.Float)

    def __repr__(self):
        return '<{} - {}>'.format(self.purchase_quantity, self.name)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_sub_total(self, price):
        self.sub_total = price * self.purchase_quantity