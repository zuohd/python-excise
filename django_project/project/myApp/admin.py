from django.contrib import admin

# Register your models here.
from .models import Grades, Children


class GradesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDeleted']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    # fields = ['ggirlnum','gboynum','gname','gdate','isDeleted']
    # fieldsets = []


admin.site.register(Grades, GradesAdmin)
admin.site.register(Children)
