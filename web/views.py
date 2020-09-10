from django.shortcuts import render
# from .models import Class_1, Class_2


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

"""
def news(request):
    if request.method == 'GET':
        try:
            articles = Article.objects.all()
        except:
            articles = None
        return render(request, 'news.html', {'articles': articles})

def article(request, slug):
    if request.method == 'GET':
        try:
            articolo = Article.objects.get(slug=slug)
        except:
            articolo = None
        return render(request, 'article.html', {'articolo': articolo})
"""


# ReCaptcha conf
"""
import requests
import json

def captcha(request):
    secretKey = settings.RECAPTCHA_PRIVATE_KEY
    clientKey = request.POST['g-recaptcha-response']
    captchaData = {
        'secret': secretKey,
        'response': clientKey
    }
    try:
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify_status = response['success']
    except:
        verify_status = 'fail'
    return verify_status
"""

# E-mail conf
"""
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

def send_email(oggetto, messaggio, nome, email):
    superusers_emails = [i[0] for i in User.objects.filter(is_superuser=True).values_list('email')]
    # allusers_emails = [i[0] for i in User.objects.values_list('email')]
    send_mail(oggetto, f'''Messaggio da {nome}.
                        \n{messaggio}
                        \nRispondere all'indirizzo {email}''', settings.EMAIL_HOST_USER, superusers_emails)
    return None
"""