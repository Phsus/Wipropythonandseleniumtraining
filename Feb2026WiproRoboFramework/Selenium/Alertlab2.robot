*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Rahul Shetty Alerts
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Wait until the first button is loaded using its exact ID
    Wait Until Element Is Visible    id=alertbtn    timeout=10s

    # 1. Simple Alert - Click and Accept (OK)
    Click Element    id=alertbtn
    Handle Alert    action=ACCEPT    timeout=5s
    Log To Console    \n1. Simple Alert Accepted successfully
    Sleep    2s

    # 2. Confirm Box - Click and Dismiss (Cancel)
    # Using the exact ID provided in your HTML snippet
    Click Element    id=confirmbtn
    Handle Alert    action=DISMISS    timeout=5s
    Log To Console    2. Confirm Box Dismissed successfully
    Sleep    2s

    Close Browser
