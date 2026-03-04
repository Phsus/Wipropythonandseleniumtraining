*** Settings ***
Documentation    Test Suite for OrangeHRM Personal Information Modification
Library          SeleniumLibrary
Library    Telnet
Resource         ../Resource/LoginPage.resource
Resource         ../Resource/MyInfoPage.resource
Test Teardown    Close Browser

*** Variables ***

${VALID_USER}      Admin
${VALID_PASS}      admin123
${NEW_FIRST_NAME}  Sushant

*** Test Cases ***
TC_03 Verify Personal details modification with valid values First Name
    [Documentation]    Verify that an ESS User can successfully update their First Name.

    Given Orange HRM site is launched and user is logged in
    When User navigates to Personal Information Page
    And User updates First Name with a valid new value
    And User clicks on Save button
    Then A success message is displayed indicating the profile was updated

*** Keywords ***


Orange HRM site is launched and user is logged in

    Navigate To OrangeHRM Login Page
    Enter Credentials    ${VALID_USER}    ${VALID_PASS}
    Submit Login Form
    Verify Dashboard Is Displayed

User navigates to Personal Information Page
    Navigate To My Info Page

User updates First Name with a valid new value
    Update First Name    ${NEW_FIRST_NAME}

User clicks on Save button
    Save Personal Details

A success message is displayed indicating the profile was updated
    Verify Profile Successfully Updated
