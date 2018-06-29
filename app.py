from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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

@app.route('/add_task', methods=['POST','GET'])
def add_task():
    if request.method == 'POST':
        is_urgent = 'false' if request.form.get('is_urgent', 'false')=='false' else 'true'
        new_task = {
                    'category_name': request.form["category"],
                    'task_name': request.form["task_name"],
                    'task_description': request.form["task_description"],
                    'is_urgent': is_urgent,
                    'due_date': request.form["due_date"]
                   }
        mongo.db.tasks.insert(new_task)
        return redirect(url_for('get_tasks'))

    return render_template("addtask.html", categories = mongo.db.categories.find())

@app.route('/edit_task/<task_id>', methods=['POST','GET'])
def edit_task(task_id):
    if request.method == 'POST':
        is_urgent = 'false' if request.form.get('is_urgent', 'false')=='false' else 'true'
        update_task = {
                    'category_name': request.form["category"],
                    'task_name': request.form["task_name"],
                    'task_description': request.form["task_description"],
                    'is_urgent': is_urgent,
                    'due_date': request.form["due_date"]
                   }
        mongo.db.tasks.update({'_id': ObjectId(task_id)}, update_task)
        return redirect(url_for('get_tasks'))

    the_task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edittask.html', task=the_task, categories=all_categories)

if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT') or 8000),
            debug=True)
