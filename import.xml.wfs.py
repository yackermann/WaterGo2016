import json
new_data = []

def parseFloat(item):

    try:
        return float(item)
    except:
        return 0

with open('dump.large.json') as r:
    data = json.loads(r.read())

    for item in data:
        fixed_item = {
            'region' : item['region'],
            'wq_temperature' : parseFloat(item['wq_temperature']),
            'wq_dissolved_oxygen_percent' : parseFloat(item['wq_dissolved_oxygen_percent']),
            'wq_dissolved_oxygen' : parseFloat(item['wq_dissolved_oxygen']),
            'wq_instantaneous_discharge' : parseFloat(item['wq_instantaneous_discharge']),
            'wq_turbidity_ntu' : parseFloat(item['wq_turbidity_ntu']),
            'wq_ph' : parseFloat(item['wq_ph']),
            'wq_ammoniacal_nitrogen' : parseFloat(item['wq_ammoniacal_nitrogen']),
            'wq_nitrate_nitrite' : parseFloat(item['wq_nitrate_nitrite']),
            'wq_total_nitrogen' : parseFloat(item['wq_total_nitrogen']),
            'wq_dissolved_phosphorus' : parseFloat(item['wq_dissolved_phosphorus']),
            'wq_calcium' : parseFloat(item['wq_calcium']),
            'wq_magnesium' : parseFloat(item['wq_magnesium']),
            'wq_sodium' : parseFloat(item['wq_sodium']),
            'wq_potassium' : parseFloat(item['wq_potassium']),
            'wq_total_alkalinity' : parseFloat(item['wq_total_alkalinity']),
            'wq_chloride' : parseFloat(item['wq_chloride']),
            'wq_sulphate' : parseFloat(item['wq_sulphate']),
            'longitude' : parseFloat(item['longitude']),
            'latitude' : parseFloat(item['latitude'])
        }

        if type(item['site_desc']) == dict:
            fixed_item['site_desc'] = item['site_desc']['#text']
        elif type(item['site_desc']) == str:
            fixed_item['site_desc'] = item['site_desc']
        else:
            print(item['site_desc'], type(item['site_desc']))
            raise

        new_data.append(fixed_item)

    with open('dump.large.new.json', 'w') as w:
        w.write(json.dumps(new_data))







# import json

# dump = []
# with open('file.json') as r:
#     data = r.read()
#     data = json.loads(data)

#     rootkey    = list(data.keys())[0]
#     rootkey_l2 = sorted(list(data[rootkey].keys()))[2]
#     list_data  = data[rootkey][rootkey_l2]
#     print(len(list_data))

#     for opitem in list_data:
#         item = opitem['{http://niwa.co.nz/ns/nemo}fchem_chemistry']
#         new_object = {
#             'site_desc' : item['{http://niwa.co.nz/ns/nemo}' + 'site_desc'],
#             'region' : item['{http://niwa.co.nz/ns/nemo}' + 'region'],
#             'wq_temperature' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_temperature'],
#             'wq_dissolved_oxygen_percent' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_dissolved_oxygen_percent'],
#             'wq_dissolved_oxygen' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_dissolved_oxygen'],
#             'wq_instantaneous_discharge' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_instantaneous_discharge'],
#             'wq_turbidity_ntu' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_turbidity_ntu'],
#             'wq_ph' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_ph'],
#             'wq_ammoniacal_nitrogen' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_ammoniacal_nitrogen'],
#             'wq_nitrate_nitrite' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_nitrate_nitrite'],
#             'wq_total_nitrogen' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_total_nitrogen'],
#             'wq_dissolved_phosphorus' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_dissolved_phosphorus'],
#             'wq_calcium' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_calcium'],
#             'wq_magnesium' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_magnesium'],
#             'wq_sodium' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_sodium'],
#             'wq_potassium' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_potassium'],
#             'wq_total_alkalinity' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_total_alkalinity'],
#             'wq_chloride' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_chloride'],
#             'wq_sulphate' : item['{http://niwa.co.nz/ns/nemo}' + 'wq_sulphate'],
#             'longitude' : item['{http://niwa.co.nz/ns/nemo}' + 'longitude'],
#             'latitude' : item['{http://niwa.co.nz/ns/nemo}' + 'latitude']
#         }

#         dump.append(new_object)

#     with open('dump.mini.json', 'w') as w:
#         w.write(json.dumps(dump))
    
# import json

# with open('file.json') as r:
#     data = r.read()
#     data = json.loads(data)
#     with open('file.json', 'w') as w:
#         w.write(json.dumps(data,sort_keys=True, indent=4, separators=(',', ': ')))