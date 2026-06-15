from django.contrib import admin

from polls.templatetags.poll_extras import register
from . import models

# Register your models here.

admin.site.register(models.User)