from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Entry

@app.route('/')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry_content = request.form['content']
    new_entry = Entry(content=entry_content)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))
