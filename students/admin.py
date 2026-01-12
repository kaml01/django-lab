from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'course', 'is_active', 'enrollment_date']
    list_filter = ['is_active', 'gender', 'course', 'enrollment_date']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at', 'enrollment_date']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'gender')
        }),
        ('Academic Information', {
            'fields': ('course', 'grade', 'enrollment_date')
        }),
        ('Address', {
            'fields': ('address',),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
