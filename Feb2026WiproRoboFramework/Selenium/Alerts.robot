*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Verify JavaScript Alerts
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Wait until the first button is loaded
    Wait Until Element Is Visible    xpath=(//button)[1]    timeout=10s

    # 1. Informational Alert - ACCEPT
    Click Element    xpath=(//button)[1]
    Handle Alert    action=ACCEPT    timeout=3
    Sleep    2s

    # 2. Confirmational Alert - DISMISS
    Click Element    xpath=(//button)[2]
    Handle Alert    action=DISMISS    timeout=3
    Sleep    2s

    # 3. Prompt Alert - Enter text and accept
    Click Element    xpath=(//button)[3]
    Input Text Into Alert    Hello    action=ACCEPT
    Sleep    2s

    Close Browser