from app import app, db, models
from flask import jsonify

available_regions = ['Nelson', 'Dunedin', 'Hamilton', 'Christchurch', 'Gisborne', 'Greymouth', 'Wanganui', 'Tekapo', 'Wellington', 'Turangi', 'Whangarei', 'Alexandra', 'Auckland', 'Rotorua', 'Havelock Nth']

@app.route('/region')
def return_available():
    return jsonify(available_regions)

@app.route('/region/<string:region>', methods=['GET'])
def get_region(region):
    if region in available_regions:
        query = models.Point.query.filter(models.Point.region == region)
        return jsonify([point.json() for point in query.all()])

    else:
        return jsonify([])

    