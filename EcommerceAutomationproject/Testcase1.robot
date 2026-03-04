*** Settings ***
Documentation     Automation Exercise - Register User Test
Library           SeleniumLibrary
Library           String

*** Variables ***
${BROWSER}        Chrome
${URL}            http://automationexercise.com
${NAME}           SUSHANT
${PASSWORD}       Test@1234
${FIRST_NAME}     Sushant
${LAST_NAME}      Choudhary
${COMPANY}        MyCompany
${ADDRESS1}       123 Main St
${ADDRESS2}       Apt 4B
${STATE}          Delhi
${CITY}           New Delhi
${ZIPCODE}        110001
${MOBILE}         1234567890

*** Test Cases ***
Register User On Automation Exercise
    [Documentation]    End to End test to register a new user on Automation Exercise.

    # 1. Launch browser & 2. Navigate to URL
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # 3. Verify that home page is visible successfully
    Wait Until Element Is Visible    xpath=//a[@href='/']    timeout=10s
    Element Should Be Visible        xpath=//a[@href='/']

    # 4. Click on 'Signup / Login' button
    Click Element    xpath=//a[@href='/login']

    # 5. Verify 'New User Signup!' is visible
    Wait Until Element Is Visible    xpath=//h2[text()='New User Signup!']    timeout=10s

    # 6. Enter name and email address (Using random email to ensure script works multiple times)
    ${random_string}=    Generate Random String    5    [LOWER]
    ${random_email}=     Set Variable    sushant${random_string}@gmail.com
    Input Text       css=[data-qa="signup-name"]     ${NAME}
    Input Text       css=[data-qa="signup-email"]    ${random_email}

    # 7. Click 'Signup' button
    Click Button     css=[data-qa="signup-button"]

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    Wait Until Element Is Visible    xpath=//b[text()='Enter Account Information']    timeout=10s

    # 9. Fill details: Title, Name, Email , Password, Date of birth
    Click Element    id=id_gender1
    Input Text       id=password    ${PASSWORD}
    Select From List By Value    id=days      10
    Select From List By Value    id=months    5
    Select From List By Value    id=years     1990

    # 10. Select checkbox 'Sign up for our newsletter!'
    Select Checkbox  id=newsletter

    # 11. Select checkbox 'Receive special offers from our partners!'
    Select Checkbox  id=optin

    # 12. Fill details: First name, Last name, Company, Address, etc.
    Input Text       id=first_name        ${FIRST_NAME}
    Input Text       id=last_name         ${LAST_NAME}
    Input Text       id=company           ${COMPANY}
    Input Text       id=address1          ${ADDRESS1}
    Input Text       id=address2          ${ADDRESS2}
    Select From List By Value    id=country   India
    Input Text       id=state             ${STATE}
    Input Text       id=city              ${CITY}
    Input Text       id=zipcode           ${ZIPCODE}
    Input Text       id=mobile_number     ${MOBILE}

    # 13. Click 'Create Account' button
    Click Button     css=[data-qa="create-account"]

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    Wait Until Element Is Visible    xpath=//b[text()='Account Created!']    timeout=10s

    # 15. Click 'Continue' button
    Click Element    css=[data-qa="continue-button"]

    # 16. Verify that 'Logged in as username' is visible
    Wait Until Element Is Visible    xpath=//a[contains(., 'Logged in as') and contains(., '${NAME}')]    timeout=10s
    Element Should Be Visible        xpath=//a[contains(., 'Logged in as') and contains(., '${NAME}')]

    [Teardown]    Close Browser
