from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'participant_info',
        'display_name': "Enroll in secret project",
        'num_demo_participants': 2,
        'app_sequence': ['participant_info'],
    },
    {
        'name': 'codenames',
        'display_name': "Only you can save the world",
        'num_demo_participants': 2,
        'app_sequence': ['participant_info','codenames'],
    },
    # other session configs ...
]

#my IP adress is:
#192.168.1.37

#start with sudo otree runserver 10.192.51.29:80


#http://192.168.1.37:8000/


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = 'STUDY'

ADMIN_USERNAME = "D"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = "DK"


# Consider '', None, and '0' to be empty/false
DEBUG =0

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = 't3^-vs&6t78er@w8cqp6#!_5ualbnl_h7(qm#2(if1b(^7z%x3'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
