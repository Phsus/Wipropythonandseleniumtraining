*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://www.tutorialspoint.com/selenium/practice/check-box.php
${BROWSER}     chrome

*** Test Cases ***
Verify Checkbox Selection
    # Start the automation session
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Wait for the first checkbox to be interactable
    Wait Until Element Is Visible    xpath://input[@id='c_bs_2']    timeout=10s

    # Click Checkpoint 1 using provided relative XPath
    # [Working: Clicking Checkpoint 1]
    Click Element    xpath://input[@id='c_bs_2']

    # Click Checkpoint 2 using provided relative XPath
    # [Working: Clicking Checkpoint 2]
    Click Element    xpath://input[@id='c_bs_1']

    # Log status to console to show progress
    Log To Console    Successfully clicked Checkpoint 1 and Checkpoint 2

    # Brief sleep to see the result before closing (optional)
    Sleep    2s

    # End the session
    Close Browser
