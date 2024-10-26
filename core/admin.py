from django.contrib import admin
from core.models import Post, Tag

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'created_at')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
