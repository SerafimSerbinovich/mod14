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
    return create_json_for_years(data)


if __name__ == '__main__':
    app.run()
