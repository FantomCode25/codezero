from flask import Blueprint

bp = Blueprint('appointments', __name__)

@bp.route('/appointments')
def list_appointments():
    return "Appointments List"
