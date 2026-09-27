from django.shortcuts import render
from myapp.models import *

# Create function
def create(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email'],
            profile_image=request.FILES.get('profile_image')
        )
        return redirect('read.html')
    
    return render(request, 'create.html')
