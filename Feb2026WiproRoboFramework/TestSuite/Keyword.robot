*** Settings ***
# setting we add the external library detail ,resources , set up and tear down commnds
Library  SeleniumLibrary

*** Test Cases ***
# name of the Testcase
Verify login with valid credentials
             Login

Verify Add to cart functionality
             Login
     Log   user selects the product
     Log   user adds the product to the cart
     Log   user verifies that the product with details is added to the cart

*** Keywords ***
Login
     Log   Enterusername
     Log   Enter password
     Log   click on login button
     Log   user is on the home page