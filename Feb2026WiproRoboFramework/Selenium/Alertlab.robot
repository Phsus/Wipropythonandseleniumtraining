*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/alerts.php

*** Test Cases ***
Verify All Tutorialspoint Alerts
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Wait until the first button is loaded
    Wait Until Element Is Visible    xpath=//button[@onclick='showAlert()']    timeout=10s

    # 1. Simple Alert
    Click Element    xpath=//button[@onclick='showAlert()']
    Handle Alert    action=ACCEPT    timeout=5s
    Log To Console    \n1. Simple Alert Accepted
    Sleep    2s

    # 2. Timer/Message Alert (Using your specific onclick attribute)
    Click Element    xpath=//button[@onclick='myMessage()']
    # Keeping the 10s timeout because this specific button usually has a built-in delay
    Handle Alert    action=ACCEPT    timeout=10s
    Log To Console    2. Timer Alert Accepted
    Sleep    2s

    # 3. Confirm Box (Using your specific onclick attribute)
    Click Element    xpath=//button[@onclick='myDesk()']
    Handle Alert    action=DISMISS    timeout=5s
    Log To Console    3. Confirm Box Dismissed
    Sleep    2s

    # 4. Prompt Box (Using your specific onclick attribute)
    Click Element    xpath=//button[@onclick='myPromp()']
    Input Text Into Alert    hello    action=ACCEPT
    Log To Console    4. Prompt Box Handled successfully
    Sleep    2s

    Close Browser