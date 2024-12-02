from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import ssl

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    required_fields = ['email', 'firstName', 'lastName', 'position']
    
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Campos faltantes"}), 400

    try:
        msg = MIMEMultipart()
        msg['From'] = os.getenv('EMAIL_HOST_USER')
        msg['To'] = data['email']
        msg['Subject'] = "Registro Exitoso"

        body = f"""
        Hola {data['firstName']} {data['lastName']},

        Te hemos registrado como Aplicante para la posicion {data['position']}.

        Saludos,
        Equipo.
        """
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 465)
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        server.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
        text = msg.as_string()
        server.sendmail(os.getenv('EMAIL_HOST_USER'), data['email'], text)
        server.quit()

        return jsonify({"message": "Correo enviado exitosamente"}), 200

    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación SMTP")
        return jsonify({"message": "Error de autenticación con el servidor de correo"}), 500
    except smtplib.SMTPException as e:
        print(f"Error SMTP: {str(e)}")
        return jsonify({"message": "Error al enviar el correo"}), 500
    except Exception as e:
        print(f"Error general: {str(e)}")
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    print("Email Config:")
    print(f"HOST: {os.getenv('EMAIL_HOST')}")
    print(f"USER: {os.getenv('EMAIL_HOST_USER')}")
    app.run(debug=True, port=5000)