from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model with all CRUD operations."""
    
    full_name = serializers.ReadOnlyField()
    
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'full_name',
            'email',
            'phone',
            'date_of_birth',
            'gender',
            'address',
            'enrollment_date',
            'course',
            'grade',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'enrollment_date', 'created_at', 'updated_at']
    
    def validate_email(self, value):
        """Ensure email is lowercase."""
        return value.lower()


class StudentListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing students."""
    
    full_name = serializers.ReadOnlyField()
    
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'course', 'is_active']
