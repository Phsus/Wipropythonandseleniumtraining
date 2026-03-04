*** Settings ***
Documentation    Page Object for OrangeHRM My Info / Personal Details Page
Library          SeleniumLibrary

*** Variables ***

${MENU_MY_INFO}      xpath=//span[text()='My Info']/parent::a
${TXT_FIRST_NAME}    name=firstName
${BTN_SAVE_INFO}     xpath=(//button[@type='submit'])[1]
${TOAST_SUCCESS}     xpath=//div[contains(@class, 'oxd-toast-content--success')]

*** Keywords ***
Navigate To My Info Page

    Wait Until Element Is Visible    ${MENU_MY_INFO}    timeout=10s
    Click Element                    ${MENU_MY_INFO}


    Wait Until Element Is Visible    ${TXT_FIRST_NAME}    timeout=10s

Update First Name
    [Arguments]    ${new_first_name}

    Press Keys       ${TXT_FIRST_NAME}    CTRL+a+BACKSPACE
    Input Text       ${TXT_FIRST_NAME}    ${new_first_name}

Save Personal Details
    Click Button     ${BTN_SAVE_INFO}

Verify Profile Successfully Updated

    Wait Until Element Is Visible    ${TOAST_SUCCESS}    timeout=10s
    Element Should Be Visible        ${TOAST_SUCCESS}