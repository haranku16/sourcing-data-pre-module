# sourcing-data-pre-module
Pre-module assignment for sourcing data for analytics.

This repository provides a CLI utility for describing CSVs using Pandas.

## Requirements

### Install Python 3

https://www.python.org/downloads/

### Setup Python virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

For a more in-depth guide, click [HERE](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

### Install requirements

```
python3 -m pip install -r requirements.txt
```

## Usage

```
python3 src/describe.py [path/to/your/csv/file]
```

For example:
```
python3 src/describe.py test_data/films.csv
```

Example output:

```
              year  imdb_rating
count     3.000000     3.000000
mean   2008.333333     8.533333
std       3.511885     0.416333
min    2005.000000     8.200000
25%    2006.500000     8.300000
50%    2008.000000     8.400000
75%    2010.000000     8.700000
max    2012.000000     9.000000
```
