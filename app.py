from flask import Flask, jsonify, request
import sqlite3
import pandas as pd

app = Flask(__name__)

class config():
    API_PORT = 5000
    DEV_PORT = 5005

@app.route('/')
def isAlive():
    return "hello world"

@app.route('/flights/<int:fid>')
def flights(fid):
    conn = sqlite3.connect("example.db")
    q = "SELECT * FROM data WHERE `index` = ?"
    r = pd.read_sql(q, conn, params=[fid])
    return jsonify(r.to_dict(orient='records')[0])

@app.route('/flights')
def flight_list():
    conn = sqlite3.connect("example.db")
    q = "SELECT `index` FROM data"
    r = pd.read_sql(q, conn)
    ids = [str(row[0]) for row in r.values]
    # import pdb; pdb.set_trace()
    return str(list(map(int, ids)))

@app.route('/search')
def search():
    query = request.args.get('query')
    print(query)
    conn = sqlite3.connect("example.db")
    q = r"SELECT * FROM data WHERE UPPER(ORIGIN_DESC) LIKE '%' || UPPER(?) || '%' OR UPPER(DEST_DESC) LIKE '%' || UPPER(?) || '%'"
    r = pd.read_sql(q, conn, params=[query, query])
    # import pdb; pdb.set_trace()
    return jsonify(r.to_dict(orient='records'))

# == execution logic == #

def main(prod: ('production mode', 'flag', 'p')):
	""" about the program """
	if not prod:
		app.run(debug=True, host='0.0.0.0', port=config.DEV_PORT)
	else:
		from waitress import serve
		serve(app, listen=f'*:{config.API_PORT}')

if __name__=='__main__':
	import plac
	plac.call(main)