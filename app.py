from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminders.db'
db = SQLAlchemy(app)

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    reminders = Reminder.query.all()
    return render_template('index.html', reminders=reminders)

@app.route('/add', methods=['GET', 'POST'])
def add_reminder():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        frequency = request.form['frequency']
        reminder = Reminder(title=title, category=category, frequency=frequency)
        db.session.add(reminder)
        db.session.commit()
        return redirect('/')
    return render_template('add_reminder.html')

@app.route('/delete/<int:id>')
def delete_reminder(id):
    reminder = Reminder.query.get(id)
    db.session.delete(reminder)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)