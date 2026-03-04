*** Settings ***
Library    SeleniumLibrary
# Using your exact absolute path with forward slashes for safety
Library    DataDriver    file=C:/Users/KIIT01/PycharmProjects/Feb2026WiproRoboFramework/Testdata/ddtLogindata.xlsx

# Test Template allows a single keyword to be executed multiple times with different data sets
Test Template    Login Test
Test Setup       Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
Test Teardown    Close Browser

*** Test Cases ***
Login with user ${username} and ${password}    Default    UserData


*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}

    # Wait till the element is loaded
    Wait Until Element Is Visible    xpath=//input[@name='username']    timeout=10s

    # Enter the text in the username field
    Input Text    xpath=//input[@name='username']    ${username}

    # Enter text into the password field
    Input Text    xpath=//input[@name='password']    ${password}

    # Click login button
    Click Element    xpath=//button[@type='submit']

    # Give the website a moment to process the login before the teardown closes the browser
    Sleep    3s
    Log To Console    \nAttempted login with: ${username}