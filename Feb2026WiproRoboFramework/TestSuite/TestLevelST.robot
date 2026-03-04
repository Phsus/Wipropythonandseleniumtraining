*** Settings ***
# Setting we add external library details, resources, set up and tear down commands
# Test Setup - These run before EACH test case.
# Test Teardown - These run after EACH test case.

Resource          ./../Resources/Resource.robot
Library           SeleniumLibrary

Test Setup        Launch Browser
Test Teardown     Close the Browser

*** Test Cases ***
# Name of the testcase
Verify login with valid credentials
    Login

Verify Add to cart functionality
    Login
    Log    User selects the product
    Log    User adds the product to the cart
    Log    User verifies that the product with details is added to the cart
