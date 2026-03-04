*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://jqueryui.com/datepicker/

*** Test Cases ***
Verify Datepicker Selection Inside Frame
    # Open the browser and navigate to the jQuery UI site
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # 1. SWITCHING TO THE FRAME
    # The calendar widget is actually embedded inside a mini web page (iframe).
    # Selenium cannot see it until we explicitly switch our focus inside that frame!
    Wait Until Element Is Visible    xpath=//iframe[@class='demo-frame']    timeout=10s
    Select Frame    xpath=//iframe[@class='demo-frame']
    Log To Console    \nSuccessfully switched inside the iframe.

    # 2. INTERACTING WITH THE CALENDAR
    # Click the input field to make the calendar pop up
    Click Element    id=datepicker
    Sleep    1s

    # Click on the date '21' using an exact text match XPath
    Click Element    xpath=//a[text()='21']
    Log To Console    Selected the date '21' from the calendar.

    # Give it a second so you can visually confirm the date was entered into the box
    Sleep    2s

    # 3. SWITCHING BACK
    # Always return to the main HTML document when you are done inside a frame!
    Unselect Frame
    Log To Console    Switched focus back to the main default web page.

    # Close the browser
    Close Browser
