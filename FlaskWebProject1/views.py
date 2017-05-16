"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, abort, jsonify
from FlaskWebProject1 import app
import pandas as pd
from flask_mail import Message
from __init__ import mail



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/parse_geo_pal/davenport/material_to_csv', methods=['POST'])
def materials_to_csv():
    if not request.json:
        abort(400)
    csv_data = request.json
    for material in csv_data:
        material['total'] = float(material['total'])
        material['weight'] = float(material['weight'])
        material['amount'] = float(material['amount'])
    materials_df = pd.DataFrame(csv_data)
    materials_df.to_csv('FlaskWebProject1/static/files/materials_weight.csv')

    total = materials_df['total'].sum()
    email_address = "engineeringgeofile@gmail.com"

    message = Message("Hello World!",
                      sender=('Actavo-Engineering', "engineeringgeofile@gmail.com"),
                      recipients=["ben.chadwick@actavo.com"])
    message.body = "Material Weights Summary"
    with app.open_resource('static/files/materials_weight.csv') as csv_file:
        message.attach('materials_weight.csv', 'text/csv', csv_file.read())
    try:
        mail.send(message)
        return jsonify({'TotalWeight': total,
                        'EmailSent': 'true',
                        'EmailAddress': email_address}), 200
    except StandardError:
        return jsonify({"Email": "Failure"})
