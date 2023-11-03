return to [README.md](README.md)
# Index - Table of Contents

- [Manual Testing](#manual-testing)
- [Validation Tests](#validation-tests)
- [Bugs](#bugs) 


# Manual Testing

These tests are based on User Stories, Links and Features testing.

### Purpose of The Website /Landing Page

### US.01:
- As a <strong>Site User</strong>, I understand the purpose of the website So that I can find what I am looking for and eventually make a purchase.

#### Acceptance Criteria

- The Website loads with all the css and the user is able to interact and read about the Business objective.

#### Steps taken to Test Manually

- Clicked on the link [Beauty Boutique](https://beauty-boutique-0f4969a43fa4.herokuapp.com/) and the wesite loads perfectly.
- Information about the Purpose of this Website can be read in the about us section.
- All the links/Buttons serve their puprose and the related pages load and get displayed without errors.

#### Result 
- Pass

<hr>

### Home Page 

### US.22:

- As a <strong>Site User</strong>, after signup or login I can see The Home Page so that I can explore the additional features which are allowed to a registered User.

#### Acceptance Criteria

- The user is able to signup/register.
- The user receives a confirmation E-mail after registration.
- The user is able to login after signup/register.
- The home page and all its features are available after login.

#### Steps taken to Test Manually

- Click signup under the user icon in the upper navbar to go to signup page.
- Signup by entering all the required data.
- Confirm the signup using the confirmation E-mail.
- Click Login under the user icon in the upper navbar.
- Login using your username and password.
- Verify that you are logged in and your username is displayed under the user icon.
- Verify that the favorites icon is displayed on the upper navbar.

#### Result:

# Pass


### Navigation

### US.02: 

- As a <strong>Site User</strong> I can easily navigate around the website so that I can explore it and can go on different pages where I want to go.

#### Acceptance Criteria

- The user is able to easily navigate through the site using the navigation bar.
- The links direct to and display the desired page and information.

#### Steps taken to Test Manually

- Click each and every link/option in the navigation bar and check that it is working as desired.
- Click back and forth to check that the navigation is working in every aspect.
- Make sure that there is no broken navigation link.

#### Result:

# Pass


### View Products 

### US.03: 

- As a <strong>Site User</strong> I can easily navigate to the products page so that I can choose from them and make a purchase.


#### Acceptance Criteria

- The user is able to navigate to the products to view all the available products in order to make a purchase.
- The user is able to view products using the Discover and New Arrivals links from the home page.
#### Steps taken to Test Manually

- Click the all products link and select by price to view the product list ordered by price
- Click the all products link and select by rating to view the product list ordered by rating
- Click the all products link and select by category to view the product list ordered by category
- Click the all products link and select all products to view the unordered products list.
- Click the Discover link on the homepage to view all the products.
- Click the New Arrivals link on the homepage to view the new arrivals.

#### Result:

# Pass

### View Products By Category

### US.04: 

- As a <strong>Site User</strong> I can view Products by selecting category so that I can view the products I am searching for without scrolling through all the products.

#### Acceptance Criteria

- The user is able to view different product categories.
- The user is able to view products based on the different categories.


#### Steps taken to Test Manually

- Click Care and select an option in order to view products related to this category.
- Click Makeup and select an option in order to view products related to this category.
- Click Perfume and select an option in order to view products related to this category.
- Click Special Offers and select an option in order to view the products related to this category

#### Result:

# Pass

### Search Products

### US.05: 

- As a <strong>Site User</strong> I can search for a particular product so that I can quickly find the desired product. <hr>


#### Acceptance Criteria

- The user is able to view a search bar in the top navigation bar.
- The user is able to search for a product and see the results.
- The user is notified in case the desried product is not found.

#### Steps taken to Test Manually
- Type skin repair in the search bar and click the search icon or press enter to see the desired product appear as the result.
- Type test in the search bar and click the search icon or press enter to see no results appear.



#### Result:

# Pass

### Product Sorting

### US.21:

- As a <strong>Site User</strong> I can sort Products by Price, Rating, Name or by Category so that I can Easily find what I am looking for.


#### Acceptance Criteria

- The user sees a drop down on the products page.
- The user is able to sort the products by selecting an option from the drop down.

#### Steps taken to Test Manually

- On the products page select price(low to high) to see that the products are sorted based on the selection.
- On the products page select price(high to low) to see that the products are sorted based on the selection.
- On the products page select rating(low to high) to see that the products are sorted based on the selection.
- On the products page select rating(hight to low) to see that the products are sorted based on the selection.
- On the products page select name(A-Z) to see that the products are sorted based on the selection.
- On the products page select name(Z-A) to see that the products are sorted based on the selection.
- On the products page select category(A-Z) to see that the products are sorted based on the selection.
- On the products page select category(Z-A) to see that the products are sorted based on the selection.


#### Result:

# Pass

### Product Detail

### US.23: 

- As a <strong>Site User</strong> I am able to go to a Product's detail page so that I can read about the description of the product, add it to favourites or basket by selecting the quantity of the product.

#### Acceptance Criteria

- The user is able to see the product details on the product detail page.
- The user is able to add the product to the basket from the page.
- The user is able to add the product to favorites from the page.
- The user is able to increase/decrease the quantity of the product from the page.

#### Steps taken to Test Manually

- Click on a product from the products list to go to the product details page.
- On the product details page, a picture and a detailed description about the product is available.
- Click the basket icon to add the product to the basket.
- Click the favourites icon to add the product to your favourites list.
- Click the favourites icon to remove it from your favourites list.
- Click the plus icon to increase the product quantity.
- Click the minus icon to decrease the product quantity.
- Click the quantity field and enter the number of your choice. 
- Hover over the quantity filed to see an upward and downward arrowhead.
- Increase the quantity by clicking the upward arrowhead.
- Dicrease the quantity by clicking the downward arrowhead.


#### Result:

# Pass

### Favourites

### US.06: 

- As a <strong>Site User</strong> I can add or remove items into the favourites so that I can buy them in the Future if they are on sale or simply remove them.

#### Acceptance Criteria
- The user is able to add all the desired products in the favourites list and access them later from the list.
- The user is able to add one or more products from the favourites to the basket.
- The user is able to remove products from the favourites list.
- 

#### Steps taken to Test Manually

- Click the favourites icon on a product details page and then go to the favourites page using the favourites icon on the top right to see the product listed on the page. Check that the favourites counter increases everytime a product is added to the favourites list.
- On the favourites page click the add to basket in order to add the product to the basket to make a purchase.
- On the favourites page click the remove button next to a product in order to remove the product from the favourites list. Check that the counter decreases once a product is removed from the favourites list.


#### Result:

# Pass

### Basket

### US.07: 

- As a <strong>Site User</strong> I am able to check the Basket so that I can find the products I added to it. 

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Quantity of Products

### US.15: 

- As a <strong>Customer</strong> I can increase or decrease the quantity of the products so that I can decide how many products I want to buy.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass


### Edit or Update Basket

### US.08: 

- As a <strong>Site User</strong> I can Edit or Update my basket so that I can adjust the Quantity of the products or simply remove them before purchasing.
#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass


### Checkout

### US.09: 

As a <strong>Site User</strong> I can checkout securely so that I can see the order summary and purchase the items I have added to the basket.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Payment

### US.10:

- As a <strong>Site User</strong> I can make payment so that I can finally buy the products.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Order Confirmation

### US.17: 

- As a <strong>Customer</strong> I can receive a confirmation message after placing an order so that I am satisfied that the order has been placed and can view my order in my order history. 

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass


### Register an Account

### US.11:

- As a <strong>New User</strong> I need to understand the purpose of registration so that I can decide whether I should register an account or not.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Verification

### US.12: 

- As a <strong>Site User</strong> I can receive an email so that I can verify that my account has been registered successfully.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Login/Logout

### US.13: 

- As a <strong>Registered User</strong> I can Login and Logout of my account so that I can add products to the Basket, purchase them, add my favourite items to my favourites, see the list of orders I have made or view my details and update them if I need to.
#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### View/ Update User Profile

### US.14: 

- As a <strong>Registered User</strong> I can access my Profile so that I can view my order history, favourites list and update my delivery details.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Subscribe to Newsletter

### US.16:

- As a <strong>Site User</strong> I can Subscribe for Newsletter so that I can get all the updates about new offers and upcoming events.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Error Page

### US.18: 

- As a <strong>Site User</strong>  I can understand when an error occurs so that I can be given clear feedback on what I should do.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Admin

### US.19: 

- As an <strong>Admin</strong>  I can login and access the admin page from the main website so that I can perform the actions required as an Admin.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

### Admin Objectives

### US.20: 

- As an <strong>Admin</strong> I can Add, Update or Delete products from the website so that I can keep the list of products Up to date and can track all the activity running on my website and can send Newsletters to the Subscribers.

#### Acceptance Criteria


#### Steps taken to Test Manually


#### Result:

# Pass

[Back to Top](#table-of-contents)



# Validation Test

#### HTML is checked through the W3C CSS Validator and shows no errors.

<img src="static/media/html-validation.jpg" width="80%" align = "center"> <br>

#### CSS is checked through the W3C CSS Validator and shows no errors.

<img src="static/media/css-validation.jpg" width="80%" align = "center"> <br>

#### JavaScript is checked through the JSHint and shows no errors.

<img src="static/media/js-validation.jpg" width="80%" align = "center"> <br>

#### Python code is validated using the command "python3 -m flake8" from the Gitpod terminal. Most of the errors are line too long or other Django errors. The code is free of any warnings. I tried to remove all the Errors but still there are some left.

<img src="static/media/python3-validation1.jpg" width="80%" align = "center"> <br>

<img src="static/media/python3-validation2.jpg" width="80%" align = "center"> <br>

<img src="static/media/python3-validation3.jpg" width="80%" align = "center"> <br>

# Bugs

There are no Bugs found.

[Back to Top](#table-of-contents)