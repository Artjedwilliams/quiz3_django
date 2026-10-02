from django.shortcuts import render
from django.core.paginator import Paginator  # <-- Import the Paginator
from .models import Student

def welcome(request):
    return render(request, 'main/welcome.html')

def home(request):
    # Fetch all records ordered by creation date
    student_list = Student.objects.all().order_by('-created_at')
    
    # Restrict to 10 students per page split matrix
    paginator = Paginator(student_list, 10) 
    
    # Extract active target index page parameters from URL request context
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    
    return render(request, 'main/home.html', {'students': students})

