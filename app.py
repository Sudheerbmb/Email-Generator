from flask import Flask, render_template, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sudheerdata@outlook.com'
app.config['MAIL_PASSWORD'] = 'Sudheer@123'
app.config['MAIL_DEFAULT_SENDER'] = 'sudheerdata@outlook.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        msg = Message('Hello from Flask', recipients=[' '])
        msg.body = 'This is a test email sent from a Flask application.'
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send email: {str(e)}', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
