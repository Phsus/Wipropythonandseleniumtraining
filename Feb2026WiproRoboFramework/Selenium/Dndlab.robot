*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/droppable.php

*** Test Cases ***
Verify Tutorialspoint Drag And Drop
    Open Browser    ${url}    chrome
    Maximize Browser Window


    Wait Until Element Is Visible    id=droppable    timeout=10s


    Wait Until Element Is Visible    xpath=//p[text()='Drag me to my target']    timeout=10s


    Drag And Drop    xpath=//p[text()='Drag me to my target']    id=droppable

    Log To Console    \nElement successfully dragged and dropped!


    Sleep    3s

    Close Browser