# Shopping Cart Project 

## Setup 

### Repo Setup 

Use the GitHub online interface to create a new remote project repository called "shopping-cart". Add a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. 

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer.

After cloning the repo, navigate there from the command-line:

```sh
cd shopping-cart 
```

# Environment Setup 

You will need to activate a new Anaconda virtual environment.

```sh
conda create -n shopping-env python=3.8 
conda activate shopping-env
```

Use a "requirements.txt" file approach to install your packages. 
You will need to write the following packages: 

```sh
# This is the 'requirements.txt' file
python-dotenv
```

Install the requirements: 
```sh
pip install -r requirements.txt
```

# Environmental Variables 

You must set up a local file named ".env" outside the root directory of the project. You will be able to store the necessary environment variables in this file. The 

```sh
# this is the .env file 

You can configure your own tax rate via an environment variable called `TAX_RATE`.
# Tax Rate 
TAX_RATE = 0.0875
```

For Access to Google Sheets: 
```sh
# this is the .env file 
`GOOGLE_SHEET_ID` = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI"
`SHEET_NAME` = "Products-2021"
```

NOTE: The ".env" file must be ignored from version control, by using a corresponding entry in the ".gitignore" file.

```sh
# this is the ".gitignore" file...

# ignore environment variables in the ".env" file:
.env
```

# Sending Receipts via Email 

From within an active virtual environment, install the 'sendgrid' package:

```sh
pip install sendgrid

# optionally install a specific version:
#pip install sendgrid==6.6.0
```

First, sign up for a [SendGrid account](https://signup.sendgrid.com/), then follow the instructions to complete your "Single Sender Verification", clicking the link in a confirmation email to verify your account. 


Then [create a SendGrid API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions. We'll want to store the API Key value in an environment variable called `SENDGRID_API_KEY`.
Also set an environment variable called `SENDER_ADDRESS` to be the same email address as the single sender address you just associated with your SendGrid account.

Use a ".env" file approach to manage these environment variables.

```sh
# this is the .env file 

`SENDGRID_API_KEY` = "SENDGRID_API_KEY"
`SENDER_ADDRESS` = "SENDER_EMAIL_ADDRESS" 
`SENDGRID_TEMPLATE_ID` = d-4c7766bc749f40bbbeb2a80a25e6f980
```

## Email Templates

Navigate to https://sendgrid.com/dynamic_templates and press the "Create Template" button on the top right. Give it a name like "example-receipt", and click "Save". At this time, you should see your template's unique identifier (e.g. "d-b902ae61c68f40dbbd1103187a9736f0"). Copy this value and store it in an environment variable called `SENDGRID_TEMPLATE_ID`.

Back in the SendGrid platform, click "Add Version" to create a new version of a "Blank Template" and select the "Code Editor" as your desired editing mechanism.

At this point you should be able to paste the following HTML into the "Code" tab, and the corresponding example data in the "Test Data" tab, and save each after you're done editing them.


Example "Code" template which will specify the structure of all emails:
```sh
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello. This is your receipt from Georgetown Green Grocery!</h3>
<p>Date: {{tday2}}</p>

<ul>
{{#each matching_products}}
    <li>You ordered: {{name}} ({{price}}) </li>
{{/each}}

</ul>

<p>Sub-Total: {{subtotal_price}}</p>
<p>Tax: {{tax}}</p>
<p>Total: {{total_price}}</p>
```

Example "Test Data" which will populate the template:

```sh
{
    "subtotal_price":"$14.95",
    "tax":"$14.95",
    "total_price": "$14.95",
    "tday2": "2022-02-21 18:38:35",
    "matching_products":[
        {"name": "Product 1", "price": "$14.95"},
        {"name": "Product 2", "price": "$14.95"},
        {"name": "Product 3", "price": "$14.95"}
    ]
}
```

Finally, configure the template's subject by clicking on "Settings" in the left sidebar. Choose an email subject like "Your Receipt from the Green Grocery Store". Then click "Save Template".

After configuring and saving the email template, we should be able to use it to send an email:

```sh
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

# this must match the test data structure

template_data = {
  "subtotal_price":str(to_usd(subtotal_price)),
  "tax":(str(to_usd(tax))),
  "total_price": to_usd(total_price),
  "tday2": tday2.strftime("%Y-%m-%d %H:%M:%S"), 
  "matching_products":
      [{'name':matching_product['name'], 'price': to_usd(matching_product['price'])} for matching_product in matching_products]
  } # or construct this dictionary dynamically based on the results of some other process :-D

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
```

Follow this [Sendgrid Package](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) for better details.

# Integrating with Google Sheets Database 

First install the package (and a dependent auth-related package) using Pip, if necessary:

```sh
pip install gspread oauth2client
```

NOTE: you'll need to download a google credentials JSON file into your repo, but this file must ABSOLUTELY be ignored from version control. HINT: you can use an entry like the following in your ".gitignore" file:

```sh
# this is the .gitignore file

# ignore environment variables:
.env

# ignore google credentials:
# if you want to name your credentials "google-credentials.json":
google-credentials.json 
# otherwise use this catch-all to ignore all JSON files:
*.json 
```

## Usage 

Run the program: 

```sh
python shopping_cart.py 
```

Received Help from https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be
& the TA Sessions 

