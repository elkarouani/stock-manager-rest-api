from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Command

@admin.register(Command)
class CommandModelAdmin(VersionAdmin):
    pass
