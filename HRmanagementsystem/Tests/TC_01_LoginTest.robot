*** Settings ***
Documentation    Test Suite for OrangeHRM Login Functionality
Library          SeleniumLibrary

Resource         ../Resource/LoginPage.resource
Test Teardown    Close Browser

*** Variables ***

${VALID_USER}    Admin
${VALID_PASS}    admin123

*** Test Cases ***
TC_01 Verify Successful Employee login to OrangeHRM portal
    [Documentation]    Verify that an employee can login successfully with valid credentials.

    Given Orange HRM site is launched on a compatible browser
    When User enters valid username and password
    And User clicks on login button
    Then User is logged in successfully and dashboard is displayed

*** Keywords ***


Orange HRM site is launched on a compatible browser
    Navigate To OrangeHRM Login Page

User enters valid username and password
    Enter Credentials    ${VALID_USER}    ${VALID_PASS}

User clicks on login button
    Submit Login Form

User is logged in successfully and dashboard is displayed
    Verify Dashboard Is Displayed