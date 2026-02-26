*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify Right Click And Double Click

    Open Browser    ${url}    firefox
    Maximize Browser Window


    Sleep    3s


    Wait Until Element Is Visible    xpath://a[normalize-space()='Sell']    timeout=10s
    Open Context Menu    link=Sell
    Log To Console    \nSuccessfully right-clicked on the 'Sell' link.
    Sleep    2s



    Wait Until Element Is Visible    xpath://a[normalize-space()='Mobiles']    timeout=10s
    Double Click Element    xpath://a[normalize-space()='Mobiles']
    Log To Console    Successfully double-clicked on the 'Mobiles' link.
    Sleep    2s


    Close Browser
