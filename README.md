Steps to build from scratch:

* tar -zxvf nhl_cities.tar.gz
* cd nhl_cities
* sudo -H pip install -r requirements.txt
* python geocode.py
* python distmatrix.py

This produces an output file 'nhl_distmatrix.csv' which is a comma
delimited file where each row is distance from city[row_n] to all
cities in row_n. The distance calculation is Haversine distance (great
arc on sphere).
