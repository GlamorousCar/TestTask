from django.contrib import admin

# Register your models here.
from .models import Article, Comment


@admin.register(Comment)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'text',)
    date_hierarchy = 'created_date'


admin.site.register(Article)
