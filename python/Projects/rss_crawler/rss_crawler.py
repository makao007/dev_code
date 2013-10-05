#coding:utf-8

import feedparser
import sqlite3
import hashlib

def md5 (s):
    return hashlib.md5(str(s)).hexdigest() 

def rss_fetch (url):
    d = feedparser.parse(url)
    d.feed.link = url
    return d

def rss_save (d, exists_article=[]):
    rss_articles = []
    for entry in d.entries:
        guid_md5 = md5(entry.guid)
        rss_article = [entry.title, entry.link, entry.description, entry.category, entry.published, entry.guid, guid_md5 ]

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


def start_craw_rss ():
    urls = ['http://cn.reuters.feedsportal.com/chinaNews','http://cn.reuters.com/rssFeed/CNAnalysesNews/','http://cn.reuters.com/rssFeed/CNIntlBizNews/',\
            'http://cn.reuters.com/rssFeed/CNTopGenNews/','http://cn.reuters.com/rssFeed/CNMgtNews/','http://cn.reuters.com/rssFeed/commoditiesNews/',\
            'http://cn.reuters.com/rssFeed/cnBizNews/','http://cn.reuters.com/rssFeed/cnInvNews/','http://cn.reuters.com/rssFeed/companyNews/', \
            'http://cn.reuters.com/rssFeed/cnMktNews/','http://cn.reuters.com/rssFeed/stocksNews/','http://cn.reuters.com/rssFeed/fundsNews/' , \
            'http://cn.reuters.com/rssFeed/bondsNews/','http://cn.reuters.com/rssFeed/currenciesNews/','http://cn.reuters.com/rssFeed/industryNews/', \
            'http://cn.reuters.com/rssFeed/macroeconomicsNews' ]
    db_conn()
    for url in urls:
        db_rss_save(rss_save(rss_fetch(url), db_rss_load_guid_md5()))
    db_close()

start_craw_rss ()

