from django.contrib import admin
from .models import Member
from sorl.thumbnail.admin import AdminImageMixin

# Register your models here.

class MemberAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

admin.site.register(Member)
