from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("your_mongodb_connection_string")
db = client.your_database_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_exs', methods=['GET'])
def get_exs():
    word = request.args.get('word_give')
    examples = db.examples.find({"word": word}, {"_id": 0})
    return jsonify({'result': 'success', 'examples': list(examples)})

@app.route('/api/save_ex', methods=['POST'])
def save_ex():
    word = request.json['word_give']
    example = request.json['example']
    db.examples.insert_one({"word": word, "example": example})
    return jsonify({'result': 'success'})

@app.route('/api/delete_ex', methods=['POST'])
def delete_ex():
    word = request.json['word']
    id = request.json['id']
    db.examples.delete_one({"word": word, "example_id": id})
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
