from flask import Flask,jsonify
from DAOdb import *
from utils import *

app = Flask('__name__')


# create view for title searching
@app.route('/movie/<title>/')
def search_by_name_page(title):
    data = search_for_query(title)
    return jsonify(create_a_json_dict(data))


# create view for year filter
@app.route('/movie/<int:year_1>/to/<int:year_2>')
def search_by_years(year_1, year_2):
    data = search_for_release_year(year_1, year_2)
    return jsonify(create_json_for_years(data))


@app.route('/rating/children')
def search_for_children():
    data = search_for_rating_g()
    return jsonify(create_json_for_rating(data))


@app.route('/rating/family')
def search_for_family():
    data = search_for_rating_family()
    return jsonify(create_json_for_rating(data))


@app.route('/rating/adult')
def search_for_adult():
    data = search_for_rating_adult()
    return jsonify(create_json_for_rating(data))


if __name__ == '__main__':
    app.run()
