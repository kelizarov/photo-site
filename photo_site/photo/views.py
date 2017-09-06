from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import PhotoUser
from .forms import SignUpForm
# Create your views here.

class IndexView(View):
    template_name = 'photo/index.html'

    def get(self, request):
        return render(request, self.template_name)

class SignUpView(View):
    template_name = 'photo/signup.html'
    form_class = SignUpForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})
