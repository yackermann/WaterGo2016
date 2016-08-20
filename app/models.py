from app import db

class Point(db.Model):
    __tablename__ = 'points'

    id          = db.Column(db.Integer, primary_key = True)

    # Site description
    site_desc                    = db.Column(db.String)
    # Region
    region                       = db.Column(db.String)

    # Temperature (deg C)
    temperature                  = db.Column(db.Float)
    # Dissolved oxygen (% saturation)
    dissolved_oxygen_percent     = db.Column(db.Float)
    # Dissolved oxygen (g/m3 O2)
    dissolved_oxygen             = db.Column(db.Float)
    # Instantaneous discharge (m3/s)
    instantaneous_discharge      = db.Column(db.Float)
    # Turbidity (NTU)
    turbidity_ntu                = db.Column(db.Float)
    # pH
    ph                           = db.Column(db.Float)
    # Ammoniacal nitrogen (mg/m3 N)
    ammoniacal_nitrogen          = db.Column(db.Float)
    # Nitrate/nitrite (mg/m3 N)
    nitrate_nitrite              = db.Column(db.Float)
    # Total nitrogen (mg/m3 N)
    total_nitrogen               = db.Column(db.Float)
    # Dissolved reactive phosphorus (mg/m3 P)
    dissolved_phosphorus         = db.Column(db.Float)
    # Calcium (g/m3)
    calcium                      = db.Column(db.Float)
    # Magnesium (g/m3)
    magnesium                    = db.Column(db.Float)
    # Sodium (g/m3)
    sodium                       = db.Column(db.Float)
    # Potassium (g/m3)
    potassium                    = db.Column(db.Float)
    # Total alkalinity (g CaCO3/m3)
    total_alkalinity             = db.Column(db.Float)
    # Chloride (g/m3)
    chloride                     = db.Column(db.Float)
    # Sulphate (g/m3 SO4)
    sulphate                     = db.Column(db.Float)
    # Longitude
    longitude                    = db.Column(db.Float)
    # Latitude
    latitude                     = db.Column(db.Float)

    # Source
    # https://gs.niwa.co.nz/nemo/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=nemo:fchem_chemistry_metadata

    def __init__(self, site_desc, region,
        temperature, dissolved_oxygen_percent, dissolved_oxygen,
        instantaneous_discharge, turbidity_ntu, ph,
        ammoniacal_nitrogen, nitrate_nitrite, total_nitrogen,
        dissolved_phosphorus, calcium, magnesium, sodium,
        potassium, total_alkalinity, chloride,
        sulphate, longitude, latitude):
    
        self.site_desc                    = site_desc 
        self.region                       = region 
        self.temperature                  = temperature 
        self.dissolved_oxygen_percent     = dissolved_oxygen_percent 
        self.dissolved_oxygen             = dissolved_oxygen 
        self.instantaneous_discharge      = instantaneous_discharge 
        self.turbidity_ntu                = turbidity_ntu 
        self.ph                           = ph 
        self.ammoniacal_nitrogen          = ammoniacal_nitrogen 
        self.nitrate_nitrite              = nitrate_nitrite 
        self.total_nitrogen               = total_nitrogen 
        self.dissolved_phosphorus         = dissolved_phosphorus 
        self.calcium                      = calcium 
        self.magnesium                    = magnesium 
        self.sodium                       = sodium 
        self.potassium                    = potassium 
        self.total_alkalinity             = total_alkalinity 
        self.chloride                     = chloride 
        self.sulphate                     = sulphate 
        self.longitude                    = longitude 
        self.latitude                     = latitude 

    def get_coordinates(self):
        return str(self.latitude) + ',' + str(self.longitude) 
