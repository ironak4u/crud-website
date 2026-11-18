# TaskFlow — To-Do List

A small Flask CRUD web app for keeping a to-do list in a **local MySQL database**. Add tasks with descriptions, view the list and creation dates, update tasks, and delete tasks.

## Requirements

- Python 3.8 or later
- MySQL Server running on your computer
- `pip` (included with most Python installations)

## 1. Set up the local database

Start your MySQL server, then connect to it using your MySQL client (for example, `mysql -u root -p`) and run:

```sql
CREATE DATABASE ToDos;
USE ToDos;

CREATE TABLE todolist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `Task` VARCHAR(100) NOT NULL,
    `Description` VARCHAR(200),
    created DATE NOT NULL
);
```

The app connects to MySQL at `localhost` and currently uses the credentials `root` / `root` in `app.py`. If your local MySQL username or password is different, update the connection settings in `app.py` to match before starting the app. The database and table names and columns must match the schema above.

## 2. Install the Python dependencies

From the repository folder, create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate it:

- **Windows (Command Prompt):** `.venv\Scripts\activate.bat`
- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
- **macOS/Linux:** `source .venv/bin/activate`

Install Flask and the MySQL connector:

```bash
python -m pip install Flask mysql-connector-python
```

## 3. Start the web app

Make sure MySQL is running and the connection settings in `app.py` are correct. Then run:

```bash
python app.py
```

Open <http://127.0.0.1:5000> in your browser.

## Using the to-do list

- **Add a task:** Enter a task title and, optionally, a description. Select **Add Task** to save it to MySQL.
- **View tasks:** The home page lists saved tasks and their creation dates. The task count updates with the list.
- **Update a task:** Select **Update**, edit the title or description, then select **Save Changes**. Use **Cancel** to return without saving.
- **Delete a task:** Select **Delete** and confirm. The task is removed from the database.

Changes are stored in the local `ToDos.todolist` table and remain available after the app is restarted.

## Project structure

```text
.
├── app.py              # Flask routes and MySQL CRUD operations
├── templates/
│   ├── base.html       # Shared page layout
│   ├── index.html      # To-do list and add-task form
│   └── edit.html       # Update-task form
└── README.md
```

## Notes

- This app expects the MySQL database and table to be created before it starts; it does not create them automatically.
- `app.py` currently hardcodes local database credentials and starts Flask with `debug=True`. These settings are intended for local development only. Do not expose the debug server publicly; use environment-based secrets and disable debug mode before deploying.
