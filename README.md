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

## Requirement
* Python 3.5.3

  Windows and Mac: Install it from python.org: https://www.python.org/downloads/
  Mac (with Homebrew): In the terminal, run brew install python3
  Debian/Ubuntu/Mint: In the terminal, run sudo apt-get install python3
  Open a terminal and check whether you have Python installed:
  Checking Python versions with the --version option.
  Checking Python versions with the --version option.
  Depending on your system, the Python 3 command may be called python or python3.

* psycopg2

  You can install the pycodestyle tool to test this, with pip install pycodestyle or pip3 install pycodestyle (Python 3).

* Postgresql 9.6

  * Install VirtualBox
    VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

  * Install Vagrant
    Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

  * Load Database
    To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
    Here's what this command does:

    psql — the PostgreSQL command line program
    -d news — connect to the database named news which has been set up for you
    -f newsdata.sql — run the SQL statements in the file newsdata.sql

    Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.


##  How to Execute codes

* connect to the database
```sql
psql -d news
```
* to see an output on terminal
```sql
python LogsAnalysis.py or python3 LogsAnalysis.py
```
