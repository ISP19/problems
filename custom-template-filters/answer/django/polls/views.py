from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib import messages

from .models import Choice, Question


def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def reset_index(request):
    all_question_list = Question.objects.all()
    context = {'all_question_list': all_question_list}
    return render(request, 'polls/reset_polls.html', context)


def reset(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.reset_votes()
    messages.success(request, f'Reset votes for Poll \"{question.question_text}"')
    return HttpResponseRedirect(reverse('polls:reset_index'))