*** Settings ***
Library    SeleniumLibrary

*** Variables ***

${url}    https://the-internet.herokuapp.com/windows

*** Test Cases ***
Verify Window Switching

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s


    Click Element    link=Click Here
    Log To Console    \nClicked link to open a new tab.
    @{windows}=   Get Window Handles
    @{titles}=   Get Window Titles


    Sleep    2s


    Switch Window    title=New Window
    Log To Console    Successfully switched focus to the New Window.


    Element Text Should Be    xpath://h3[contains(text(),'New Window')]    New Window


    Switch Window    MAIN
    Log To Console    Successfully switched focus back to the MAIN window.


    Close Browser