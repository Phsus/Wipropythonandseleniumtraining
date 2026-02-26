*** Settings ***
Documentation     Automation Exercise - Verify All Products and Product Detail Page
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Firefox
${URL}            https://automationexercise.com

*** Keywords ***
Click Element Bypassing Ads
    [Arguments]    ${locator}
    [Documentation]    Finds the element, scrolls it into view, and clicks it using JS to bypass ad overlays.
    Wait Until Element Is Visible    ${locator}    timeout=10s
    ${element}=    Get WebElement    ${locator}
    Execute Javascript    arguments[0].scrollIntoView(true);    ARGUMENTS    ${element}
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${element}

*** Test Cases ***
Verify All Products And Product Detail Page
    [Documentation]    Test Case 8: Navigate to Products page, view a product, and verify details.

    # 1. Launch browser & 2. Navigate to url
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # 3. Verify that home page is visible successfully
    Wait Until Element Is Visible    xpath=//a[@href='/']    timeout=10s
    Element Should Be Visible        xpath=//a[@href='/']

    # 4. Click on 'Products' button
    Click Element Bypassing Ads    xpath=//a[@href='/products']

    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    Wait Until Element Is Visible    xpath=//h2[text()='All Products']    timeout=10s
    Element Should Be Visible        xpath=//h2[text()='All Products']

    # 6. The products list is visible

    Wait Until Element Is Visible    css=.features_items    timeout=10s
    Element Should Be Visible        css=.features_items

    # 7. Click on 'View Product' of first product
    Click Element Bypassing Ads    xpath=//a[@href='/product_details/1']

    # 8. User is landed to product detail page
    Wait Until Element Is Visible    css=.product-information    timeout=10s
    Location Should Contain          /product_details/1

    # 9. Verify that product details are visible: name, category, price, availability, condition, brand
    # Product Name
    Element Should Be Visible        xpath=//div[@class='product-information']/h2[text()='Blue Top']
    # Category
    Element Should Be Visible        xpath=//div[@class='product-information']/p[contains(text(), 'Category')]
    # Price
    Element Should Be Visible        xpath=//div[@class='product-information']//span[text()='Rs. 500']
    # Availability
    Element Should Be Visible        xpath=//div[@class='product-information']/p[b[text()='Availability:']]
    # Condition
    Element Should Be Visible        xpath=//div[@class='product-information']/p[b[text()='Condition:']]
    # Brand
    Element Should Be Visible        xpath=//div[@class='product-information']/p[b[text()='Brand:']]

    [Teardown]    Close Browser
