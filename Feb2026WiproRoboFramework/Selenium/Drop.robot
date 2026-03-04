*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php

*** Test Cases ***
Verify State and City Dropdowns
    # Open the browser and navigate to the practice page
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Wait until the State dropdown is visible on the screen
    Wait Until Element Is Visible    id=state    timeout=10s

    # Select the State by Value based on the HTML (<option value="Uttar Pradesh">)
    Select From List By Value    id=state    Uttar Pradesh
    Log To Console    State 'Uttar Pradesh' selected successfully.

    # Adding a sleep to observe the selection
    Sleep    2s

    # Wait until the City dropdown is visible
    # (On many websites, city dropdowns only activate AFTER a state is chosen)
    Wait Until Element Is Visible    id=city    timeout=10s

    # Select the City by Label based on the visible text (>Lucknow<)
    Select From List By Label    id=city    Lucknow
    Log To Console    City 'Lucknow' selected successfully.

    # Adding a sleep to observe the selection
    Sleep    2s

    # Close the browser session
    Close Browser
