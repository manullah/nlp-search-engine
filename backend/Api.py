from flask import Flask
from flask import request
import json
import random

from Trie import Trie
from Synonym import Synonym

def load_queries_from_file(path, max_size=10**6):
    data = []
    i = 0
    # Read the first max_size rows
    with open(path, 'r', encoding="utf8") as f:
        for line in f:
            data.append(line)
            i+=1
            if i== max_size:
                break;
    # Generate random frequencies
    queries = {i: random.randint(1, 1000) for i in data}
    return queries


app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers['Access-Control-Allow-Methods'] = '*'
  response.headers['Access-Control-Allow-Origin'] = '*'
  response.headers['Vary'] = 'Origin'
  return response

@app.route('/autocomplete', methods=['GET'])
def fetchAutocomplete():
    query = request.args.get('query')
    res = t.search(query)
    return res

@app.route('/synonym', methods=['GET'])
def fetchSynonyms():
    query = request.args.get('query')
    res = synonym.getSynonyms(query)
    return res


max_size = 10**6

path = "dataset/sample.txt"

t = Trie()
queries = load_queries_from_file(path)
t.build_tree(queries)

synonym = Synonym()

app.run(debug=False, host="127.0.0.1", port=3000)