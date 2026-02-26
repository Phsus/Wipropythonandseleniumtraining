*** Settings ***
Library    SeleniumLibrary

*** Variables ***

${base_url}    https://www.amazon.in/

*** Test Cases ***
Verify link texts and URLs
    Open Browser    ${base_url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s


    Sleep    3s


    ${links}=    Get WebElements    xpath://a

    Log To Console    \n--- Extracting Links ---


    ${counter}=    Set Variable    0

    FOR    ${link}    IN    @{links}
        ${text}=    Get Text    ${link}



        ${href_link}=    Get Element Attribute    ${link}    href

        Log To Console    Text: ${text} | URL: ${href_link}


        ${counter}=    Evaluate    ${counter} + 1
        Run Keyword If    ${counter} == 5    Exit For Loop
    END

    Close Browser
