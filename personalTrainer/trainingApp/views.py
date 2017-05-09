from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from personalTrainer import settings

from .models import Client, WeightIn

def home(request):
    return render(request, 'trainingApp/home.html')

def user_profile(request, user_pk):

    user = User.objects.get(pk=user_pk)
    weights = WeightIn.objects.filter(
        user=user.pk).order_by('date_weighted').reverse()

    return render(request, 'trainingApp/clientDetails.html',
                  {'user': user, 'history': weights})


class ClientsListView(generic.ListView):
    template_name = 'trainingApp/clients.html'
    context_object_name = 'list_of_clients'

    def get_queryset(self):
        """Return all the objects in the clients table."""
        return Client.objects.order_by('first_name')

class ClientsDetailView(generic.DetailView):
    model = Client
    template_name = 'trainingApp/clientDetails.html'


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('trainingApp/home')
#         else:
#             form = SignUpForm()
#             return render(request, 'trainingApp/signup.html', {'form': form})
#
# def login(request):
#     next = request.GET.get('next', '/home/')
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return HttpResponseRedirect(next)
#         else:
#             return HttpResponse("Account is not active at the moment.")
#         else:
#             return HttpResponseRedirect(settings.LOGIN_URL)
#             return render(request, "trainingApp/login.html", {'next': next})
