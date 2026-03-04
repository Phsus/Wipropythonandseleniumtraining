*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://www.saucedemo.com/
${BROWSER}     chrome
${USERNAME}    standard_user
${PASSWORD}    secret_sauce

*** Test Cases ***
Verify End-to-End Checkout Flow
    # 1. Launch and Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=user-name    timeout=10s

    Input Text        id=user-name    ${USERNAME}
    Input Password    id=password     ${PASSWORD}
    Click Element     id=login-button
    Log To Console    \nLogged in successfully.

    # 2. Add Item to Cart
    Wait Until Element Is Visible    id=add-to-cart-sauce-labs-backpack    timeout=10s
    Click Element     id=add-to-cart-sauce-labs-backpack
    Log To Console    Added backpack to cart.

    # 3. Navigate to Cart
    # Using the CSS selector for the class name you provided
    Click Element     css=.shopping_cart_link
    Log To Console    Navigated to shopping cart.

    # 4. Proceed to Checkout
    Wait Until Element Is Visible    id=checkout    timeout=10s
    Click Element     id=checkout
    Log To Console    Clicked Checkout.

    # 5. Fill Checkout Information
    Wait Until Element Is Visible    id=first-name    timeout=10s
    Input Text        id=first-name    John
    Input Text        id=last-name     Doe
    Input Text        id=postal-code   12345
    Click Element     id=continue
    Log To Console    Checkout information filled and submitted.

    # 6. Finish Order
    Wait Until Element Is Visible    id=finish    timeout=10s
    Click Element     id=finish
    Log To Console    Clicked Finish to complete the order.

    # 7. Final Validation
    # We use the class from the <h2> tag to verify the text matches exactly
    Wait Until Element Is Visible    css=.complete-header    timeout=10s
    Element Text Should Be           css=.complete-header    Thank you for your order!
    Log To Console    Order completion verified successfully!

    # 8. Teardown
    Sleep    2s
    Close Browser
