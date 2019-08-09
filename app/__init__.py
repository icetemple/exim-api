from .factory import Factory
from config import config


def create_app(config_name: str) -> Factory:
    app = Factory(__name__, )
    app.url_map.strict_slashes = False
    app.config.from_object(config[config_name])

    app.register_controllers()
    return app
