# -*- coding: utf-8 -*-

from flask import Flask
import pandas as pd 

from sqlalchemy import create_engine

engine = create_engine("postgresql://izqesmsjoczkzz:dded6e1737ec332ef2bb0a898d23101b70406d9e25cb44fd472079b9a2aab111@ec2-54-225-234-165.compute-1.amazonaws.com:5432/dbqh4fnj6la4kq", echo = False)
engine.connect()
## DB 연결 Local
def db_create():
    #로컬 
    #engine = create_engine("postgresql://postgres:12232305@localhost:5432/postgres",echo=False)
    #postgresql://username:password@localhost:5432/Maintenance database
    #Heroku
    
    engine.execute("""
        CREATE TABLE IF NOT EXISTS dreamspon(
            name varchar(90) NOT NULL,
            advantage varchar(10) NOT NULL,
            who varchar(40) NOT NULL,
            age varchar(15) NOT NULL,
            where1 VARCHAR(30) NOT NULL,
            qualification VARCHAR(30) NOT NULL,
            url VARCHAR(70) NOT NULL
        );"""
    )
    data = pd.read_csv('data/dreamspon.csv')
    print(data)
    data.to_sql(name='dreamspon', con=engine, schema = 'public', if_exists='replace', index=False)


def db_select():
    result_set = engine.execute("SELECT name FROM dreamspon")
    for r in result_set:
        print(r)

app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return "Hello World!"


if __name__ == "__main__":
    # db_create()
    db_select()
    # app.run()