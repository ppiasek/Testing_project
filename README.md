# Testing_project

# Basic configuration info
# API tests:
To connect to specific Gdrive account via API, json file should be downloaded from google developer
console. Location of that file should be provided in api.py _json_credentials variable. Also _token variable should
be filled with location of token.pickle file or if it does not exist yet, the location where we want to save it.

#Selenium tests:
Location of Selenium drivers need to be provided in driver.py module with use of forward slashes.
driver_location variable contains folder location of all required drivers.
browser_driver variable contains names/remaining location of all required drivers.
tested_url variable stores url for our site to test.
Evidence folder as well as credentials file is provided in ui_functions.py file.
Evidence naming is using executed file name for folder name and executed function name for filename.


# What works
- Login with Selenium
- Logout with Selenium
- Screenshots with correct naming folders/files (folders with executed file name, files with executed function name)
- Self made custom selenium actions with waits until Expected Condition is fulfilled
- API login
- API download file by id
- API upload file

# What semi works
- Depending of machine performance, going through left side menu via Selenium with assertions may need some static waits before assertions (to be verified)
- In TearDown function ui objects are not recognizable for some reason, even though they are correctly executed

# Known bugs
- Pytest does not work due to inability to find selenium package ;(

#To be done:
- Allure reporting
- Separate tests and testing framework to different repositories
- create python package
- improve and add new API tests
