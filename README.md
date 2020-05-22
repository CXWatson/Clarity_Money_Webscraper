# Clarity Money Webscraper
## A webscraper that pulls in transaction information from the budgeting app Clarity Money.
## Intro
This webscraper is designed to pull transaction dates, transaction information, and transaction prices and writes it all into a csv file.

This webscraper logs into Clarity Money desktop interface using chrome webdriver. It fills in the information automatically, logs in automatically, clicks the "See More" button to add more transactions to, and then grabs all the transactions.

## Requirements
- Need to download the corresponding version of chromedriver for your current version of Google Chrome
- Need to set up a chrome user profile to bypass two factor authentification. Without this it will ask you the access code every time you try to log in with chrome driver.
- (Optional) Since this is being saved publicly the email and password information is saved in a shell file outside this script. you can do the same. If not you can set the email and password variables to your email and password.