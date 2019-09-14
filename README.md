# Testing_project

To connect to specific Gdrive account, credentials.json file should be downloaded from google developer console.

Selenium drivers need to be provided in test_base.py module with use of forward slashes.
driver_location variable contains folder location of all required drivers
browser_driver variable contains names/remaining location of all required drivers

# What works
- Login with Selenium in Chrome browser (Windows / Linux?)
- API login
- API download file by id
- API upload file

# Known bugs
- Login with Selenium does not work in Firefox browser, due to problem with clicking "Next" button after providing
password (Windows / Linux?)