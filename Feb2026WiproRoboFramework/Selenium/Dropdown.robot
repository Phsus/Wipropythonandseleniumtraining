# selecting the visible text
#selecting by index
# selecting the value


*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify drop downs
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Wait until the dropdown element is loaded
    Wait Until Element Is Visible    id=dropdown-class-example

    # Get the currently selected label and log it
    ${labels}=    Get Selected List Labels    id=dropdown-class-example
    Log    ${labels}

    # select by label - visible text
    Select From List By Label    id=dropdown-class-example    Option3
    Sleep    2s

    # select by index
    Select From List By Index    id=dropdown-class-example    2
    Sleep    2s

    # select by value
    Select From List By Value    id=dropdown-class-example    option1
    Sleep    2s

    Close Browser
