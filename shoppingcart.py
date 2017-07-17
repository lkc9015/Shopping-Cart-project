import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]

product_ids = []

## check point 1
while True:
    product_id = input("Please input a valid product identifier, or 'DONE' if there are no more items:") # withouth if statement, infinite loop
    if product_id == "DONE":
        break # break out of the loop
    elif int(product_id) >= 21:
        print ("Hey, are you sure that product identifier is correct? Please try again!")
    else:
        product_ids.append(int(product_id))

## The beginning of the receipt
print ("-" * 30)
print ("Lee's mart")
print ("-" * 30)
print ("Web: www.leemart.com")
print ("Phone: 1-917-498-1036")
now = datetime.datetime.now()
checkout_time = now.strftime("%Y-%m-%d %H:%M:%S")
print ("Checkout Time:" + " " + checkout_time)
print ("-" * 30)

## Printing items
print ("Shopping Cart Items:")

def lookup_product_by_id(product_id):
     matching_products = [product for product in products if product["id"] == product_id]
     return matching_products[0]

subtotal = 0

for product_id in product_ids:
    product = lookup_product_by_id(product_id)
    subtotal += product["price"]
    price_usd = ' (${0:.2f})'.format(product["price"])
    print(" + " + product["name"] + price_usd)

## The end of the receipt
print ("-" * 30)
print ("Subtotal: " + '${0:.2f}'.format(subtotal))

sales_tax = 0.08875 * subtotal
print ("Plus NYC Sales Tax (8.875%): " + '${0:.2f}'.format(sales_tax))

total_price = subtotal + sales_tax
print("Total: " + '{0:.2f}'.format(total_price))

print ("-" * 30)
print ("Thank you for your business! Please come again.")
