*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://practice.automationtesting.in/

*** Test Cases ***
Verify End-To-End WooCommerce Checkout
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # 1. Add Item to Basket
    Wait Until Element Is Visible    xpath=//a[@data-product_id='160']
    Scroll Element Into View         xpath=//a[@data-product_id='160']
    Execute Javascript               window.scrollBy(0, -200)
    Sleep    1s
    Click Element                    xpath=//a[@data-product_id='160']
    Log To Console                   \nAdded product to basket.

    # 2. View Basket
    Wait Until Element Is Visible    xpath=//a[@title='View Basket']    timeout=10s
    ${basket_btn}=    Get WebElement    xpath=//a[@title='View Basket']
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${basket_btn}
    Log To Console                   Navigated to the Basket page.

    # 3. Proceed to Checkout
    Wait Until Element Is Visible    xpath=//a[contains(@class, 'checkout-button')]
    ${checkout_btn}=  Get WebElement    xpath=//a[contains(@class, 'checkout-button')]
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${checkout_btn}
    Log To Console                   Navigated to the Checkout page.

    # 4. Fill Standard Billing Information
    Wait Until Element Is Visible    id=billing_first_name
    Input Text    id=billing_first_name    Sushant
    Input Text    id=billing_last_name     choudhary
    Input Text    id=billing_email         sc@example.com
    Input Text    id=billing_phone         9876543210
    Input Text    id=billing_address_1     123 streets
    Input Text    id=billing_city          New Delhi
    Input Text    id=billing_postcode      110001


    Scroll Element Into View    id=s2id_billing_country
    Execute Javascript          window.scrollBy(0, -200)
    Sleep    1s
    Click Element               id=s2id_billing_country

    Wait Until Element Is Visible    xpath=//div[@id='select2-drop']//*[text()='India']    timeout=5s
    Click Element                    xpath=//div[@id='select2-drop']//*[text()='India']


    Sleep    3s


    Scroll Element Into View    id=select2-chosen-2
    Execute Javascript          window.scrollBy(0, -200)
    Sleep    1s
    Click Element               id=select2-chosen-2

    Wait Until Element Is Visible    xpath=//div[@id='select2-drop']//*[text()='Delhi']    timeout=5s
    Click Element                    xpath=//div[@id='select2-drop']//*[text()='Delhi']

    Log To Console    Billing information and dropdowns selected successfully.


    Sleep    3s
    Wait Until Element Is Visible    id=place_order    timeout=10s
    ${place_order_btn}=    Get WebElement    id=place_order
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${place_order_btn}
    Log To Console                   Clicked Place Order!


    Sleep    5s
    Close Browser