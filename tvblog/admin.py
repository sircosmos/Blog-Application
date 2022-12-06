from django.contrib import admin
from .models import Post
from .models import Email

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ('status', 'published')


admin.site.register(Email)
