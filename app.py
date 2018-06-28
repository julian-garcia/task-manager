from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = 'mongodb://root:tablet12@ds221631.mlab.com:21631/task_manager'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html",
                           tasks=mongo.db.tasks.find())

@app.route('/add_task')
def add_task():
    return render_template("addtask.html")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT') or 8000),
            debug=True)
