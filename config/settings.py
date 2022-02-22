import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'w9s3hh)#qix8wl&zic06b90rb5b^c_=*01gyn51e(32v8$_$br'
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'orders.apps.OrdersConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATIC_ROOT = os.path.join(BASE_DIR, 'live-static', 'static-root')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static', 'media-root')

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    'site_title': 'Заказы на кофе в офис',

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    'site_header': 'Кофе в офис!',

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    'site_logo': 'images/coffee-beans.png',

    # Welcome text on the login screen
    'welcome_sign': 'Добро пожаловать',

    # Copyright on the footer
    'copyright': '',

    # The model admin to search from the search bar, search bar omitted if excluded
    'search_model': 'orders.Order',

    # Field name on user model that contains avatar image
    'user_avatar': '',

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    'topmenu_links': [
        {'name': 'Кофе в офис!',  'url': 'admin:index'},
        # {'model': 'orders.Order'},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    'usermenu_links': [{'model': 'auth.user'}],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': False,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    'order_with_respect_to': ['orders', 'auth'],

    # Custom links to append to app groups, keyed on app name
    'custom_links': {},

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'orders': 'fas fa-archive',
        'orders.order': 'fas fa-file-invoice-dollar'
},
    # Icons that are used when one is not manually specified
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    'related_modal_active': True,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    'custom_css': 'css/app-style.css',
    'custom_js': None,
    # Whether to show the UI customizer on the sidebar
    'show_ui_builder': True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    'changeform_format': 'horizontal_tabs',
    # override change forms on a per modeladmin basis
    'changeform_format_overrides': {
        'auth.user': 'collapsible', 'auth.group': 'vertical_tabs'
    },
    # Add a language dropdown into the admin
    'language_chooser': False,
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': False,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': False,
    'accent': 'accent-gray',
    'navbar': 'navbar-gray-dark navbar-dark',
    'no_navbar_border': False,
    'navbar_fixed': False,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': False,
    'sidebar': 'sidebar-dark-primary',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': True,
    'theme': 'spacelab',
    'dark_mode_theme': None,
    'button_classes': {
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success'
    }
}
