*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}          https://www.tutorialspoint.com/selenium/practice/upload-download.php

${file_path}    C:/Users/KIIT01/Downloads/Generated_Image_January_19__2026_-_1_39AM__1_-removebg-preview (1).png

*** Test Cases ***
Verify Tutorialspoint File Upload
    Open Browser    ${url}    chrome
    Maximize Browser Window


    Wait Until Element Is Visible    id=uploadFile    timeout=10s


    Choose File    id=uploadFile    ${file_path}

    Log To Console    \nSuccessfully attached the image file to the upload form.


    Sleep    3s

    Close Browser
