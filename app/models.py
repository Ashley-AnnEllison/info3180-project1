from werkzeug.security import generate_password_hash
from . import db;


class PropertyInfo(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    #__tablename__ = 'property_info'

    id = db.Column(db.Integer, primary_key=True)
    propertyTitle = db.Column(db.String(80))
    description = db.Column(db.String(255), nullable=False)
    bedrooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    price = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    filename = db.Column(db.String(80))
    #save filename also
    #image =  FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])

    def  __init__(self, propertyTitle, description, bedrooms, bathrooms, price, type, location, filename):
        self.propertyTitle = propertyTitle
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.type = type
        self.location = location
        self.filename = filename

    """ def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support"""

    def __repr__(self):
        return '<PropertyInfo %r>' % (self.propertyTitle) 