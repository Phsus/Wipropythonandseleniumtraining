*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify multiselect check boxes
    # Start browser session
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Wait for the elements to be present in the DOM
    Wait Until Element Is Visible    xpath://input[@type = 'checkbox']    timeout=10s

    # Identify all checkbox elements and store them in a list variable
    # [Working: Collecting all elements matching the type 'checkbox']
    ${elements}=    Get WebElements    xpath://input[starts-with(@id,'c_bs_')]

    # Loop through the list of elements and click each one
    FOR    ${element}    IN    @{elements}
        # [Working: Clicking individual element in loop]
        Click Element    ${element}
        # Adding a sleep to observe the checkboxes being checked one by one
        Sleep    2s
    END

    # Close browser session
    Close Browser