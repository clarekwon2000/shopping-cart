import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

# PRODUCT DATA FROM GOOGLE SHEETS 

DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
SHEET_NAME = os.getenv("SHEET_NAME", default="Products-2021")
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google-credentials.json")
AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
client = gspread.authorize(credentials)

# READ SHEET VALUES

# access the document:
doc = client.open_by_key(DOCUMENT_ID)

# access a sheet within the document:
sheet = doc.worksheet(SHEET_NAME)

# fetch all data from that sheet:
rows = sheet.get_all_records()

products = rows = sheet.get_all_records()

from ast import If
import datetime
from itertools import product
from pickle import TRUE
from time import strftime

# products = [
#     {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#     {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#     {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#     {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#     {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#     {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#     {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#     {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#     {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#     {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#     {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#     {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#     {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#     {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#     {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#     {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#     {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#     {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#     {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#     {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
   Converts a numeric value to usd-formatted string, for printing and display purposes.

   Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

   Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

subtotal_price = 0
product_ids = []
tday = datetime.datetime.now()
tday2 = tday.replace(microsecond = 0)

product_id = ""

while True: 
    # ASK FOR USER INPUT 
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if product_id == "DONE" or product_id == "done":
        break
    elif int(product_id) > len(products) or int(product_id) <=0 :
       print ("INVAlID ID : PLEASE TRY AGAIN")
    else:
        product_ids.append(product_id)


# INFO DISPLAY / OUTPUT 

print("--------------")

# A grocery store name of your choice
print("GEORGETOWN GREENS GROCERY")
# A grocery store phone number and/or website URL and/or address of choice
print("Call us at (202)-123-4567 / www.georgetown-greens-grocery.com")

print("--------------")

# The date and time of the beginning of the checkout process, formatted in a human-friendly way
print("CHECKOUT AT:", tday2)

print("--------------")

# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
print("SELECTED PRODUCTS:") 

matching_products = []
for product_id in product_ids:
    matching_product = [x for x in products if str(x["id"]) == str(product_id)]
    matching_product = matching_product[0]
    matching_products.append(matching_product)
    subtotal_price = subtotal_price + matching_product["price"]
    print("...", matching_product["name"], "(" + str(to_usd(matching_product["price"]))+ ")")

# subtotal, tax, total 

import os
from dotenv import load_dotenv

load_dotenv()

tax_rate = os.getenv("TAX RATE", default = 0.0875)
tax = subtotal_price * float(tax_rate)
total_price = subtotal_price + tax

# END OF RECEIPT 
print("--------------")
print("SUBTOTAL: " + str(to_usd(subtotal_price)))
print("TAX: " + (str(to_usd(tax))))
print ("TOTAL:", to_usd(total_price))
print("--------------")

########

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#### EMAIL 

while TRUE:
    user_receipt = input("Would you like to receive your receipt by email? [y/n]?")
    if user_receipt == "n" or product_id == "no" or product_id == "NO":
        # A friendly message thanking the customer and/or encouraging the customer to shop again
        print("--------------")
        print("THANKS, SEE YOU AGAIN SOON!")
        print("--------------")
        break
    elif user_receipt == "y" or product_id == "yes" or product_id == "YES":
        load_dotenv()

        SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
        SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
        SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

        # this must match the test data structure

        print(tday2.strftime("%Y-%m-%d %H:%M:%S"))
        
        print(matching_products)
        template_data = {
            "subtotal_price":str(to_usd(subtotal_price)),
            "tax":(str(to_usd(tax))),
            "total_price": to_usd(total_price),
            "tday2": tday2.strftime("%Y-%m-%d %H:%M:%S"), 
            "matching_products":
                [{'name':matching_product['name'], 'price': to_usd(matching_product['price'])} for matching_product in matching_products]
       }

        client = SendGridAPIClient(SENDGRID_API_KEY)
        print("CLIENT:", type(client))

        message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
        message.template_id = SENDGRID_TEMPLATE_ID
        message.dynamic_template_data = template_data
        print("MESSAGE:", type(message))

        try:
            response = client.send(message)
            print("RESPONSE:", type(response))
            print(response.status_code)
            print(response.body)
            print(response.headers)

        except Exception as err:
            print(type(err))
            print(err)
        break
    else:
        print ("INVAlID ID : PLEASE TRY AGAIN")

        