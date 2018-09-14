import csv
import pymysql
import json
import os

#paas-ta에 있는 'VCAP_SERVICES에서 DB 접속 정보를 받아와 pymysql로 접속한다'

if 'VCAP_SERVICES' in os.environ:
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])

    if 'Mysql-DB' in vcap_services:
        mysql_srv = vcap_services['Mysql-DB'][0]
        mysql_cred = mysql_srv['credentials']
        print(mysql_cred['hostname'], mysql_cred['password'], mysql_cred['port'], type(mysql_cred['port']), mysql_cred['name'])
        mydb = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')

cur = mydb.cursor()
tablename = "nationalcost"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
mydb.commit()

f = open('nationalcost.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "bokjiro"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
mydb.commit()

f = open('bokjiro.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "toyouth"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
mydb.commit()

f = open('toyouth.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "health"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
mydb.commit()

f = open('health.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "cityhall"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
mydb.commit()

f = open('cityhall.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "public"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
mydb.commit()

f = open('public.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()






mydb.close()
