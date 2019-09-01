
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'uspressm',
        'USER': 'uspressm',
        'PASSWORD' : 'codefair',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
