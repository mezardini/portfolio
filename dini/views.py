from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    # visitor_ip = request.META.get('REMOTE_ADDR')
    # send_mail(
    #         'New Visitor',
    #         'A visitor ' + visitor_ip + ' has been on your portfolio website',
    #         'settings.EMAIL_HOST_USER',
    #         ['mezardini@gmail.com'],
    #         fail_silently=False,
    #     )
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        sender = request.POST['name']
        body = request.POST['body']
        send_mail(
            subject,
            email + sender + body,
            'settings.EMAIL_HOST_USER',
            ['mezardini@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'mezard.html')