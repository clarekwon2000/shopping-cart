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

Install the requirements: 

```sh
pip install -r requirements.txt
```

# Environmental Variables 

You must set up a local file named ".env" outside the root directory of the project. You will be able to store the necessary environment variables in this file. The 

```sh
# this is the .env file 

You can configure your own tax rate via an environment variable called TAX_RATE.
# Tax Rate 
TAX_RATE = 0.0875

# Sendgrid Email Bonus Assignment 

SENDGRID_API_KEY = "SENDGRID_API_KEY"
SENDER_ADDRESS = "SENDER_EMAIL_ADDRESS" 
SENDGRID_TEMPLATE_ID = d-4c7766bc749f40bbbeb2a80a25e6f980

# Google Sheet Bonus Assignment 
GOOGLE_SHEET_ID = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI"
SHEET_NAME = "Products-2021"
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

