from flask import Flask, abort, redirect, render_template, request, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ToDos"
)

if db.is_connected():
    print("Connected to the database")


@app.route('/', methods=['GET', 'POST'])
def Home():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO todolist (`Task`, `Description`, created) "
            "VALUES (%s, %s, CURDATE())",
            (title, description),
        )
        db.commit()
        cursor.close()
        return redirect('/')
    
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, `Task` AS title, `Description` AS description, created "
        "FROM todolist ORDER BY id ASC"
    )
    todos = cursor.fetchall()

    cursor.close()
    return render_template('index.html', todos=todos)


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM todolist WHERE id = %s", (task_id,))
    db.commit()
    cursor.close()
    return redirect(url_for('Home'))


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, `Task` AS title, `Description` AS description, created "
        "FROM todolist WHERE id = %s",
        (task_id,),
    )
    todo = cursor.fetchone()
    if todo is None:
        cursor.close()
        abort(404)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        if not title:
            cursor.close()
            abort(400, description='Task title is required.')

        cursor.execute(
            "UPDATE todolist SET `Task` = %s, `Description` = %s WHERE id = %s",
            (title, description, task_id),
        )
        db.commit()
        cursor.close()
        return redirect(url_for('Home'))

    cursor.close()

    return render_template('edit.html', todo=todo)


if __name__ == '__main__':
    app.run(debug=True)