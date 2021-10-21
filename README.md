# Store

A typical convenience store application, bundled with inventory management and tracking functionality.
The application is desktop focused and not intended for use on devices with screens smaller than a computer's.

## Store Front
The main user of the application will be the store attendant. The *Index page* (landing page) of the app is the *Store Front*. Here, the attendant can easily navigate through the list of items in the store's inventory with their names, prices and available stock. When a customer wants to make a purchase, they locate the item they wish to buy, input the quantity purchased and click the `Add` button to add to the checkout cart. Please note that only one item can be added to the cart at a time, this is deliberate to reduce user input errors.

### Checkout Cart
The checkout cart has two submenus: 
- Resume Checkout - This is the default menu of the Checkout Cart page. A list of all items in the purchase session are displayed with their names, purchase quantity and subtotal price. Then at the bottom, the total amount for the purchase session is displayed.
- Modify Cart - The modify cart menu gives the attendant the freedom to remove items from the cart by multiple selection.

## Create New Item
This menu allows for addition of new items to the store inventory. The item name, price and available stock are entered and the create request is sent.

## Restock Items
The restock menu performs the function of restocking inventory items. The item name is selected from a drop-down list, stock addition amount is inputed and the request is sent.

## Inventory Management
This is the store's inventory page displaying all items, their names, prices and available stock. The inventory page has two sub-menus:
- Default - The default menu allows for removal of store items permanently. Any and all items removed cannot be recovered. 
- Modify Items - This menu allows for item modification, that is changing an item's name, price and available stock amount.
