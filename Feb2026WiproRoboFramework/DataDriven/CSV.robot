*** Settings ***
Library    SeleniumLibrary

Library    DataDriver    file=C:/Users/KIIT01/PycharmProjects/Feb2026WiproRoboFramework/Testdata/ddtLogindataCSV.csv.csv

Test Template    Login Test
Test Setup       Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
Test Teardown    Close Browser

*** Test Cases ***

Login with user ${username} and ${password}    Default    UserData


*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}


    Wait Until Element Is Visible    xpath=//input[@name='username']    timeout=10s


    Input Text    xpath=//input[@name='username']    ${username}
    Input Text    xpath=//input[@name='password']    ${password}


    Click Element    xpath=//button[@type='submit']


    Sleep    3s
    Log To Console    \nAttempted login with username: ${username}