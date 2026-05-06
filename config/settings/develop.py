"""Development settings."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

from .base import *  # noqa: F401, F403, E402

DEBUG = True

SECRET_KEY = os.environ.get(  # type: ignore[assignment]
    "SECRET_KEY",
    "dev-insecure-secret-key-change-in-production",
)

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
