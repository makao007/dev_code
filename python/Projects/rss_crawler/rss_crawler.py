#coding:utf-8

import feedparser
import sqlite3
import hashlib
from sys import argv

def md5 (s):
    return hashlib.md5(str(s)).hexdigest() 

def rss_fetch (url):
    d = feedparser.parse(url)
    d.feed.link = url
    return d

def rss_save (d, exists_article=[]):
    rss_articles = []
    for entry in d.entries:
        guid_md5 = md5(entry.get("guid"))
        rss_article = [entry.get("title"), entry.get("link"), entry.get("description"), entry.get("category"), entry.get("published"), entry.get("guid"), guid_md5 ]

        if guid_md5 not in exists_article:
            rss_articles.append (rss_article)

    try:
        print '%3d of %3d save to DB;  title: %s;  url: %s' % (len(rss_articles),len(d.entries),d.feed.title, d.feed.link)
    except:
        print 'error in %s ' % d.feed.link
    return rss_articles
        
def db_conn():
    global db_table_rss,conn,cursor
    db_name = 'rss'
    db_table_rss = 'rss_article'
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute ('create table if not exists %s (title text, link text,description text, category text, publish date,guid text, guid_md5 text)' % db_table_rss)

def db_rss_save (data):
    sql = "insert into %s values (?,?,?,?,?,?,?)" % db_table_rss
    cursor.executemany (sql,data)
    conn.commit()

def db_rss_load_guid_md5 ():
    sql = "select guid_md5 from %s" % db_table_rss
    return [x[0] for x in cursor.execute (sql)]
    

def db_close():
    cursor.close()
    conn.close()

def feed_urls(filename):
    return file(filename).readlines()

def start_craw_rss (feed_filename):
    db_conn()
    for url in feed_urls(feed_filename):
        db_rss_save(rss_save(rss_fetch(url), db_rss_load_guid_md5()))
    db_close()


if __name__ == "__main__":
    if len(argv)<2:
        start_craw_rss ('feeds.txt')
    else:
        start_craw_rss (argv[1])

