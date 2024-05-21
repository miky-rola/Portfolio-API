from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Portfolio API. Navigate to /api/projects/ to see the project list.")
