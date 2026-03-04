*** Settings ***
Library    Collections

*** Variables ***

${NAME}       John Doe
${CITY}       Hyderabad
@{FRUITS}     Apple    Banana    Mango    Grapes
&{USER}       username=admin    email=admin@test.com

*** Test Cases ***
Scenario 1: Scalar Variables and Math
    # Task 1: Print scalar variable
    Log To Console    \nName: ${NAME}

    # Task 2: Assign numbers and print sum
    ${num1}    Set Variable    10
    ${num2}    Set Variable    20
    ${sum}     Evaluate    ${num1} + ${num2}
    Log To Console    Sum of ${num1} and ${num2} is: ${sum}

    # Task 3: Use variable in a sentence
    Log To Console    I am currently living in ${CITY}.

Scenario 2: Variable Reassignment and Lists
    # Task 4: Reassign a variable
    ${STATUS}    Set Variable    Initial State
    ${STATUS}    Set Variable    Updated State
    Log To Console    Updated Status: ${STATUS}

    # Task 5: Print first item of a list
    Log To Console    First Fruit: ${FRUITS}[0]

    # Task 6: Loop through a list
    FOR    ${fruit}    IN    @{FRUITS}
        Log To Console    Fruit Name: ${fruit}
    END

    # Task 7: Find length of a list
    ${length}    Get Length    ${FRUITS}
    Log To Console    Total fruits in list: ${length}

Scenario 3: Dictionary Operations
    # Task 8: Print dictionary key value
    Log To Console    User Email: ${USER}[email]

    # Task 9: Add new key-value pair
    Set To Dictionary    ${USER}    phone=9876543210
    Log To Console    Updated User: ${USER}

    # Task 10: Loop through dictionary keys and values
    FOR    ${key}    IN    @{USER.keys()}
        Log To Console    Key: ${key} | Value: ${USER}[${key}]
    END
