from app import db, models
import json 

with open('dump.large.new.json') as r:
    data = json.loads(r.read())

    for point in data:
        # print('site_desc', type(point['site_desc']), point['site_desc'])
        # print('region', type(point['region']), point['region'])
        # print('wq_temperature', type(point['wq_temperature']), point['wq_temperature'])
        # print('wq_dissolved_oxygen_percent', type(point['wq_dissolved_oxygen_percent']), point['wq_dissolved_oxygen_percent'])
        # print('wq_dissolved_oxygen', type(point['wq_dissolved_oxygen']), point['wq_dissolved_oxygen'])
        # print('wq_instantaneous_discharge', type(point['wq_instantaneous_discharge']), point['wq_instantaneous_discharge'])
        # print('wq_turbidity_ntu', type(point['wq_turbidity_ntu']), point['wq_turbidity_ntu'])
        # print('wq_ph', type(point['wq_ph']), point['wq_ph'])
        # print('wq_ammoniacal_nitrogen', type(point['wq_ammoniacal_nitrogen']), point['wq_ammoniacal_nitrogen'])
        # print('wq_nitrate_nitrite', type(point['wq_nitrate_nitrite']), point['wq_nitrate_nitrite'])
        # print('wq_total_nitrogen', type(point['wq_total_nitrogen']), point['wq_total_nitrogen'])
        # print('wq_dissolved_phosphorus', type(point['wq_dissolved_phosphorus']), point['wq_dissolved_phosphorus'])
        # print('wq_calcium', type(point['wq_calcium']), point['wq_calcium'])
        # print('wq_magnesium', type(point['wq_magnesium']), point['wq_magnesium'])
        # print('wq_sodium', type(point['wq_sodium']), point['wq_sodium'])
        # print('wq_potassium', type(point['wq_potassium']), point['wq_potassium'])
        # print('wq_total_alkalinity', type(point['wq_total_alkalinity']), point['wq_total_alkalinity'])
        # print('wq_chloride', type(point['wq_chloride']), point['wq_chloride'])
        # print('wq_sulphate', type(point['wq_sulphate']), point['wq_sulphate'])
        # print('longitude', type(point['longitude']), point['longitude'])
        # print('latitude', type(point['latitude']), point['latitude'])

        new_db_record = models.Point(point['site_desc'],
            point['region'],
            point['wq_temperature'],
            point['wq_dissolved_oxygen_percent'],
            point['wq_dissolved_oxygen'],
            point['wq_instantaneous_discharge'],
            point['wq_turbidity_ntu'],
            point['wq_ph'],
            point['wq_ammoniacal_nitrogen'],
            point['wq_nitrate_nitrite'],
            point['wq_total_nitrogen'],
            point['wq_dissolved_phosphorus'],
            point['wq_calcium'],
            point['wq_magnesium'],
            point['wq_sodium'],
            point['wq_potassium'],
            point['wq_total_alkalinity'],
            point['wq_chloride'],
            point['wq_sulphate'],
            point['longitude'],
            point['latitude'])
        
        db.session.add(new_db_record)
        db.session.commit()