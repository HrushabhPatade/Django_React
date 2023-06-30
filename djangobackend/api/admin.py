from django.contrib import admin
from api.models import Students

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuname', 'email')

admin.site.register(Students, StudentAdmin)    


# Register your models here.
