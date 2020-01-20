from flask import Flask, jsonify, request
from db import Database
app = Flask(__name__)

database = Database("mongodb+srv://Coner:cdtst112617@league-wxmis.mongodb.net/test?retryWrites=true&w=majority", "League", "Champions")


@app.route('/')
def index():
    return jsonify({'message' : 'League API'})

@app.route('/champ', methods=['GET'])
def returnALL():
    return database.get_all_champs()

@app.route('/champ/<string:name>', methods=['GET'])
def returnone(name):
    return database.get_one_champ(name)

if __name__ == '__main__':
    app.run(debug=True)