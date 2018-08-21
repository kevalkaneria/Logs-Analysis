#!/usr/bin/env python3
import psycopg2


def run_query(query):
    """connect to an existing database"""
    try:
        db = psycopg2.connect("dbname=news")
    except:
        print ("Unable to connect to the database")
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


# Question-1 : he most popular three articles of all time?
def get_popular_articles():
    query = """
        select articles.title,count(*) as views
        from articles
        join log
        on log.path
        like  concat('/article/%',articles.slug)
        group by articles.title
        order by views desc
        limit 3;
    """         
    # To Run query
    results = run_query(query)

    # To Print records
    print('The most popular three articles of all time:')
    count = 1
    for i in results:
        number = '(' + str(count) + ')'
        title = '"' + i[0] + '"'
        views = str(i[1]) + " " + "views"
        print(number + title + " " + "-" + " " + views)
        count += 1 


# Question-2 : Who are the most popular article authors of all time?
def get_popular_article_author():

    query = """
        select authors.name, count(*) as views
        from authors
        join articles
        on authors.id = articles.author
        join log
        on log.path
        like concat('/article/%', articles.slug)
        group by authors.name
        order by views desc;
    """

    # To Run query
    results = run_query(query)

    # To Print records
    print('The most popular article authors of all time:')
    count = 1
    for i in results:
        number = '(' + str(count) + ')'
        author = i[0]
        views = str(i[1]) + " " + "views"
        print(number + author + " " + "-" + " " + views)
        count += 1


# Question-3 : On which days did more than 1% of requests lead to errors?
def get_days_lead_errors():    
    query = """
        select errors.day, (100.0 * errors.abc / total.views) as percentage
        from
        (select time::date as day, COUNT(*) as abc 
        from log where status = '404 NOT FOUND' group by day) as errors
        join
        (select time::date as day, COUNT(*) as views 
        from log  group by day) as total
        on errors.day = total.day
        where (100.0 * errors.abc / total.views) > 1
        order by percentage desc;
    """

    # To Run query
    results = run_query(query)

    # To Print records
    print('The days did more than 1% of requests lead to errors:')
    count = 1
    for i in results:
        day = i[0].strftime('%B %d,%Y')
        errors = str(round(i[1], 2)) + " % " + "errors"
        print(day + " " + "-" + " " + errors)
        count += 1                 
get_popular_articles()
get_popular_article_author()
get_days_lead_errors()


