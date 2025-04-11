from flask import Blueprint, jsonify
from controllers import patient_controller

bp = Blueprint('patients', __name__)

@bp.route('/patients')
def get_patients():
    return jsonify(patient_controller.get_all())
