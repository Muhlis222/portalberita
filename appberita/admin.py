from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['create_date', 'publish_date', 'slug']

admin.site.register(Post, PostAdmin)