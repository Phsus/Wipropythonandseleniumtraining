*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/drag_and_drop

*** Test Cases ***
Verify Drag And Drop
    Open Browser    ${url}    chrome

    # Maximize the browser window
    Maximize Browser Window

    # Wait till the element is loaded
    Sleep    3s
    Wait Until Element Is Visible    xpath://div[@id='column-a']
    Sleep    2s

    # Drag element A and drop it onto element B
    Drag And Drop    xpath://div[@id='column-a']    xpath://div[@id='column-b']

    Sleep    2s

    # Close browser
    Close Browser
