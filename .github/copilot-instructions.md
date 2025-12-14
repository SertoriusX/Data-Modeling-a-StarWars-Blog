# Copilot instructions — Flask app (core/)

Short, actionable guidance to help an AI agent be productive in this repository.

- **Big picture:** This is a small Flask application whose runtime lives in `run.py` and whose application object, DB, and modules live in the `core/` package. The app and SQLAlchemy `db` singletons are created in [core/__init__.py](core/__init__.py#L1-L20). Models and routes are imported at package import time to register them with the app.

- **Key files:**
  - **App entry:** `run.py` — runs the dev server and calls `db.create_all()`.
  - **App bootstrap:** `core/__init__.py` — `app = Flask(__name__)`, `db = SQLAlchemy(app)`, `migrate = Migrate(app, db)`.
  - **Data models:** `core/models.py` — currently incomplete; fix obvious syntax before adding models.
  - **Routes:** `core/routers.py` — place API endpoints here (prefer Blueprints for features).
  - **Business logic:** `core/service.py` — put core non-HTTP logic here and call from routes.

- **Database & migrations:** The project uses SQLite by default (`sqlite:///myDatabase.db`). Prefer Flask-Migrate for schema changes instead of `db.create_all()`.
  - Dev server (quick): `python run.py` (this will call `db.create_all()` as the current shortcut).
  - Flask CLI (recommended): `flask --app run.py run --debugger --reload` or on PowerShell: `$env:FLASK_APP='run.py'; flask run`.
  - Migrations: `flask --app run.py db init` (once), `flask --app run.py db migrate -m "msg"`, `flask --app run.py db upgrade`.

- **Patterns & conventions (project-specific):**
  - Keep routes thin and stateless. Implement business logic inside `core/service.py` and call it from `core/routers.py`.
  - Avoid circular imports: import `db`/`app` from `core` rather than duplicating creation, and follow the existing pattern of importing models/routes at the end of `core/__init__.py` to register them.
  - When adding new routes, prefer Blueprints and register them in `core/__init__.py` or import them from there so they load on package import.

- **Concrete examples:**
  - Registering a blueprint in `core/__init__.py`:

```py
from flask import Blueprint

bp = Blueprint('api', __name__)

@bp.route('/ping')
def ping():
    return {'ok': True}

app.register_blueprint(bp, url_prefix='/api')
```

  - Service usage pattern (in `core/service.py`): keep pure functions that accept primitive inputs and return serializable results — call them from `core/routers.py`.

- **Developer workflow notes:**
  - Create a virtualenv and install dependencies. The environment in this workspace includes packages like Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-WTF, Flask-Login, flask-cors, flask-bcrypt, Flask-JWT-Extended, and Pillow. If `requirements.txt` is missing, create it with `pip freeze > requirements.txt`.
  - Quick sanity check to catch syntax errors: `python -c "import core; print(core.app.name)"` — this will reveal import-time errors.

- **What to watch for when editing:**
  - `core/models.py` currently has a syntax error (e.g. malformed `import uuid from`); fix and run the quick sanity check above.
  - If you change model definitions, add a migration instead of manually editing the DB file.
  - Keep package-level side effects minimal; importing `core` should be safe and fast.

- **Suggested first issues for an AI agent:**
  - Fix the syntax in `core/models.py` and add a minimal `User` model.
  - Add a simple `/api/ping` route to `core/routers.py` using a Blueprint and a corresponding unit test.
  - Add `requirements.txt` and a short `README.md` describing the dev commands above.

If anything here is unclear or you want more project-specific rules (tests, PR message templates, CI), tell me which area to expand and I'll iterate.
