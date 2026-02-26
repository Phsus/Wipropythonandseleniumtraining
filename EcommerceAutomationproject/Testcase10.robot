*** Settings ***
Documentation     Automation Exercise - Verify Subscription in home page
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            https://automationexercise.com
${EMAIL}          sushant_test_sub@gmail.com

*** Test Cases ***
Verify Subscription In Home Page
    [Documentation]    Test Case 10: Scroll to footer, subscribe using email, and verify success message.

    # 1. Launch browser & 2. Navigate to url
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # 3. Verify that home page is visible successfully
    Wait Until Element Is Visible    xpath=//a[@href='/']    timeout=10s
    Element Should Be Visible        xpath=//a[@href='/']

    # 4. Scroll down to footer

    Execute Javascript               window.scrollTo(0, document.body.scrollHeight)

    # 5. Verify text 'SUBSCRIPTION'

    Wait Until Element Is Visible    xpath=//h2[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='subscription']    timeout=10s

    # 6. Enter email address in input and click arrow button

    Wait Until Element Is Visible    id=susbscribe_email    timeout=10s
    Input Text                       id=susbscribe_email    ${EMAIL}
    Click Element                    id=subscribe

    # 7. Verify success message 'You have been successfully subscribed!' is visible
    Wait Until Element Is Visible    id=success-subscribe    timeout=10s
    Element Text Should Be           id=success-subscribe    You have been successfully subscribed!

    [Teardown]    Close Browser
