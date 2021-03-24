"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask import send_from_directory
from .form import propertyForm
from .models import PropertyInfo


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


#For displaying the form to add a new property.
@app.route('/property', methods=('GET', 'POST'))
def property():
    """Render the website's about page."""
    myform = propertyForm()

    if request.method == 'POST':
        if myform.validate_on_submit():
            propertyTitle = myform.title.data
            description = myform.description.data
            bedrooms = myform.bedroom.data
            bathrooms = myform.bathroom.data
            price = myform.price.data
            type = myform.type.data
            location = myform.location.data
            img = myform.image.data
            fname = myform.filename.data
            filename = secure_filename(img.filename)

            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        propertyinfo = PropertyInfo(request.form.get('propertyTitle', False), request.form.get('description', False), request.form.get('bedrooms', False), 
        request.form.get('bathrooms', False), request.form.get('price', False), request.form.get('type', False), request.form.get('location', False), request.form.get('filename', False))

        db.session.add(propertyinfo)
        db.session.commit()

        #flash('New user was successfully added')
        #return redirect(url_for('show_users'))
 
    return render_template('property.html', form=myform)


#For displaying a list of all properties in the database.
@app.route('/properties')
def properties():
    """Render the website's about page."""
    return render_template('properties.html')


#For viewing an individual property by the specific property id.
@app.route('/property/<propertyid>')
def get_property(fileID):
    root_dir = os.getcwd()

    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), fileID)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
