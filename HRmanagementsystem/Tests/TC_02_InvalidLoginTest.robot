*** Settings ***
Documentation    Test Suite for OrangeHRM Invalid Login Functionality
Library          SeleniumLibrary
Resource         ../Resource/LoginPage.resource
Test Teardown    Close Browser

*** Variables ***

${VALID_USER}      Admin
${INVALID_PASS}    wrongpassword123

*** Test Cases ***
TC_02 Verify Error message on unsuccessful Employee login to OrangeHRM portal
    [Documentation]    Verify that logging in with an invalid password shows an exact error message.

    Given Orange HRM site is launched on a compatible browser
    When User enters valid username and invalid password
    And User clicks on login button
    Then An Error message is displayed with exact text Invalid credentials

*** Keywords ***


Orange HRM site is launched on a compatible browser
    Navigate To OrangeHRM Login Page

User enters valid username and invalid password
    Enter Credentials    ${VALID_USER}    ${INVALID_PASS}

User clicks on login button
    Submit Login Form

An Error message is displayed with exact text Invalid credentials
    Verify Invalid Credentials Error Message