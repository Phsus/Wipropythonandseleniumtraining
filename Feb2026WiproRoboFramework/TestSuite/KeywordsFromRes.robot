*** Settings ***

Resource  ./../Resources/Resource.robot
Library  SeleniumLibrary

*** Test Cases ***
Verify login with valid credentials
             Login

Verify Add to cart functionality
             Login
     Log   user selects the product
     Log   user adds the product to the cart
     Log   user verifies that the product with details is added to the cart
Launch Browser
             Login

Close the browser
             Login
