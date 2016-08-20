from app import db

class Point(db.Model):
    __tablename__ = 'points'

    id          = db.Column(db.Integer, primary_key = True)

    site_desc                    = db.Column(db.String)
    region                       = db.Column(db.String)

    temperature                  = db.Column(db.Float)
    dissolved_oxygen_percent     = db.Column(db.Float)
    dissolved_oxygen             = db.Column(db.Float)
    instantaneous_discharge      = db.Column(db.Float)
    turbidity_ntu                = db.Column(db.Float)
    ph                           = db.Column(db.Float)
    ammoniacal_nitrogen          = db.Column(db.Float)
    nitrate_nitrite              = db.Column(db.Float)
    total_nitrogen               = db.Column(db.Float)
    dissolved_phosphorus         = db.Column(db.Float)
    calcium                      = db.Column(db.Float)
    magnesium                    = db.Column(db.Float)
    sodium                       = db.Column(db.Float)
    potassium                    = db.Column(db.Float)
    total_alkalinity             = db.Column(db.Float)
    chloride                     = db.Column(db.Float)
    sulphate                     = db.Column(db.Float)
    longitude                    = db.Column(db.Float)
    latitude                     = db.Column(db.Float)

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
