from flask import Flask, request
from scrapping import scrap

import json

app = Flask(__name__)

@app.route('/bulas/<remedy>', methods=['GET'])
def hello(remedy):
  result = scrap(remedy)
  formatted_result = result.replace('\n', '')
  js = json.dumps(formatted_result, ensure_ascii=False)

  return js

if __name__ == '__main__':
  app.run(debug=True)