from flask import Flask, request
import pymysql
import json
import os

#paas-ta DB 접속정보 받아와서 접속
if 'VCAP_SERVICES' in os.environ:
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])

    if 'Mysql-DB' in vcap_services:
        mysql_srv = vcap_services['Mysql-DB'][0]
        mysql_cred = mysql_srv['credentials']
        conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')

app = Flask(__name__)
#api = Api(app, version='1.0', title="복지로 부산 DATA", description="복지로 부산 DATA => bokjiro_busan 복지로 메인 DATA => bokjiro_main")

#db 모든 데이터 json으로 출력
@app.route("/")
def main():
    return "<h2>/health_all</h2>\
            <p>\
            <h2>/health?ID=</h2>\
            <p>\
            <h2>/health?타이틀=</h2>\
            <p>\
            <h2>/bokjiro_all</h2>\
            <p>\
            <h2>/bokjiro?ID=</h2>\
            <p>\
            <h2>/bokjiro?타이틀=</h2>\
            "

#DB데이터 모두 출력
@app.route("/health_all", methods=["GET"])
def health_all():
    curs = conn.cursor()
    curs.execute("select * from health")
    result = []

    for row in curs:
        temp_dic = {
            'ID' : row[0],
            'TITLE' : row[1],
            'CONTENTS' : row[2],
            'DATE' : row[3],
            'TARGET' : row[4],
            'LINK' : row[5],
            'REGION' : row[6],
            'ASK' : row[7],
            'CONTACT' : row[8],
            'ORIGIN' : row[9],
            'CATEGORY' : row[10]
        }
        result.append(temp_dic)

    temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
    return temp

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/health",methods=["GET"])
def health():
    ID = request.args.get('ID')
    TITLE = request.args.get('타이틀')
    curs = conn.cursor()

    if ID is not None :
        curs.execute("select * from health where ID = " + ID)
    elif TITLE is not None :
        curs.execute("select * from health where 타이틀 = " + TITLE)

    result = []
    for row in curs:
        temp_dic = {
            'ID' : row[0],
            'TITLE' : row[1],
            'CONTENTS' : row[2],
            'DATE' : row[3],
            'TARGET' : row[4],
            'LINK' : row[5],
            'REGION' : row[6],
            'ASK' : row[7],
            'CONTACT' : row[8],
            'ORIGIN' : row[9],
            'CATEGORY' : row[10]
        }
        result.append(temp_dic)

    temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
    return temp

#DB데이터 모두 출력
@app.route("/bokjiro_all", methods=["GET"])
def bokjiro_all():
    curs = conn.cursor()
    curs.execute("select * from bokjiro")
    result = []

    for row in curs:
        temp_dic = {
            'ID' : row[0],
            'TITLE' : row[1],
            'CONTENTS' : row[2],
            'DATE' : row[3],
            'TARGET' : row[4],
            'LINK' : row[5],
            'REGION' : row[6],
            'ASK' : row[7],
            'CONTACT' : row[8],
            'ORIGIN' : row[9],
            'CATEGORY' : row[10]
        }
        result.append(temp_dic)

    temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
    return temp

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/bokjiro",methods=["GET"])
def bokjiro():
    ID = request.args.get('ID')
    TITLE = request.args.get('타이틀')
    curs = conn.cursor()

    if ID is not None :
        curs.execute("select * from bokjiro where ID = " + ID)
    elif TITLE is not None :
        curs.execute("select * from bokjiro where 타이틀 = " + TITLE)

    result = []
    for row in curs:
        temp_dic = {
            'ID' : row[0],
            'TITLE' : row[1],
            'CONTENTS' : row[2],
            'DATE' : row[3],
            'TARGET' : row[4],
            'LINK' : row[5],
            'REGION' : row[6],
            'ASK' : row[7],
            'CONTACT' : row[8],
            'ORIGIN' : row[9],
            'CATEGORY' : row[10]
        }
        result.append(temp_dic)

    temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
    return temp

#DB데이터 모두 출력
@app.route("/toyouth_all", methods=["GET"])
def toyouth_all():
    curs = conn.cursor()
    curs.execute("select * from toyouth")
    result = []

    for row in curs:
        temp_dic = {
            'ID' : row[0],
            'TITLE' : row[1],
            'CONTENTS' : row[2],
            'DATE' : row[3],
            'TARGET' : row[4],
            'LINK' : row[5],
            'REGION' : row[6],
            'ASK' : row[7],
            'CONTACT' : row[8],
            'ORIGIN' : row[9],
            'CATEGORY' : row[10]
        }
        result.append(temp_dic)

    temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
    return temp

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/toyouth",methods=["GET"])
def toyouth():
    ID = request.args.get('ID')
    TITLE = request.args.get('타이틀')
    curs = conn.cursor()

    if ID is not None :
        curs.execute("select * from toyouth where ID = " + ID)
    elif TITLE is not None :
        curs.execute("select * from toyouth where 타이틀 = " + TITLE)

    result = []
    for row in curs:
        temp_dic = {
            'ID' : row[0],
            'TITLE' : row[1],
            'CONTENTS' : row[2],
            'DATE' : row[3],
            'TARGET' : row[4],
            'LINK' : row[5],
            'REGION' : row[6],
            'ASK' : row[7],
            'CONTACT' : row[8],
            'ORIGIN' : row[9],
            'CATEGORY' : row[10]
        }
        result.append(temp_dic)

    temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
    return temp

#DB데이터 모두 출력
@app.route("/NationalCost_all", methods=["GET"])
def NationalCost_all():
    curs = conn.cursor()
    curs.execute("select * from NationalCost")
    result = []

    for row in curs:
        temp_dic = {
            'ID' : row[0],
            'TITLE' : row[1],
            'CONTENTS' : row[2],
            'DATE' : row[3],
            'TARGET' : row[4],
            'LINK' : row[5],
            'REGION' : row[6],
            'ASK' : row[7],
            'CONTACT' : row[8],
            'ORIGIN' : row[9],
            'CATEGORY' : row[10]
        }
        result.append(temp_dic)

    temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
    return temp

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/NationalCost",methods=["GET"])
def NationalCost():
    ID = request.args.get('ID')
    TITLE = request.args.get('타이틀')
    curs = conn.cursor()

    if ID is not None :
        curs.execute("select * from NationalCost where ID = " + ID)
    elif TITLE is not None :
        curs.execute("select * from NationalCost where 타이틀 = " + TITLE)

    result = []
    for row in curs:
        temp_dic = {
            'ID' : row[0],
            'TITLE' : row[1],
            'CONTENTS' : row[2],
            'DATE' : row[3],
            'TARGET' : row[4],
            'LINK' : row[5],
            'REGION' : row[6],
            'ASK' : row[7],
            'CONTACT' : row[8],
            'ORIGIN' : row[9],
            'CATEGORY' : row[10]
        }
        result.append(temp_dic)

    temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
    return temp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
