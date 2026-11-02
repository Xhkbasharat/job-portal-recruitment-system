from flask import Flask, render_template
from config import Config
from extensions import db, login_manager, bcrypt, migrate

# Import database models
from models import User, Job, Application

# Import route blueprints
from routes.auth import auth_bp
from routes.jobs import jobs_bp
from routes.recruiter import recruiter_bp
from routes.admin import admin_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Register application routes
    app.register_blueprint(auth_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(recruiter_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
  
