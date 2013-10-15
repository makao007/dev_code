#coding:utf-8

import feedparser
import sqlite3
import hashlib
from sys import argv
import os
import urllib2
import datetime
import web_extract_content
import socket

socket.setdefaulttimeout(10)

_db = "MySQL"
#_db = "sqlite"

def md5 (s):
    return hashlib.md5(str(s)).hexdigest() 

def fetch (url):
    timeout_second = 10
    try:
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.69 Safari/537.36')
        response = urllib2.urlopen(request, timeout=timeout_second)
        if response.code == 200:
            return response.read()
        else:
            return ''
    except:
        return ''


def rss_fetch (url):
    d = feedparser.parse(url)
    d.feed.link = url
    return d

def rss_save (d, exists_article=[]):
    rss_articles = []
    for entry in d.entries:
        link_md5 = md5(entry.get("link"))
        rss_article = [entry.get("title"), entry.get("link"), entry.get("description"), entry.get("category"), entry.get("published"), entry.get("guid"), link_md5 ]

        if link_md5 not in exists_article:
            rss_articles.append (rss_article)

    try:
        print '%3d of %3d save to DB;  title: %s;  url: %s' % (len(rss_articles),len(d.entries),d.feed.title, d.feed.link)
    except:
        print 'error in %s ' % d.feed.link
    return rss_articles

def content_save (content, link, md5_link):
    sql = "insert into %s values (?,?,?,?)" % db_table_rss_content
    cursor.execute(sql,[md5_link,link,datetime.datetime.now(), content])
    conn.commit()

        
def db_conn():
    global conn, cursor, db_table_rss, db_table_rss_content
    db_name = 'rss'
    db_table_rss = 'rss_article'
    db_table_rss_content = 'rss_content'
    if _db == "MySQL":
        import MySQLdb
        conn = MySQLdb.connect(db="rss",user="app_user",passwd="app_user")
    else:
        conn = sqlite3.connect(db_name)
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute ('create table if not exists %s (title text, link text,description text, category text, publish date,guid text, link_md5 text)' % db_table_rss)
    
    cursor.execute ('create table if not exists %s (link_md5 text, link text, download_time datetime, content text) ' % db_table_rss_content )

def db_rss_save (data):
    sql = "insert into %s values (?,?,?,?,?,?,?)" % db_table_rss
    cursor.executemany (sql,data)
    conn.commit()

def db_rss_load_guid_md5 ():
    sql = "select link_md5 from %s" % db_table_rss
    return [x[0] for x in cursor.execute (sql)]
    
def db_rss_load_link ():
    sql = "select link_md5, link from %s" % db_table_rss
    return [x for x in cursor.execute(sql)]

def db_rss_load_url_content():
    sql = "select link_md5 from %s" % db_table_rss_content
    return [x[0] for x in cursor.execute(sql)]


def db_close():
    cursor.close()
    conn.close()

def feed_urls(filename):
    lines = file(filename).readlines()
    urls = []
    for line in lines:
        line = line.strip()
        if os.path.isdir(line):
            files = os.listdir (line)
            for sfile in files:
                urls.extend (file(os.path.join(line,sfile)).readlines())
        elif os.path.isfile (line):
            urls.extend (file(line).readlines())
    return urls

def start_craw_rss (feed_filename):
    db_conn()
    for url in feed_urls(feed_filename):
        db_rss_save(rss_save(rss_fetch(url.strip()), db_rss_load_guid_md5()))
    db_close()


def start_craw_rss_content ():
    db_conn()
    links_rss = db_rss_load_link()
    links_down = db_rss_load_url_content()

    for link in links_rss:
        if link[0] not in links_down:
            print link[1]
            #content = web_extract_content.extract_content(link[1])
            content = web_extract_content.fetch(link[1])
            if content:
                content_save (content, link[1], link[0])
            else:
                print 'error download : %s ' % link[1]
        else:
            print 'url exists'
    db_close()

if __name__ == "__main__":
    start_craw_rss_content()
    if len(argv)<2:
        start_craw_rss ('feeds.txt')
    else:
        start_craw_rss (argv[1])

