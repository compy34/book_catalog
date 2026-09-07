    from Flask_sqlalchemy import SQLAlchemy
    from Flask_login import LoginManager

    db = SQLAlchemy()
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'