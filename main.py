from flask import Flask, request, jsonify
from mailer import Mailer

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    receiver = data.get('receiver')
    subject = data.get('subject')
    message = data.get('message')

    if not email or not password or not receiver or not subject or not message:
        return jsonify({'error': 'Email, password, receiver, subject, and message are required'}), 400

    mail = Mailer(email=email, password=password)
    mail.settings(provider=mail.MICROSOFT)
    mail.send(receiver=receiver, subject=subject, message=message)

    if mail.status:
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
