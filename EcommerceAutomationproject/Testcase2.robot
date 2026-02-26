*** Settings ***
Documentation     Automation Exercise - Login User Test
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Firefox
${URL}            http://automationexercise.com

${EMAIL}          sushantchoudhary586@gmail.com
${PASSWORD}       Test@1234

*** Test Cases ***
Login User With Correct Email And Password
    [Documentation]    Test Case 2: Login User with correct email and password using Firefox

    # 1. Launch browser & 2. Navigate to url
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # 3. Verify that home page is visible successfully
    Wait Until Element Is Visible    xpath=//a[@href='/']    timeout=10s
    Element Should Be Visible        xpath=//a[@href='/']

    # 4. Click on 'Signup / Login' button
    Click Element    xpath=//a[@href='/login']

    # 5. Verify 'Login to your account' is visible
    Wait Until Element Is Visible    xpath=//h2[text()='Login to your account']    timeout=10s
    Element Should Be Visible        xpath=//h2[text()='Login to your account']

    # 6. Enter correct email address and password
    Input Text       css=[data-qa="login-email"]       ${EMAIL}
    Input Text       css=[data-qa="login-password"]    ${PASSWORD}

    # 7. Click 'login' button
    Click Button     css=[data-qa="login-button"]

     Verify successful login
    Wait Until Element Is Visible    xpath=//a[contains(., 'Logged in as')]    timeout=10s

    [Teardown]    Close Browser