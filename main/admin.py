from django.contrib import admin
from .models import Gallery, Contact

# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image',]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'sex']

# You can customize the way these models are displayed in the admin interface by adding more configurations to the respective Admin classes.
