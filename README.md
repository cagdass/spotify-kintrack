# Spotify Kintrack

Modest Python program I use to keep track of the monetary transcations with my Spotify family, lest anyone rippeth anyone off. The pricing information is in Turkish Liras, but prices in other currencies can be fed with a simple modification.

## Before Usage

I use a simple text file with 4 semi-colon separated columns. It follows the following format:

| Name        | Start Date           | End Date  | Amount Paid |
| ------------- |:-------------:| :-----:| ----: |
| Baraa Orabi   | 24-10-2016 | N/A | 6|
| Sarjeel Yusuf     | 29-10-2016   |   22-12-2016 | 2.5 |

Looks like 

```
Name;Start Date;End Date;Amount Paid
Baraa Orabi;24-10-2016;N/A;6
Sarjeel Yusuf;29-10-2016;22-12-2016;2.5
```

Unless you want to modify the program, there are a few details:

* Dates are formatted dd-mm-yyyy.
* You can use any placeholder for End Date as long as it contains no more than 2 hyphens (-) *The date is extracted by splitting on the hyphen character*.
* I hardly think not explicitly stating the currency in the Amount Paid field will be a problem, but a modification to the program can be made on line 65, where the amount is parsed as a float.
* The file is called ```spotify.log```, which can be changed in the program on line 50, where the filename is given as a parameter with a default value.
* The price changes, date of the price change and the new price, are defined on line 6 as follows: 

```python
price_changes = [(datetime(2017,4,25), 21.0), (datetime(1977,1,1), 15.0)]
```

This can be modified for other currencies.

## Usage

```
git clone https://github.com/cagdass/spotify-family.git
cd spotify-family
python spotify.py # Make sure you have a log file that follows the format and named spotify.log, you can always modify the program regarding the file format and name.
```
