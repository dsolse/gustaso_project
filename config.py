DATA_BASE_NAME = "guaposesen"
USER = "root"
PASSWORD = "rootroot"


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        f"mysql://{USER}:{PASSWORD}@localhost:3306/{DATA_BASE_NAME}"
    )
    SQLALCHEMY_POOL_SIZE = 50
    SQLALCHEMY_POOL_TIMEOUT = 300
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1414892a04d3eb59b0c9953af3487cb1ff88152eb386b3bc50feac70e68098d71c682f63d3c0d8b5"
    LOGIN_DISABLED = False
