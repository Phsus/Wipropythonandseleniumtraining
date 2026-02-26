*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Window Switching On Rahul Shetty Page

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s


    Click Element    id=opentab
    Log To Console    \nClicked 'Open Tab' button.


    Sleep    3s


    Switch Window    NEW
    Log To Console    Successfully switched focus to the new tab.


    Location Should Contain    qaclickacademy
    Log To Console    Verified we are on the QAClick Academy page.


    Close Window
    Log To Console    Closed the new tab.


    Switch Window    MAIN
    Log To Console    Successfully switched focus back to the MAIN window.


    Title Should Be    Practice Page
    Log To Console    Verified we are back on the Rahul Shetty Practice Page.


    Close Browser
