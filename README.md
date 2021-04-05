# CSV-converter
Converts a non-comma delimited csv file to comma delimited.

## Requirements
- python3


## Usage

By default the program will name the converted file `<filename>_cleaned.csv`, this can be changed with the `-o` argument.

### CSV-converter cli args

usage: csvconverter.py [-h] --csv CSV [--delim DELIM] [--out OUT]


required args:

  `--csv CSV, -c CSV : csv file to convert`

optional arguments:

  `-h, --help : show this help message and exit`

  `--delim DELIM, -d DELIM : Delimeter to convert from`

  `--out OUT, -o OUT : File output name`

  `--explicit_empty_fields, EEF, -e EEF : Explicitly print null in empty fields, default prints null in their place`


### Example

`$ csvconverter.py -c movies.csv`


## Extra information 

Hello World 


