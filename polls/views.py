from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # get_queryset에서 반환하는 값을 넣는 곳
    # latest_question_list이름으로 index.html에서 사용한다
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions.
        (not including those set to be
        published in the future)"""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     print(question.choice_set)
#     return render(request, 'polls/detail.html', {'question':question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        # POST데이터를 성공적으로 처리 한 후에는 항상 HttpResponseRedirect를 반환해야 한다.
        # reverse() 함수는 뷰 함수에서 url을 하드 코딩하지 않도록 도와준다.
        # 아래는 '/polls/3/results/'와 같은 문자열을 반환한다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
