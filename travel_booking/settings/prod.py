from .base import *


ALLOWED_HOSTS = ["travel-booking-application-production.up.railway.app"]

# Security settings for production
CSRF_TRUSTED_ORIGINS = [
    "https://travel-booking-application-production.up.railway.app",
]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
