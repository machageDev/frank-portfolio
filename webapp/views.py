from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request, 'projects.html')




def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Prepare email content
        subject = f"Portfolio Contact Message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_list = ['machagefranklyn@gmail.com']  

        try:
            send_mail(subject, body, email, recipient_list)
            messages.success(request, "Message sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending email: {e}")

    return render(request, 'contact.html')
