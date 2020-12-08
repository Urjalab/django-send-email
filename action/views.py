from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def index(request):

    context = {}

    if request.method == 'POST':

        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        response = send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        context['response'] = response


    return render(
        request,
        'action/index.html',
        context
    )
