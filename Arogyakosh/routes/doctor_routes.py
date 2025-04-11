from flask import Blueprint

bp = Blueprint('doctors', __name__)

@bp.route('/doctors')
def list_doctors():
    return "Doctors List"
