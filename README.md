## Progammatic spreadsheets in bioinformatics 

Often it is useful to have bioinformatics data in a spreadsheet, 
where the data can be easily visualized, annotated manually, and shared with collaborators from diverse 
backgrounds.
To integrate this approach into a data-analysis pipeline, 
it is useful to be able to programatically interact with the spreadsheet,
e.g., create the spreadsheet from a traditional bioinformatics data file, 
or read data from the spreadsheet after it has been manually curated in order to push that data into another pipeline.
The code in this repository represents a first step in this direction.  

**dairy-spread** allows you to create a google spreadsheet at the command line from a bed file,
and to delete a spreadsheet so created, also from the command line.
The bed file is assumed to have at least four columns, with the fourth column formated according to the [gfftags spec](https://software.broadinstitute.org/software/igv/BED), and an optional `#gffTags` header line. 
Each record in the spreadsheet contains a hyperlink representing the location of the locus, 
and additional columns corresponding to the tags in the fourth column. 
The link can be used to visually inspect the locus in `igv.js`,
while the spreadsheet can be used to record any conclusions drawn from the manual inspection of the igv visualization. 
This can be useful during the development of variant-calling software, 
when one often needs to manually inspect and annotate cases where (i) the software is not capturing variants that are known to exist, 
and/or (ii) the software is making calls where variants are known to be absent. 

## How to get dairy-spread working

1. [Obtain credentials for the Google Drive API](#obtain-credentials-for-the-google-drive-api)
2. [Install dependencies](#install-dependencies)
3. Run the tool at the command line 

## Obtain credentials for the Google Drive API 

Create a project at https://console.cloud.google.com/ Here I've created one called "paddy": 

<img width="300" src="images/1.png">

Click "Go to API overview": 

<img width="200" src="images/2.png">

Click "ENABLE APIS AND SERVICES": 

<img width="200" src="images/3.png">

In the search box that appears, type "Google Drive": 

<img width="500" src="images/4.png">

Click "ENABLE": 

<img width="400" src="images/5.png">

Click "CREATE CREDENTIALS": 

<img width="900" src="images/6.png">

Select the options indicated below: 

<img width="500" src="images/7.png">

and click "What credentials do I need". On the next screen, select "Project Editor" in the "Role" dropdown
and fill in the "Service account name" as indicated: 

<img width="500" src="images/8.png">

Clicking "Continue" will download a json file that should be renamed to `credentials.json` and moved to this folder. 

For security, run `chmod og-r credentials.json`. 

Navigate back to https://console.cloud.google.com/ and click "ENABLE APIS AND SERVICES" again to enable the Google Sheets API. 

Wait at least 15 minutes for the requests to enable the two APIs to propagate to google's systems. 


## Install dependencies 

```
conda create --name dairy-spread python=3.7 gspread google-auth
```

## Run the tool at the command line 

Create a spreadsheet from a bed file: 
```
python create_spreadsheet.py \
  --bed ${bed} \
  --title "my spreadsheet name" \
  --credentials "credentials.json" \
  --email "my.name@gmail.com" 
```

Remove the spreadsheet: 
```
python remove_spreadsheet.py --bed ${bed} --credentials credentials.json 
```

## TODO 
* remove dependency on `gspread` and credentials by following https://youtu.be/VLdrgE8iJZI
