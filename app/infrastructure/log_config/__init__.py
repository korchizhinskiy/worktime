import logging.config


def configure_logging() -> None:
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "()": "app.infrastructure.log_config.formatter.ColourizedFormatter",
                "fmt": "%(asctime)s - %(levelname)s - %(message)s",
                "use_colors": True,
            },
            "access": {
                "()": "app.infrastructure.log_config.formatter.UvicornAccessColourizedFormatter",
                "fmt": "%(asctime)s - %(levelname)s - %(message)s",
                "use_colors": True,
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "level": "DEBUG",
            },
            "access": {
                "class": "logging.StreamHandler",
                "formatter": "access",
                "level": "DEBUG",
            },
        },
        "loggers": {
            "app": {
                "handlers": ["console"],
                "level": "DEBUG",
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["access"],
                "level": "DEBUG",
                "propagate": False,
            },
        },
    }
    logging.config.dictConfig(log_config)
