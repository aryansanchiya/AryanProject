from django.contrib import admin

# Register your models here.
from .models import Writing,Services

# admin.site.register(Writing)
# admin.site.register(Collobrate)

@admin.register(Writing)
class Writing(admin.ModelAdmin):
    list_display = ('title','date','Author')
    list_filter = ('date','Author')

@admin.register(Services)
class Collobrate(admin.ModelAdmin):
    list_display = ('fullname','company_name','email_address')