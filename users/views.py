from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from .forms import RegisterForm
from .models import Utilisateur


def login(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username} ! Vous pouvez désormais vous connecter')
            return redirect('login')
    else :
        form = RegisterForm()
    return render(request, 'users/signup.html', {'form':form})


class IndexView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return Utilisateur.objects.all()

class profileDetail(generic.DetailView):
    template_name = 'users/detail.html'
    model = Utilisateur
    slug_field = 'username'
    slug_url_kwarg = 'username'