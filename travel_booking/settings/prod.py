from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com"]

# Security settings for production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
