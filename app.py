from flask import Flask, request
import pymysql
import json
import os

#paas-ta DB 접속정보 받아와서 접속
if 'VCAP_SERVICES' in os.environ:
    print("do")
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])

    if 'Mysql-DB' in vcap_services:
        mysql_srv = vcap_services['Mysql-DB'][0]
        mysql_cred = mysql_srv['credentials']

app = Flask(__name__)
#api = Api(app, version='1.0', title="복지로 부산 DATA", description="복지로 부산 DATA => bokjiro_busan 복지로 메인 DATA => bokjiro_main")
lists = ['ID', 'TITLE', 'CONTENTS', 'DATE', 'TARGET', 'LINK', 'REGION', 'ASK', 'CONTACT', 'ORIGIN', 'CATEGORY']
#db 모든 데이터 json으로 출력
@app.route("/")
def main():
    return "<h2>/health_all</h2>\
            <p>\
            <h2>/health?ID=</h2>\
            <p>\
            <h2>/health?TITLE=</h2>\
            <p>\
            <h2>/bokjiro_all</h2>\
            <p>\
            <h2>/bokjiro?ID=</h2>\
            <p>\
            <h2>/bokjiro?TITLE=</h2>\
            <p>\
            <h2>/toyouth_all</h2>\
            <p>\
            <h2>/toyouth?ID=</h2>\
            <p>\
            <h2>/toyouth?TITLE=</h2>\
            <p>\
            <h2>/nationalcost_all</h2>\
            <p>\
            <h2>/nationalcost?ID=</h2>\
            <p>\
            <h2>/nationalcost?TITLE=</h2>\
            "

#DB데이터 모두 출력
@app.route("/health_all", methods=["GET"])
def health_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
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
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            if curs:
                curs.close()
            if conn:
                conn.close()
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/health",methods=["GET"])
def health():
    i=0
    while i != 10:
        try:
            AC = []
            AC[0] = request.args.get('ID')
            AC[1] = request.args.get('TITLE')
            AC[2] = request.args.get('CONTENTS')
            AC[3] = request.args.get('DATE')
            AC[4] = request.args.get('TARGET')
            AC[5] = request.args.get('LINK')
            AC[6] = request.args.get('REGION')
            AC[7] = request.args.get('ASK')
            AC[8] = request.args.get('ORIGIN')
            AC[9] = request.args.get('CATEGORY')

            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()
            for i in range(0,10):
                if AC[i] is not None:
                    curs.execute("select * from  health where " + lists[i] + " = ")

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
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            if curs:
                curs.close()
            if conn:
                conn.close()
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB데이터 모두 출력
@app.route("/bokjiro_all", methods=["GET"])
def bokjiro_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
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
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            if curs:
                curs.close()
            if conn:
                conn.close()
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/bokjiro",methods=["GET"])
def bokjiro():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from bokjiro where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from bokjiro where TITLE = " + TITLE)

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
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            if curs:
                curs.close()
            if conn:
                conn.close()
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB데이터 모두 출력
@app.route("/toyouth_all", methods=["GET"])
def toyouth_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
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
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            if curs:
                curs.close()
            if conn:
                conn.close()
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/toyouth",methods=["GET"])
def toyouth():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from toyouth where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from toyouth where TITLE = " + TITLE)

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
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            if curs:
                curs.close()
            if conn:
                conn.close()
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB데이터 모두 출력
@app.route("/nationalcost_all", methods=["GET"])
def nationalcost_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()
            curs.execute("select * from nationalcost")
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
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            if curs:
                curs.close()
            if conn:
                conn.close()
            print("error is ==> ", e)
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/nationalcost",methods=["GET"])
def nationalcost():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from Nationalcost where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from Nationalcost where TITLE = " + TITLE)

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
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            if curs:
                curs.close()
            if conn:
                conn.close()
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

@app.route('/webhook', methods=['POST',])
def create_book():
    try:
        print("do")
        conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
    except Exception as e:
        if conn:
            conn.close()
        print(e)

    cur = conn.cursor()
    req = request.data
    inputData = json.loads(req)['result']
    output = ""
    param = inputData['parameters']
    context = inputData['contexts']

    serviceName = param['any']

    query = "select * from health where TITLE like '%" + serviceName + "%'"

    cur.execute(query)

    # for x in cur:
    #     print(x)

    if param['When']:
        for x in cur:
            txt = str(x[1]) + "의 신청기간은 " + str(x[3]) + "입니다."
            output += txt
            break
    elif param['Contact']:
        for x in cur:
            txt = str(x[1]) + "관련 연락처는 " + str(x[8]) + "입니다."
            output += txt
            break
    elif param['How']:
        for x in cur:
            txt = str(x[1]) + "관련 신청 방법은 " + str(x[5]) + "에서 확인 바랍니다."
            output += txt
            break
    elif param['Where']:
        for x in cur:
            txt = str(x[1]) + "의 위치(주소) " + str(x[6]) + "입니다."
            output += txt
            break
    elif param['Who']:
        for x in cur:
            txt = str(x[1]) + "의 적용 대상은 " + str(x[4]) + "입니다"
            output += txt
            break
    else :
        output = "error"

    # print("param : {}".format(param))
    # print("context : {}".format(context))

    print(output)
    res_msg = "{'speech': '%s', 'displayText': '%s'}" % (output, output)
    # res_msg = "{'fulfillmentMessages': [{'card': {'title': 'card title', 'subtitle': 'card text'}}]}"
    print(res_msg)
    cur.close()
    conn.close()

    return res_msg



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
