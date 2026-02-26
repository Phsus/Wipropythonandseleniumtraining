*** Settings ***
# setting we add the external library detail ,resources , set up and tear down commnds
Library   SeleniumLibrary

*** Test Cases ***
# name of the Testcase
Verify login with valid credentials
     Log To Console   Enterusername
     Log To Console  Enter password
     Log To Console  click on login button
     Log To Console  user is on the home page



