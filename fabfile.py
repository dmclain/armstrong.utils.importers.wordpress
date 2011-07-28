from armstrong.dev.tasks import *


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.core.arm_sections',
        'armstrong.apps.articles',
        'armstrong.apps.content',
        'armstrong.utils.importers.wordpress',
        'lettuce.django',
    ),
}

tested_apps = ("wordpress", )
