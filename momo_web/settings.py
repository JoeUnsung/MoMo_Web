"""
Django settings for momo_web project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^f4h*i)xwqt5e_1deirro#0$@bkj3u=ejap&(c9k-s49+l_=fx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'momo',
    'job',
    'django.contrib.sites', # new

    # 3rd party
    'allauth', # new
    'allauth.account', #new
    'allauth.socialaccount', #new

    # local
    'user.apps.UserConfig', # new

    # debug
    'debug_toolbar',

    # 금액 천단위 콤마
    'django.contrib.humanize',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'job.middleware.JobMiddleware'
]

ROOT_URLCONF = 'momo_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'momo_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'schoolRoad',
        'USER': 'momo',
        # 'PASSWORD': 'secret',  # ken
        'PASSWORD': 'Momokorea!3', # Kyle
        # 'PASSWORD': '!1q2w3e4r', # Joe>>>>>>> 6e70a34cc065fe88a8cb010b31023bceea9244f3
        'HOST': 'schoolroad.cxstjzyie2g8.ap-northeast-1.rds.amazonaws.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
                 "init_command": "SET foreign_key_checks = 0;",
            },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

DATE_INPUT_FORMATS = ['%Y-%m-%d']

## --------------------------------------------------------------------------------------------------------- ##
## title : django allauth 제어
## Reference : https://wsvincent.com/django-login-with-email-not-username/
AUTH_USER_MODEL = 'user.CustomUser' # new
ACCOUNT_FORMS = {'signup': 'user.forms.MyCustomSignupForm'}

LOGIN_REDIRECT_URL = '/job/' #home >> 나중에 Kyle이랑 합칠 때 피드 URL 넣을 부분임
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGOUT_REDIRECT_URL = '/user/signup' #home'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False # 로그인 후 로그인/회원가입 페이지 접근 제어 하도록 하는 설정 https://django-allauth.readthedocs.io/en/latest/configuration.html
SITE_ID = 1

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_UNIQUE_EMAIL = True


## --------------------------------------------------------------------------------------------------------- ##
## title : 검증 email 전송
## Reference : https://ssungkang.tistory.com/entry/Django-회원가입-시-이메일-인증-SMTP
ACCOUNT_EMAIL_SUBJECT_PREFIX = None
EMAIL_HOST = 'smtp.gmail.com' # 메일을 호스트하는 서버
EMAIL_PORT = 587 # gmail과의 통신하는 포트
EMAIL_HOST_USER = 'momonim.korea@gmail.com' # 발신할 이메일
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = 'joekorea3' # 발신할 메일의 비밀번호
EMAIL_USE_TLS = True # TLS 보안 방법


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of 'allauth'
    "django.contrib.auth.backends.ModelBackend",
    #`allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


INTERNAL_IPS = [
    '127.0.0.1',
    'http://schoolroad-env.hvnkhfbpdb.ap-northeast-1.elasticbeanstalk.com/',
    '13.114.209.60'
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: True,  # disables it
    # '...
}
