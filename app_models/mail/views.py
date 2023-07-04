from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

@login_required
def send_email_to_user(request):
    if request.method == 'POST':
        subject = 'Hello, {}'.format(request.user.username)
        message = 'This is a test email sent to you, {}'.format(request.user.username)
        from_email = 'demoemail@gmail.com'  
        recipient_list = [request.user.email]

        send_mail(subject, message, from_email, recipient_list)
        return redirect('email_sent')

    return render(request, 'send_email.html')

def email_sent(request):
    return render(request, 'email_sent.html')
# your_email@example.com