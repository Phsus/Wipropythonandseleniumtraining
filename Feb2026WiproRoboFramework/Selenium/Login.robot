*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}     https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}     chrome

*** Test Cases ***
Verify login scenario with valid credentials
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    # Added a small sleep because OrangeHRM often has a loading lag
    Set Selenium Implicit Wait    10 seconds

Login
    # Wait until the username field is visible before interacting
    Wait Until Element Is Visible    xpath://input[@name='username']
    Input Text      xpath://input[@name='username']    admin

    # Input Password
    Input Text      xpath://input[@name='password']    admin123

    # Click Login
    Click Element   xpath://button[@type='submit']

    # Validate successful login by checking the dashboard breadcrumb
    # Validate that the user reached the home page by checking the header breadcrumb
    Wait Until Element Is Visible    xpath://h6[contains(@class,'oxd-topbar-header-breadcrumb-module')]
    Element Should Be Visible       xpath://h6[contains(@class,'oxd-topbar-header-breadcrumb-module')]

Close the Browser
    Close Browser



