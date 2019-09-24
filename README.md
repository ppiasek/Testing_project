# Testing_project

# Basic configuration info
To connect to specific Gdrive account via API, json file should be downloaded from google developer
console. Location of that file should be provided in api.py _json_credentials variable. Also _token variable should
be filled with location of token.pickle file or if it does not exist yet, the location where we want to save it.

Location of Selenium drivers need to be provided in test_base.py module with use of forward slashes.
driver_location variable contains folder location of all required drivers
browser_driver variable contains names/remaining location of all required drivers
tested_url variable stores url for our site ti test.

# What works
- Going through left side menu via Selenium with assertions
- Logout with Selenium (chrome)
- API login
- API download file by id
- API upload file

# What semi works
- Login with Selenium in Chrome browser sometimes have the same issue as Firefox browser (after adding awful waits, this problem seems to be resolved)
- Selenium tests on Firefox browser are not working due to inability to log into google account (after adding awful waits, this problem seems to be resolved)

# Known bugs
- Pytest does not start due to __init__ in UIBase class.
