*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/hovers

*** Test Cases ***
Verify Mouse Hover
    Open Browser    ${url}    chrome


    Maximize Browser Window


    Sleep    3s


    Wait Until Element Is Visible    xpath://div[@class='example']//div[1]//img[1]    timeout=10s


    Mouse Over    xpath://div[@class='example']//div[1]//img[1]
    Log To Console    \nHovered over the first user avatar.


    Sleep    2s


    Element Should Be Visible    xpath://h5[contains(text(),'name: user1')]
    Log To Console    Hidden text 'name: user1' successfully appeared!


    Close Browser
