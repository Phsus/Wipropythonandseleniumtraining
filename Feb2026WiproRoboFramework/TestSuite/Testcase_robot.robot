*** Settings ***
# setting we add the external library detail ,resources , set up and tear down commnds
Library  SeleniumLibrary

*** Test Cases ***
# name of the Testcase
Verify login with valid credentials
     Log   Enterusername
     Log   Enter password
     Log   click on login button
     Log   user is on the home page


