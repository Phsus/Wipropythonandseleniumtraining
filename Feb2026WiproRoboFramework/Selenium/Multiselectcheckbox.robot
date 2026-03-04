*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify multiselect check boxes
    # Start browser session
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Identify common elements using the attribute - //input[@type = 'checkbox']
    # We store the list of matching elements in the @{elements} list variable
    ${elements}=    Get WebElements    xpath://input[@type = 'checkbox']

    # Loop through the list of elements and click each one
    FOR    ${element}    IN    @{elements}
        Click Element    ${element}
        # Adding a small sleep as seen in the screenshot to observe the action
        Sleep    2s
    END

    # Close browser
    Close Browser