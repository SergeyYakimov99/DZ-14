from flask import Flask, jsonify
from utils import *

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<title>')
def get_by_title_movie(title):
    return get_search_by_title(title)


@app.route('/movie/<int:s1>/to/<int:s2>')
def get_by_years(s1, s2):
    return jsonify(search_by_year(s1, s2))


@app.route('/rating/<category>')
def get_by_rating(category):
    return jsonify(search_by_rating(category))


@app.route('/genry/<genry>')
def get_by_genry(genry):
    return jsonify(search_by_genry(genry))


if __name__ == '__main__':
    app.run(debug=True)
