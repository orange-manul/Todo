from django.contrib import admin
from .models import Todo
# Register your models here.

class AdminTodo(admin.ModelAdmin):
    readonly_fields = ('createDate',)

admin.site.register(Todo, AdminTodo)
