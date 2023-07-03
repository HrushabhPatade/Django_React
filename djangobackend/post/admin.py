from django.contrib import admin
from post.models import Form

class FormAdmin(admin.ModelAdmin):
    list_display=('id','name', 'email', 'message')

admin.site.register(Form, FormAdmin)
# Register your models here.
