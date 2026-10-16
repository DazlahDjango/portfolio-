from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail

from app.config import config

# Extensions — created here, initialized inside create_app()
csrf = CSRFProtect()
mail = Mail()


def create_app(config_name='default'):
    """
    Application factory. Builds and returns a configured Flask app.
    Called by run.py (dev) and wsgi.py (production).
    """
    app = Flask(__name__, instance_relative_config=True)

    # Load the chosen configuration
    app.config.from_object(config[config_name])

    # Ensure the instance folder exists (Flask uses it for local-only data)
    import os
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Initialize extensions with this app
    csrf.init_app(app)
    mail.init_app(app)

    # Register blueprints (routes)
    from app.routes import main
    app.register_blueprint(main)

        # --- Context processor: variables available in every template ---
    @app.context_processor
    def inject_globals():
        from datetime import datetime
        from content.profile import PROFILE

        return {
            'profile': PROFILE,
            'current_year': datetime.now().year,
        }

    return app