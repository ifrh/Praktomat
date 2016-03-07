# Settings for development in the source tree

from os.path import join, dirname

# The name that will be displayed on top of the page and in emails.
SITE_NAME = 'Praktomat'

# Identifie this Praktomat among multiple installation on one webserver
PRAKTOMAT_ID = 'default' 

# The URL where this site is reachable. 'http://localhost:8000/' in case of the
# developmentserver.
# BASE_HOST = 'http://praktomat.inf.h-brs.de:8910'
BASE_HOST = 'http://localhost:8000'
BASE_PATH = '/'

# URL to use when referring to static files.
STATIC_URL = BASE_PATH + 'static/'

# Absolute path to the directory that shall hold all uploaded files as well as
# files created at runtime.

# Example: "/home/media/media.lawrence.com/"
UPLOAD_ROOT = join(dirname(dirname(dirname(__file__))),'data')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':   UPLOAD_ROOT+'/Database',
    }
}


PRIVATE_KEY = join(dirname(dirname(dirname(__file__))), 'examples', 'certificates', 'privkey.pem')


REGISTRATION_POSSIBLE = False
ACCOUNT_CHANGE_POSSIBLE = False
DUMMY_MAT_NUMBERS = True
SHOW_CONTACT_LINK = False


# Various extra files and versions
#CHECKSTYLEALLJAR = '/srv/praktomat/contrib/checkstyle-5.7-all.jar'
CHECKSTYLEALLJAR = '/opt/praktomat-addons/checkstyle-6.15-all.jar'
JAVA_LIBS = { 'junit3' : '/usr/share/java/junit.jar', 'junit4' : '/opt/praktomat-addons/junit4.12.jar' }


# LDAP
AUTHENTICATION_BACKENDS = (
    'accounts.ldap_auth.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
LDAP_URI="ldap://ldap.inf.fh-brs.de"
LDAP_BASE="dc=fh-bonn-rhein-sieg,dc=de"



# Finally load defaults for missing settings.
import defaults
defaults.load_defaults(globals())

# To get exceptions logged as well:
MIDDLEWARE_CLASSES += (
        'utilities.exceptionlogger.ExceptionLoggingMiddleware',
    )
