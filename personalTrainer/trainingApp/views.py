from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Question, Client, WeightIn, Choice


def home(request):
    return render(request, 'trainingApp/home.html')

class ClientsListView(generic.ListView):
    template_name = 'trainingApp/clients.html'
    context_object_name = 'list_of_clients'

    def get_queryset(self):
        """Return all the objects in the clients table."""
        return Client.objects.order_by('first_name')

class ClientsDetailView(generic.DetailView):
    model = Client
    template_name = 'trainingApp/clientDetails.html'

# def weights(request, client_id):
#     client_name = get_object_or_404(Client, pk=client_id)
    # return render(request, 'trainingApp/clientsDetail.html', {'client_name': client_name})
    # return HttpResponseRedirect(reverse('trainingApp:clientsDetail.html', args=(client_name.id,)))
    # display_weights = pk=request.POST['weight_today', 'date_weighted'])


class IndexView(generic.ListView):
    template_name = 'trainingApp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'trainingApp/detail.html'



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'trainingApp/results.html'


def stars(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question form.
        return render(request, 'trainingApp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.option_Stars += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('trainingApp:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'trainingApp/results.html', {'question': question})
