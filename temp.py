from flask import Flask, request
import pymysql
import json
import os

app = Flask(__name__)

@app.route("/")
def main():
    return "<a href='http://testdb.paas-ta.co.kr/health_all'>/health_all</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/health?ID=12'>/health?ID=12</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/bokjiro_all'>/bokjiro_all</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/bokjiro?ID=12'>/bokjiro?ID=</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/toyouth_all'>/toyouth_all</>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/toyouth?ID=12'>/toyouth?ID=</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/nationalcost_all'>/nationalcost_all</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/nationalcost?ID=12'>/nationalcost?ID=</h2>\
            "

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
