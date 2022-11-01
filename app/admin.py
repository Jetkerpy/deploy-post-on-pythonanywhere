from django.contrib import admin
from .models import Post

# Register your models here.


admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 5
    