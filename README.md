## Django Dynamic Cart

#### About the project
This project is for a shopping cart page built with Python 3+, Django 3, HTML, CSS and Javascript. The following are attributes of the cart:
1. User can see and edit the inventory of products from the django admin.
2. On submission, Availability of each product is confirmed (comparing quantity in the inventory and quantity in the shopping cart). 
3. User finds a descriptive error (“Sorry but we are out of stock for potatoes”, “Sorry but we only have 1kg of potatoes left”, etc) or a confirmation of the order if everything is correct. 
4. User can modify the quantity of each product and update the line price and total price without refreshing the page (javascript). 
5. The shopping cart is responsive (CSS).


### How to Run this Project
  - Confirm python3 and Django installations on your local computer.
  - Clone the repository using the command `git clone https://github.com/Resa-Obamwonyi/djangoCart.git`
  - In your terminal, create a virtual environment. 
  - first run `pip3 install virtualenv` then cd into the root of your project and run `virtualenv venv` where "venv" is the name of your env folder.
  - Activate the virtual environment using **`source venv/bin/activate` FOR MAC**, and **`\path\to\env\Scripts\activate` FOR WINDOWS**, confirm that the virtual environment is running.
  - In your root folder, create a file called ".env" , in this file, paste the environment variables provided to you.
  - With venv still activated run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
  - Run migrations with `python manage.py makemigrations` and `python manage.py migrate`
  - To create a super user with  which to access the django admin, run the command `python manage.py createsuperuser`, and follow the prompt.
  - Run `python manage.py runserver` to start the project server
  - To access the admin portal, visit `http://127.0.0.1:8000/admin/`, login with the superuser credentials from before.
  - To view the shopping cart page, visit `http://127.0.0.1:8000/` 