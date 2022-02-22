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
# Basic Requirements 
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

NOTE: The ".env" file must be ignored from version control, by using a corresponding entry in the ".gitignore" file.

```sh
# this is the ".gitignore" file...

# ignore environment variables in the ".env" file:
.env
```

```sh
# Google Sheet Bonus Assignment 
`GOOGLE_SHEET_ID` = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI"
`SHEET_NAME` = "Products-2021"
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

Navigate to https://sendgrid.com/dynamic_templates and press the "Create Template" button on the top right. Give it a name like "example-receipt", and click "Save". At this time, you should see your template's unique identifier (e.g. "d-b902ae61c68f40dbbd1103187a9736f0"). Copy this value and store it in an environment variable called SENDGRID_TEMPLATE_ID.





Follow this https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md link for further details.

# Google Sheet Bonus Assignment 

```sh
json
gspread oauth2client
```

## Usage 

Run the program: 

```sh
python shopping_cart.py 
```

