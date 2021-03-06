# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request
from app.models import *
from app.forms import reg_call
from flask_json import as_json


@app.route('/api/<method>/<mean>')
@as_json
def api(method, mean):
    if method == "get":
        data = {}
        if mean == "current_calls":
            alarms = db.session.query(Signals).filter(Signals.status == 'alarm').all()
            for alarm in alarms:
                tmp = {}
                tmp['id'] = alarm.id
                tmp['bed_id'] = alarm.bed_id
                tmp['datetime'] = alarm.datetime
                tmp['branch_name'] = alarm.bed.ward.branch.name
                tmp['ward_name'] = alarm.bed.ward.name
                tmp['bed_name'] = alarm.bed.name
                data.update({f'call{alarm.id}': tmp})
            return data
        if mean == "test":
            return [{"qwe": "qwe"}, 2, 3]
    return "error"
            

@app.route('/call', methods=['GET', 'POST'])
def call():
    form = reg_call()
    if form.validate_on_submit():
        db.session.add(Signals(bed_id=form.bed_id.data, status=form.status.data))
        db.session.commit()
    return 'good'


@app.route('/')
@app.route('/index')
def index():
    return 'something'


@app.route('/display', methods=['GET', 'POST'])
def display():
    alarms = db.session.query(Signals).all()
    if request.method == 'POST':
        if 'index' in request.form:
            dalarm = db.session.query(Signals).filter(Signals.id == int(request.form['index'])).first()
            dalarm.status = 'done'
            db.session.add(dalarm)
            db.session.commit()
        elif request.form['action'] == 'Update':
            return render_template('display.html', alarms=alarms, title='signal display')
        elif request.form['action'] == 'Done':
            for alarm in alarms:
                alarm.status = 'done'
                db.session.commit()
        return render_template('display.html', alarms=alarms, title='signal display')
    elif request.method == 'GET':
        return render_template('display.html', alarms=alarms, title='signal display')


@app.route('/done_display', methods=['GET', 'POST'])
def done_display():
    alarms = db.session.query(Signals).filter(Signals.status == 'done')
    if request.method == 'POST':
        if request.form.get('update') == 'Update':
            return render_template('done_display.html', alarms=alarms, title='d0ne display')
        elif request.form.get('clear') == 'Clear':
            for alarm in alarms:
                db.session.delete(alarm)
                db.session.commit()
            return render_template('done_display.html', alarms=alarms, title='d0ne display')
    elif request.method == 'GET':
        return render_template('done_display.html', alarms=alarms, title='d0ne display')
