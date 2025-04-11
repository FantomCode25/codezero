from flask import Flask
from routes import auth_routes, patient_routes, appointment_routes, doctor_routes

app = Flask(__name__)
app.secret_key = "supersecret"

# Register Blueprints
app.register_blueprint(auth_routes.bp)
app.register_blueprint(patient_routes.bp)
app.register_blueprint(appointment_routes.bp)
app.register_blueprint(doctor_routes.bp)

if __name__ == '__main__':
    app.run(debug=True)
