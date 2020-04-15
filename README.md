## Dairy spread 

Dairy spread creates a google spreadsheet from a vcf. 
Each record in the spreadsheet contains a hyperlink representing the location of the variant, 
and additional columns representing user-defined parts of the vcf record, e.g., INFO.AC. 
The links can be used to visually inspect the variant in igv.js,
while the spreadsheet can be used to record any conclusions drawn from the manual inspection. 

## Table of contents 

## Obtain credentials for the Google Drive API 

Create a project at https://console.cloud.google.com/ Here I've created one called "paddy": 

<img width="400" src="images/1.png">

Click "Go to API overview": 

<img width="200" src="images/2.png">

Click "ENABLE APIS AND SERVICES": 

<img width="200" src="images/3.png">

In the search box that appears, type "Google Drive": 

<img width="500" src="images/4.png">

Click "ENABLE": 

<img src="images/5.png">

Click "CREATE CREDENTIALS": 

<img src="images/6.png">

Select the options indicated below: 

<img src="images/7.png">

and click "What credentials do I need". On the next screen, select "Project Editor" in the "Role" dropdown
and fill in the "Service account name" as indicated: 

<img src="images/8.png">

Clicking "Continue" will download a json file that should be renamed to "credentials.json" and moved to this folder. 

For security, run `chmod og-r credentials.json`. 

Navigate back to https://console.cloud.google.com/ and click "ENABLE APIS AND SERVICES" again to enable the Google Sheets API. 

Wait at least 15 minutes for the requests to enable the two APIs to propagate to google's systems. 


## TODO 




