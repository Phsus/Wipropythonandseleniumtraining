*** Settings ***
Documentation     Automation Exercise - Verify Test Cases Page
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Firefox
${URL}            https://automationexercise.com

*** Keywords ***
Click Element Bypassing Ads
    [Arguments]    ${locator}
    [Documentation]    Finds the element and clicks it using JS to bypass ad overlays.
    Wait Until Element Is Visible    ${locator}    timeout=10s
    ${element}=    Get WebElement    ${locator}
    Execute Javascript    arguments[0].scrollIntoView(true);    ARGUMENTS    ${element}
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${element}

*** Test Cases ***
Verify Test Cases Page
    [Documentation]    Test Case 7: Navigate to the Test Cases page and verify it loads successfully.

    # 1. Launch browser & 2. Navigate to url
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # 3. Verify that home page is visible successfully
    Wait Until Element Is Visible    xpath=//a[@href='/']    timeout=10s
    Element Should Be Visible        xpath=//a[@href='/']

    # 4. Click on 'Test Cases' button

    Click Element Bypassing Ads    xpath=//a[i[contains(@class, 'fa-list')]]

    # 5. Verify user is navigated to test cases page successfully

    Wait Until Element Is Visible    xpath=//b[text()='Test Cases']    timeout=10s
    Element Should Be Visible        xpath=//b[text()='Test Cases']


    Location Should Be               ${URL}/test_cases

    [Teardown]    Close Browser
