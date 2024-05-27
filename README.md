# Original creator
https://github.com/andprov 
https://github.com/andprov/krisha.kz

# Objectives and goals
1. Modify an original code to make it suitable to deploy in Google Collab 
2. Provide user-friendly (for non-tech users) output

# Real Estate Rental Site Parser krisha.kz

[![License: MIT](https://img.shields.io/github/license/andprov/krisha.kz?color=blueviolet)](https://github.com/andprov/krisha.kz/blob/main/LICENSE.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python versions](https://img.shields.io/badge/python-_3.10_|_3.11_|_3.12-blue)](https://www.python.org/)

# Description

Searches and views listings based on the specified [parameters](#params):
- Requests data from preview pages of listings. Finds links to pages with detailed descriptions.
- Visits the detailed description pages of each listing and collects data.
- Stores results in a CSV file
- Processes entities until reaches the limit configured in main.py

Search parameters selection replicates the website's functionality. To specify search parameters, use the `SEARCH_PARAMETERS.json` file in the project's root directory.

### Third-party libraries used in the project
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests](https://requests.readthedocs.io/en/latest/)

# Installation and Running

Clone the repository:
```
git clone <https or SSH URL>
```

Navigate to the project folder:
```
cd krisha.kz
```

Create a virtual environment:
```
python3 -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Specify search parameters in the `SEARCH_PARAMETERS.json` file: [see examples](#examples)

Run the script:
```
python main.py
```

# Setting Up Scheduled Runs

Edit the cron.sh file, adding your project path:
```
#!/bin/bash
cd /home/< user-name >/< dir-name >/krisha.kz
source venv/bin/activate
python main.py
```
Open cron settings:
```
crontab -e
```
Add a cron job entry:
```
# Daily run at 12 PM.
0 12 * * * /home/< user-name >/< dir-name >/krisha.kz/cron.sh
```

# Search Parameters

- `city` - Search city from 0 to 20;
- `has_photo` - Listing has photos;
- `furniture` - Apartment has furniture;
- `rooms` - Number of rooms from 1 to 5;
- `price_from` - Minimum price;
- `price_to` - Maximum price;
- `owner` - Listing posted by the owner;

### City Values

- 0 - All of Kazakhstan.
- 1 - Almaty.
- 2 - Astana.
- 3 - Shymkent.
- 4 - Abai Region.
- 5 - Akmola Region.
- 6 - Aktobe Region.
- 7 - Almaty Region.
- 8 - Atyrau Region.
- 9 - East Kazakhstan Region.
- 10 - Zhambyl Region.
- 11 - Zhetysu Region.
- 12 - West Kazakhstan Region.
- 13 - Karaganda Region.
- 14 - Kostanay Region.
- 15 - Kyzylorda Region.
- 16 - Mangystau Region.
- 17 - Pavlodar Region.
- 18 - North Kazakhstan Region.
- 19 - Turkestan Region.
- 20 - Ulytau Region.

### Examples of Search Parameter Specification:
1. Find one-room apartments in Almaty.
Listings with photos.
Apartments with furniture.
Price from 100000 to 300000.
Listings from owners.
```json
{
  "city": 1,
  "has_photo": true,
  "furniture": true,
  "rooms": [1],
  "price_from": 100000,
  "price_to": 300000,
  "owner": true
}
```

2. Find two-room and three-room apartments in Astana.
Listings with photos.
Apartments without furniture.
Price up to 400000.
Listings from owners.
```json
{
  "city": 2,
  "has_photo": true,
  "rooms": [2, 3],
  "price_to": 400000,
  "owner": true
}
```

3. Find apartments with any number of rooms in Kazakhstan.
Listings without photos.
Apartments without furniture.
Price from 200000.
Listings from owners, agencies, and private realtors.
```json
{
  "price_from": 200000
}
```

Returns the same result as example No. 3.
```json
{
  "city": 0,
  "has_photo": false,
  "furniture": false,
  "rooms": [0],
  "price_from": 200000,
  "price_to": null,
  "owner": false
}
```
