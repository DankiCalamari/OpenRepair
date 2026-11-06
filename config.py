import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'openrepair_user'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'openrepair')
}

SECRET_KEY = os.getenv('SECRET_KEY', 'clave-de-desarrollo')

# Initial admin: created on first startup only if there are no users.
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@openrepair.com')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')
ADMIN_NOMBRE = os.getenv('ADMIN_NOMBRE', 'Administrador')

BUSINESS_NAME = 'Sunset Country Tech'
BUSINESS_SHORT_NAME = 'SCT'
BUSINESS_EMAIL = 'support@sunsetcountry.tech'
BUSINESS_PHONE = '(03) 4504 2805'
BUSINESS_LOCATION = 'Mildura, Victoria, Australia'
BUSINESS_TIMEZONE = 'Australia/Melbourne'
