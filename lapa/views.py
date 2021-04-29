from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render

# Create your views here.
from kafe import settings
from lapa.forms import OstavitOtzivForm
from lapa.models import Tovar, Otzivi, TipTovara


def render_page_home(request, alert=None):
    tovar_iz_topa = Tovar.objects.order_by('kolvo_dobavlenia_v_korzinu')[0:7]
    return render(request, 'lapa/home.html', {
        'tovar_iz_topa': tovar_iz_topa,
        'alert': alert
    })


def render_page_tovar_lv(request, vid):

    tovar = Tovar.objects.order_by('kolvo_dobavlenia_v_korzinu')
    tip_tovara = TipTovara.objects.filter(id=vid)


    return render(request, 'lapa/tovar_lv.html', {
        'tovar': tovar,
        'tip_tovara': tip_tovara,
        'vid': vid
    })


def ostavit_otziv(request):

    otzivi = Otzivi.objects.filter(prosli_moderaziu=True).order_by('data_otziva')
    # otzivi = Otzivi.objects.order_by('data_otziva')

    forma_ostavit_otziv = OstavitOtzivForm()

    if request.method == "POST":
        form = OstavitOtzivForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            # post.save()
            form.save(commit=True)

            # mail_title = 'Test Email'
            # message = 'This is a test email.'
            # email = settings.DEFAULT_FROM_EMAIL
            # recipients = ['lapa@gmail.com',]
            #
            # try:
            #     send_mail(mail_title, message, email, recipients, settings.EMAIL_HOST_USER,
            #               settings.EMAIL_HOST_PASSWORD)
            return render(request,'lapa/ostavit_otziv.html', {
        'otzivi': otzivi,
        'forma_ostavit_otziv': forma_ostavit_otziv
    })




        else:
            return render(request, 'lapa/ostavit_otziv.html', {
                'otzivi': otzivi,
                'forma_ostavit_otziv': forma_ostavit_otziv
            })
    else:
        return render(request, 'lapa/ostavit_otziv.html', {
            'otzivi': otzivi,
            'forma_ostavit_otziv': forma_ostavit_otziv
        })

def basket_do(request, alert = None):
    return render(request, 'lapa/basket.html', {
        'alert': alert
    })
