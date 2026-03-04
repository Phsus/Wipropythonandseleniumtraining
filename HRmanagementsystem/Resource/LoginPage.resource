*** Settings ***
Documentation    Page Object for OrangeHRM Login Page
Library          SeleniumLibrary

*** Variables ***
${LOGIN_URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}          Chrome


${TXT_USERNAME}     name=username
${TXT_PASSWORD}     name=password
${BTN_LOGIN}        css=[type="submit"]
${LBL_DASHBOARD}    xpath=//h6[contains(@class, 'oxd-text') and text()='Dashboard']
${LBL_ERROR_MSG}    xpath=//p[contains(@class, 'oxd-alert-content-text')]

*** Keywords ***
Navigate To OrangeHRM Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${TXT_USERNAME}    timeout=10s

Enter Credentials
    [Arguments]    ${username}    ${password}
    Input Text     ${TXT_USERNAME}    ${username}
    Input Text     ${TXT_PASSWORD}    ${password}

Submit Login Form
    Click Button   ${BTN_LOGIN}

Verify Dashboard Is Displayed
    Wait Until Element Is Visible    ${LBL_DASHBOARD}    timeout=10s
    Element Should Be Visible        ${LBL_DASHBOARD}
    Location Should Contain          /web/index.php/dashboard

Verify Invalid Credentials Error Message

    Wait Until Element Is Visible    ${LBL_ERROR_MSG}    timeout=10s
    Element Text Should Be           ${LBL_ERROR_MSG}    Invalid credentials

    Location Should Contain          /auth/login