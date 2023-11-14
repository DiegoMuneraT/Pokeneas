from flask import Blueprint, jsonify, render_template
from random import choice
from models import pokeneas
import os

app = Blueprint('pokenea_app', __name__)

@app.route('/pokenea_info', methods=['GET'])
def get_pokenea_info():
    random_pokenea = choice(pokeneas)
    pokenea_info = {
        'id': random_pokenea.id,
        'nombre': random_pokenea.nombre,
        'altura': random_pokenea.altura,
        'habilidad': random_pokenea.habilidad,
        'contenedor': os.uname()[1],
    }
    return jsonify(pokenea_info)

@app.route('/pokenea_random', methods=['GET'])
def get_random_pokenea():
    random_pokenea = choice(pokeneas)
    contenedor = os.uname()[1]
    return render_template('pokenea_template.html', pokenea=random_pokenea, contenedor=contenedor)