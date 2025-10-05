from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def projects(request):
    return render(request, 'webapp/projects.html')

def contact(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        print(f"Message from {name} ({email}): {message}")
    return render(request, 'contact.html')