from pathlib import Path
SECRET_KEY = 'f3432rr3fwe4'
INSTALLED_APPS = [
    "CaseConnect.tests",
    'django.contrib.contenttypes',
]


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}