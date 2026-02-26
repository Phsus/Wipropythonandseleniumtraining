*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify Scroll And Click

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    Sleep    3s

    Scroll Element Into View    link=Sell on Amazon
    Log To Console    \nSuccessfully scrolled to the 'Sell on Amazon' link.
    Sleep    2s

    Click Element    link=Sell on Amazon
    Log To Console    Clicked the link.
    Sleep    3s

    Title Should Be    Amazon.in: Selling on Amazon - Start Selling Now
    Log To Console    Page title verified successfully!
    Close Browser
