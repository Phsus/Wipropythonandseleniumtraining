*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@value = 'radio1']
    Click Element    xpath://input[@value = 'radio1']
    Click Element    id=checkBoxOption3
    Close Browser