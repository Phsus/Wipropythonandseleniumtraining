*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify Screenshot Capture
    Open Browser    ${url}    chrome


    Maximize Browser Window


    Sleep    3s
    Wait Until Element Is Visible    xpath://input[@id='file-upload']    timeout=10s


    Capture Page Screenshot    Robo5.png
    Log To Console    \nSuccessfully captured full page screenshot: Robo5.png


    Capture Element Screenshot    xpath://input[@id='file-upload']    Robo6.png
    Log To Console    Successfully captured element screenshot: Robo6.png

    Sleep    2s


    Close Browser

