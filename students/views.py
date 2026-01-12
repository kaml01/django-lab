from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Student
from .serializers import StudentSerializer, StudentListSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Student CRUD operations.
    
    Endpoints:
    - GET    /api/students/          - List all students
    - POST   /api/students/          - Create a new student
    - GET    /api/students/{id}/     - Retrieve a student
    - PUT    /api/students/{id}/     - Update a student (full)
    - PATCH  /api/students/{id}/     - Update a student (partial)
    - DELETE /api/students/{id}/     - Delete a student
    - GET    /api/students/active/   - List only active students
    """
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'course']
    ordering_fields = ['first_name', 'last_name', 'created_at', 'enrollment_date']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Use lightweight serializer for list action."""
        if self.action == 'list':
            return StudentListSerializer
        return StudentSerializer
    
    def create(self, request, *args, **kwargs):
        """Create a new student with custom response."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                'message': 'Student created successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        """Update a student with custom response."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {
                'message': 'Student updated successfully',
                'data': serializer.data
            }
        )
    
    def destroy(self, request, *args, **kwargs):
        """Delete a student with custom response."""
        instance = self.get_object()
        student_name = instance.full_name
        self.perform_destroy(instance)
        return Response(
            {
                'message': f'Student "{student_name}" deleted successfully'
            },
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only active students."""
        active_students = Student.objects.filter(is_active=True)
        serializer = StudentListSerializer(active_students, many=True)
        return Response(serializer.data)
