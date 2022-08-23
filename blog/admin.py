from django.contrib import admin

from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ("title", "date", "author")
  list_filter = ("title", "date", "author",)


class CommentAdmin(admin.ModelAdmin):
  list_filter = ("post",)
  list_display = ("post", "user_name")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
