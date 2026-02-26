*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/frames.php

*** Test Cases ***
Verify Text Extraction From Multiple Frames
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s


    Sleep    2s


    Wait Until Element Is Visible    xpath=(//iframe)[1]    timeout=10s
    Select Frame    xpath=(//iframe)[1]
    Log To Console    \nSwitched into Frame 1.


    Wait Until Element Is Visible    xpath=//h1    timeout=5s
    ${frame1_text}=    Get Text    xpath=//h1
    Log To Console    Text found in Frame 1: ${frame1_text}


    Unselect Frame
    Log To Console    Exited Frame 1.


    Wait Until Element Is Visible    xpath=(//iframe)[2]    timeout=10s
    Select Frame    xpath=(//iframe)[2]
    Log To Console    Switched into Frame 2.


    Wait Until Element Is Visible    xpath=//body    timeout=5s
    ${frame2_text}=    Get Text    xpath=//body
    Log To Console    Text found in Frame 2: ${frame2_text}


    Unselect Frame
    Log To Console    Exited Frame 2.


    Close Browser
