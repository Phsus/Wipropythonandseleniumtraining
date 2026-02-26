*** Settings ***
Documentation     Automation Exercise - Logout User Test
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Firefox
${URL}            http://automationexercise.com

${EMAIL}          sushantchoudhary586@gmail.com
${PASSWORD}       Test@1234
${USERNAME}       SUSHANT

*** Test Cases ***
Logout User Successfully
    [Documentation]    Test Case 4: Login and then Logout User using Firefox

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

    # 8. Verify that 'Logged in as username' is visible
    Wait Until Element Is Visible    xpath=//a[contains(., 'Logged in as') and contains(., '${USERNAME}')]    timeout=10s
    Element Should Be Visible        xpath=//a[contains(., 'Logged in as') and contains(., '${USERNAME}')]

    # 9. Click 'Logout' button
    Click Element    xpath=//a[@href='/logout']

    # 10. Verify that user is navigated to login page
    Wait Until Element Is Visible    xpath=//h2[text()='Login to your account']    timeout=10s
    Element Should Be Visible        xpath=//h2[text()='Login to your account']
    Location Should Be               ${URL}/login

    [Teardown]    Close Browser
