"""Settings for the kbowen-django-todo template project."""

from pathlib import Path

from environs import Env

# import socket # Comment out if not using debug_toolbar

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = ["django-todo.cool", "localhost", "127.0.0.1"]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party applications
    "crispy_forms",
    "crispy_bootstrap4",
    # "debug_toolbar",
    "django_countries",
    "django_extensions",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    # Local applications
    "tasks.apps.TasksAppConfig",
    "accounts.apps.AccountsConfig",
    "pages.apps.PagesConfig",
]

MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# Note: Set sqlite/dev URI in .env file
DATABASES = {
    "default": {
        "ENGINE": env.str("ENGINE_DB", "django.db.backends.postgresql"),
        "DATABASE_URL": env.dj_db_url(
            "DATABASE_URL", default="postgres://postgres@db/postgres"
        ),
        "NAME": env.str("POSTGRES_DB", "postgres"),
        "USER": env.str("POSTGRES_USER", default="fakeuser"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", "password"),
        "HOST": env.str("POSTGRES_HOST", "db"),
        "PORT": env.int("POSTGRES_PORT", "5432"),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Vancouver"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

# django-allauth config
LOGIN_REDIRECT_URL = "index"
ACCOUNT_LOGOUT_REDIRECT = "home"
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGIN_METHODS = {"username", "email"}
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True

SOCIALACCOUNT_PROVIDERS = {
    "github": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        # "VERIFIED_EMAIL": True
        "APP": {
            "client_id": env.str("GITHUB_SOCIALACCOUNT_APP_CLIENT_ID"),
            "secret": env.str("GITHUB_SOCIALACCOUNT_APP_SECRET"),
            "key": "",
        },
    }
}

# third-party email relay configuration
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "kevin.bowen@gmail.com"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Used in production deployment
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
# Use the following line for testing docker-compose-prod.yml locally:
# SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=False)
SECURE_HSTS_SECONDS = env.int(
    "DJANGO_SECURE_HSTS_SECONDS",
    default=2592000,
)  # 30 days
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS",
    default=True,
)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)

# django-crispy-forms
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_CLASS_CONVERTERS = {
    "textinput": "textinput textInput",
    "fileinput": "fileinput fileUpload",
    "passwordinput": "textinput textInput",
}

# media/file uploads URLs
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

ADMINS = [("Kevin Bowen", "kevinbowen@protonmail.com")]
MANAGERS = ADMINS

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}

# django-debug-toolbar

# Note: disable when running Nox tests
# Uncomment the following two lines for using toolbar in Docker:
# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
# The following line is for toolbar use locally:
# INTERNAL_IPS = ["127.0.0.1"]
