# CONVENIENCE STORE MANAGEMENT

A typical convenience store, supermarket or minimart application, bundled with inventory tracking and management functionality.
The application is desktop focused and not intended for use on devices smaller than 970px

A core feature of the application, is it's ability to notify users when items are low on stocks. For every time an item is restocked, its post restock value is set and when the stock reaches 20% or less than the post restock value, the user is notified. This feature also lists the specific items that are low, on the restock page so as to enable easier tracking. 

## Store Front
The *Index page* (landing page) of the app is the *Store Front*. Here, the user can easily navigate through the list of items in the store's inventory with their names, prices and available stock. Whenever a customer wants to make a purchase, they locate the item they wish to buy, input the quantity purchased and click the `Add` button to add it to the checkout cart. Please note that only one item can be added to the cart at a time, and this is deliberate to reduce user input error.

### Checkout Cart
The checkout cart has two sub-menus: 
- Resume Checkout - This is the default menu of the Checkout Cart page. A list of all items in the purchase session are displayed with their names, purchase quantity and sub-total price. At the bottom of the page, the total amount for the purchase session is displayed.
- Modify Cart - The modify cart menu gives the user the freedom to remove items from the cart by multiple selection.

## Create New Item
This menu allows for addition of new items to the store inventory. The item name, price and available stock are entered and then the `Create` button is clicked.

## Restock Items
The restock menu performs the function of restocking inventory items. The item name is selected from a drop-down list, stock addition amount is inputed and the request is sent.

## Inventory Management
This is the store's inventory page displaying all items, their names, prices and available stock. The inventory page has two sub-menus:
- Modify Items(Default) - This menu allows for item modification, that is, changing an item's price and available stock amount. Name changes are prevented.
- Remove Items - This menu allows for removal of store items permanently by multiple selection. Any and all items removed *cannot be recovered*. 
