from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET", "POST"])
def project_list(request):
    """
    List all projects or create a new project.
    """
    if request.method == "GET":
        # Retrieve all projects
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        # Create a new project
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def project_detail(request, pk):
    """
    Retrieve, update or delete a project instance.
    """
    # Get the project instance or return 404 if not found
    project = get_object_or_404(Project, pk=pk)

    if request.method == "GET":
        # Retrieve a specific project
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == "PUT":
        # Update a specific project
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Delete a specific project
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)