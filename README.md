#LogAnalysis project

This Project is about to create a reporting tool in a Python program using the psycopg2 module to connect to the database.

##Questions
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors

## List of Installation

*  You can install the pycodestyle tool to test this, with pip install pycodestyle or pip3 install pycodestyle (Python 3).


## Requirement
* Python 3.5.3
* psycopg2
* Postgresql 9.6


##  How to Execute codes
* load the data onto the database
```sql
psql -d news -f newsdata.sql
```
* connect to the database
```sql
psql -d news
```
* to see an output on python2 or python3
```sql
python LogsAnalysis.py or python3 LogsAnalysis.py
```
