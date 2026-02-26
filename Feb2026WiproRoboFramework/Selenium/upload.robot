*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}          https://the-internet.herokuapp.com/upload
${file_path}    C:/Users/KIIT01/Downloads/Generated_Image_January_19__2026_-_1_39AM__1_-removebg-preview (1).png

*** Test Cases ***
Verify Actual File Upload
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Wait until the hidden upload input is ready
    Wait Until Element Is Visible    id=file-upload    timeout=10s

    # Attach the file from your local machine to the web page
    Choose File    id=file-upload    ${file_path}
    Log To Console    \nFile selected from Downloads folder.

    # Click the "Upload" submit button
    Click Element    id=file-submit

    # Verify the page changes and displays the success message
    Wait Until Element Is Visible    xpath=//h3[normalize-space()='File Uploaded!']    timeout=10s
    Element Text Should Be           xpath=//h3[normalize-space()='File Uploaded!']    File Uploaded!

    Log To Console    Success message verified!
    Sleep    2s

    Close Browser
