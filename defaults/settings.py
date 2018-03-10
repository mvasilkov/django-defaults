# Options specific to django-defaults

DJANGO_ROOT = None
ROUTES_MODULE = None
SETTINGS_MODULE = None

# Django settings

DEBUG = None

SECRET_KEY = None

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = None


def finalize(*, debug: bool = False):
    """
    Finalize settings at runtime.
    """

    global DEBUG, SECRET_KEY, ROOT_URLCONF

    DEBUG = debug

    if debug:
        SECRET_KEY = 'POTATO'

        ALLOWED_HOSTS.append('*')

    ROOT_URLCONF = ROUTES_MODULE
