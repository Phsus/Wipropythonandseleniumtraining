*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${name}       John
${city}       Hyderabad
${address}    st peters Road

# Lists (Arrays)
@{list1}      green    red    blue
@{list2}      apple    banana    grapes

# Dictionary (Key-Value pairs)
&{creds}      username=admin    password=admin123

*** Test Cases ***
Verify the variables
    # Logging Scalar Variables
    Log To Console    Name: ${name}
    Log To Console    City: ${city}
    Log To Console    Address: ${address}

    # For Loop (Note the 2-space indentation inside the loop)
    FOR    ${element}    IN    @{list1}
        Log To Console    Color: ${element}
    END

    # Accessing specific list items (Index starts at 0)
    # Using square brackets inside the curly braces
    Log To Console    First Color: ${list1}[0]
    Log To Console    Second Color: ${list1}[1]

    # Accessing Dictionary items
    Log To Console    User: ${creds}[username]
    Log To Console    Pass: ${creds}[password]