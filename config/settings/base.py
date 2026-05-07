"""Base settings shared across all environments."""
from pathlib import Path

import os
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party
    "django_htmx",
    # local
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "uk"
TIME_ZONE = "Europe/Kyiv"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email — Gmail SMTP
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
NOTIFICATION_EMAIL = os.environ.get("NOTIFICATION_EMAIL", os.environ.get("EMAIL_HOST_USER", ""))

# Cloudinary
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME", ""),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY", ""),
    "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET", ""),
}

# ── Unfold Admin ──────────────────────────────────────────────────────────────

UNFOLD = {
    "SITE_TITLE": "Фанери",
    "SITE_HEADER": "Фанери — Адміністрування",
    "SITE_SYMBOL": "inventory_2",
    "SHOW_HISTORY": False,
    "SHOW_VIEW_ON_SITE": False,
    "COLORS": {
        "primary": {
            "50": "240 249 255",
            "100": "224 242 254",
            "200": "186 230 253",
            "300": "125 211 252",
            "400": "56 189 248",
            "500": "14 165 233",
            "600": "2 132 199",
            "700": "3 105 161",
            "800": "7 89 133",
            "900": "12 74 110",
            "950": "8 47 73",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "CMS",
                "separator": False,
                "items": [
                    {
                        "title": "Налаштування сайту",
                        "icon": "settings",
                        "link": reverse_lazy("admin:core_sitesettings_changelist"),
                    },
                    {
                        "title": "Продукти",
                        "icon": "category",
                        "link": reverse_lazy("admin:core_product_changelist"),
                    },
                    {
                        "title": "Галерея",
                        "icon": "photo_library",
                        "link": reverse_lazy("admin:core_galleryimage_changelist"),
                    },
                ],
            },
            {
                "title": "Заявки",
                "separator": True,
                "items": [
                    {
                        "title": "Дзвінки",
                        "icon": "phone_callback",
                        "link": reverse_lazy("admin:core_callbackrequest_changelist"),
                    },
                    {
                        "title": "Повідомлення",
                        "icon": "mail",
                        "link": reverse_lazy("admin:core_contactmessage_changelist"),
                    },
                ],
            },
        ],
    },
}
