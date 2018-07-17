
                          #!/usr/bin/env python
from __future__ import print_function
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin

import logging
import pymysql
import os

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*","methods":"POST,DELETE,PUT,GET,OPTIONS"}})

def creatConnection():
    # Read MySQL Environment Parameters
    connectString = os.environ.get('MYSQLCS_CONNECT_STRING', 'localhost:3306/myDB') 
    hostname = connectString[:connectString.index(":")]
    database = connectString[connectString.index("/")+1:]
    conn = pymysql.connect(host=hostname, 
	                       port=int(os.environ.get('MYSQLCS_MYSQL_PORT', '3306')), 
						   user=os.environ.get('MYSQLCS_USER_NAME', 'root'), 
						   passwd=os.environ.get('MYSQLCS_USER_PASSWORD', ''), 
						   db=database,
						   cursorclass=pymysql.cursors.DictCursor)
    return conn;

@app.route('/')
def index():
    return 'The application is running!'
	
@app.route('/pokemon/setupdb')
def setupDB():
    conn = creatConnection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE POKEMON (
				  NAME VARCHAR(255),
                  LEVEL VARCHAR(255),
				  TYPE1 VARCHAR(255),
				  TYPE2 VARCHAR(255),
				  ABILITY VARCHAR(255),
				  MOVE VARCHAR(255),
				  PRIMARY KEY (NAME)
				  ); ''') 
    conn.commit()
    cur.close()
    conn.close()
    return 'The POKEMON tables was created succesfully'
	
@app.route('/pokemon')
def pokemon():
    conn = creatConnection()
    cur = conn.cursor()
    cur.execute('''SELECT NAME, LEVEL, TYPE1, TYPE2, ABILITY, MOVE FROM POKEMON''')
    results = cur.fetchall()	
    cur.close()
    conn.close()
    return jsonify( results)	

@app.route('/pokemon/<str:pokemon_name>', methods=['GET'])
def get_pokemon(pokemon_name):
    conn = creatConnection()
    cur = conn.cursor()
    cur.execute('''SELECT NAME, LEVEL, TYPE1, TYPE2, ABILITY, MOVE FROM POKEMON WHERE NAME = %s'''%(pokemon_name))
    rv = cur.fetchone()    
    if rv is None:
        abort(404)
    cur.close()
    conn.close()
    return jsonify( rv)	

@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    conn = creatConnection()
    cur = conn.cursor()
    try:
        cur.execute('''INSERT INTO POKEMON (NAME, LEVEL, TYPE1, TYPE2, ABILITY, MOVE) 
	                VALUES('%s','%s','%s','%s','%s','%s') '''%(request.json['name'],request.json['level'],
				    request.json['type1'],request.json['type2'],request.json['ability'],request.json['move']))    
        conn.commit()
        message = {'status': 'New pokemon record is created succesfully'}
        cur.close()	 
    except Exception as e:
        logging.error('DB exception: %s' % e)
        message = {'status': 'The creation of the new pokemon failed.'}
    conn.close()
    return jsonify(message)

@app.route('/pokemon/<str:employee_id>', methods=['PUT'])
def update_pokemon(pokemon_name):
    conn = creatConnection()
    cur = conn.cursor()
    try:
        cur.execute('''UPDATE POKEMON SET NAME='%s', LEVEL='%s', TYPE1='%s', TYPE1='%s', ABILITY='%s', MOVE='%s'
	               WHERE NAME=%s '''%(request.json['name'],request.json['level'],
				   request.json['type1'],request.json['type2'],request.json['ability'],request.json['move'],pokemon_name))    
        conn.commit()
        message = {'status': 'The pokemon record is updated succesfully'}
        cur.close()	 
    except Exception as e:
        logging.error('DB exception: %s' % e)	
        message = {'status': 'Pokemon update failed.'}
    conn.close()
    return jsonify(message)

@app.route('/pokemon/<str:pokemon_name>', methods=['DELETE'])
def delete_pokemon(pokemon_name):
    conn = creatConnection()
    cur = conn.cursor()
    try:
        cur.execute('''DELETE FROM POKEMON WHERE NAME=%s '''%(pokemon_name))    
        message = {'status': 'The pokemon record is deleted succesfully'}
        conn.commit()
        cur.close()	 
    except Exception as e:
        logging.error('DB exception: %s' % e)	
        message = {'status': 'Pokemon delete failed.'}
    conn.close()
    return jsonify(message)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.environ.get('PORT', '8080'))
