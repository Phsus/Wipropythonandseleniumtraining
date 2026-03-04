*** Settings ***
Documentation     Automation Exercise - Search Product
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            https://automationexercise.com
${SEARCH_TERM}    Top

*** Keywords ***
Click Element Bypassing Ads
    [Arguments]    ${locator}
    [Documentation]    Finds the element, scrolls it into view, and clicks it using JS to bypass ad overlays.
    Wait Until Element Is Visible    ${locator}    timeout=10s
    ${element}=    Get WebElement    ${locator}
    Execute Javascript    arguments[0].scrollIntoView(true);    ARGUMENTS    ${element}
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${element}

*** Test Cases ***
Search Product
    [Documentation]    Test Case 9: Navigate to Products page, search for a product, and verify results.

    # 1. Launch browser & 2. Navigate to url
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # 3. Verify that home page is visible successfully
    Wait Until Element Is Visible    xpath=//a[@href='/']    timeout=10s
    Element Should Be Visible        xpath=//a[@href='/']

    # 4. Click on 'Products' button (
    Click Element Bypassing Ads    xpath=//a[@href='/products']

    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    Wait Until Element Is Visible    xpath=//h2[text()='All Products']    timeout=10s
    Element Should Be Visible        xpath=//h2[text()='All Products']

    # 6. Enter product name in search input and click search button
    Input Text                       id=search_product    ${SEARCH_TERM}
    Click Element Bypassing Ads      id=submit_search

    # 7. Verify 'SEARCHED PRODUCTS' is visible
    Wait Until Element Is Visible    xpath=//h2[text()='Searched Products']    timeout=10s
    Element Should Be Visible        xpath=//h2[text()='Searched Products']

    # 8. Verify all the products related to search are visible

    Wait Until Element Is Visible    css=.features_items    timeout=10s
    Wait Until Element Is Visible    css=.productinfo       timeout=10s
    Element Should Be Visible        css=.productinfo

    [Teardown]    Close Browser
