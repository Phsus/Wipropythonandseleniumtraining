*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}             https://the-internet.herokuapp.com/download
# Updated path to match your actual Windows user profile from previous logs
${download_dir}    C:/Users/KIIT01/Downloads
${expected_file}   upload.txt

*** Test Cases ***
Verify File Download And Check Directory
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Wait for the link and click it to trigger the download
    Wait Until Element Is Visible    link=${expected_file}    timeout=10s
    Click Link    link=${expected_file}
    Log To Console    \nTriggered download for ${expected_file}... waiting 5s for it to finish.

    # Give the browser time to actually download and save the file
    Sleep    5s

    # --- File Verification Logic ---
    # 1. Grab all files in your Windows Downloads folder
    ${files}=    List Files In Directory    ${download_dir}

    # 2. Assert that our specific downloaded file is inside that list
    List Should Contain Value    ${files}    ${expected_file}

    Log To Console    Success! Found ${expected_file} in ${download_dir}.
    Close Browser