=====
Django Sprofile
=====

Based on django-profile-middleware

Compatible with Django 1.11 and later

Python 3.x

Quick start
-----------

1. Add "django_sprofile" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'django_sprofile',
    ]

2. Add "django_sprofile.middleware.sProfilerMiddleware" to your MIDDLEWARE setting like this:

    MIDDLEWARE = [
        ...
        'django_sprofile.middleware.sProfilerMiddleware',
    ]

3. Set sProfile Config(PROFILER) to your setting:

    PROFILER = {
        'enable': True,
        'sort': 'time',
        'count': None ,
        'output': ['console','file'],             
        'file_location': 'profiling_results.txt'
    }

TODO
----
1.better logfile
2.dashboard