from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.




def regi(request):
    ufo=UserForm()
    pfo=profileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST'and request.FILES:
        ufod=UserForm(request.POST)
        pfod=profileForm(request.POST,request.FILES)
        if ufod.is_valid() and pfod.is_valid():
            nsufo=ufod.save(commit=False)
            submittedpassword=ufod.cleaned_data['password']
            nsufo.set_password(submittedpassword)
            nsufo.save()
            nspfo=pfod.save(commit=False)
            nspfo.username=nsufo
            nspfo.save()
            send_mail('Registration',
                      'Hi How R u',
                      'gvasu1125@gmail.com',
                      [nsufo.email],
                      fail_silently=False)
            return HttpResponse('registration is successful')
    return render(request,'form.html',d)