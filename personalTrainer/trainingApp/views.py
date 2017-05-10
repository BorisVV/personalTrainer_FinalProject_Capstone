from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from personalTrainer import settings

from django.shortcuts import render_to_response

from .models import Client, WeightIn, WorkOutSchedule

from chartit import DataPool, Chart

def home(request):
    ''' Home page same as Index page'''
    num_of_clients = Client.objects.all().count()
    num_of_workouts = WorkOutSchedule.objects.all().count()
    return render(request, 'trainingApp/home.html',
    context={'num_of_clients': num_of_clients, 'num_of_workouts': num_of_workouts})


class ClientsListView(generic.ListView):
    # Display the clients list.
    template_name = 'trainingApp/clients.html'
    context_object_name = 'list_of_clients'

    def get_queryset(self):
        """Return all the objects in the clients table."""
        return Client.objects.order_by('first_name')

class ClientsDetailView(generic.DetailView):
    # WeightIns details
    model = Client
    template_name = 'trainingApp/clientWeightIns.html'

class ClientsWorkOutSchdListView(generic.ListView):
    template_name = 'trainingApp/all_WOSchedules.html'
    context_object_name = 'list_of_WOSchedules'

    def get_queryset(self):
        return WorkOutSchedule.objects.order_by('date_WO')

class ClientWorkOutSchdDetail(generic.DetailView):
    model = Client
    template_name = 'trainingApp/clientWorkOutSchd.html'

# def line(request, name_of_client):
#     ds = DataPool(
#        series=
#         [{'options': {
#             'source': Client.objects.get(pk=name_of_client)},
#           'terms': [
#             'date_weighted',
#             'weight_today']}
#          ])
#
#     cht = Chart(
#             datasource = ds,
#             series_options =
#               [{'options':{
#                   'type': 'line',
#                   'stacking': False},
#                 'terms':{
#                   'date_weighted': [
#                     'weight_today']}
#                 }],
#             chart_options =
#               {'title': {
#                    'text': 'The chart for the client'},
#                'xAxis': {
#                     'title': {
#                        'text': 'date_weighted'}}})
#
#     return render_to_response('trainingApp/clientWeightIns.html', {'weightChart':cht})

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
