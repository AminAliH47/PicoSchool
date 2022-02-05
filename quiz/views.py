import random
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from main.decorators import (
    allow_user,
    quiz_access,
)
from main.mixins import AllowUserMixin
from manager.filters import QuizListFilter
from quiz.filters import QuizResultFilter
from quiz.forms import (
    CreateQuestionForm,
    CreateQuizForm,
    UpdateQuestionForm,
    UpdateQuizForm,
)
from quiz.models import (
    Quiz,
    QuizQuestion,
    QuizDescAnswers,
    QuizMultipleAnswers,
    QuizResult,
)


@login_required()
@allow_user(['is_superuser', 'is_manager', 'is_student', 'is_teacher'])
def quiz_list(request):
    if request.method == "POST":
        if request.is_ajax:
            id = request.POST['id']
            print(id)
            QuizQuestion.objects.get(id=id).delete()

    context = {
        'page_title': 'فهرست آزمون ها'
    }
    if request.user.is_superuser or request.user.is_manager:
        context['filter'] = QuizListFilter(request.GET, queryset=Quiz.objects.all())
    if request.user.is_student:
        context['filter'] = QuizListFilter(request.GET,
                                           queryset=Quiz.objects.filter(quiz_class=request.user.student_class))
    if request.user.is_teacher:
        context['filter'] = QuizListFilter(request.GET,
                                           queryset=Quiz.objects.filter(quiz_class__teacher__pk=request.user.pk))
    return render(request, "quiz/quiz_list.html", context)


@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    context = {
        'page_title': f" آزمون {quiz.name}",
        'quiz': quiz,
    }
    return render(request, "quiz/quiz_detail.html", context)


@allow_user(['is_superuser', 'is_manager'])
def quiz_questions_list(request, pk):
    questions = QuizQuestion.objects.filter(quiz__pk=pk)
    quiz = Quiz.objects.get(pk=pk)
    if request.method == "POST":
        if request.is_ajax:
            input_value = {
                'qus_id': request.POST['qus_id'],
                'quiz_id': request.POST['quiz_id'],
                'question_type': request.POST['question_type'],
                'question_text': request.POST['question_text'],
            }
            print(input_value)
            if input_value['question_type'] == 'تشریحی':
                qus = QuizQuestion(id=input_value['qus_id'], text=input_value['question_text'],
                                   quiz=Quiz.objects.get(id=input_value['quiz_id']),
                                   question_type=input_value['question_type'])
                qus.save()
                ans = QuizDescAnswers(question=QuizQuestion.objects.get(id=input_value['qus_id']))
                ans.save()
            elif input_value['question_type'] == 'چهار گزینه ای':
                qus = QuizQuestion(id=input_value['qus_id'], text=input_value['question_text'],
                                   quiz=Quiz.objects.get(id=input_value['quiz_id']),
                                   question_type=input_value['question_type'])
                qus.save()
    context = {
        'page_title': 'فهرست سوالات',
        'questions': questions,
        'quiz': quiz,
        'form': CreateQuestionForm(),
        'edit_form': UpdateQuestionForm(),
        'answers': range(4)
    }
    return render(request, "quiz/quiz_list.html", context)


@allow_user(['is_superuser', 'is_manager'])
def create_answers(request):
    input_value = {
        'qus_id': request.POST['qus_id'],
        'answer_text': request.POST['answer_text'],
        'correct': request.POST['correct'],
    }

    if input_value['correct'] == 'true':
        correct = True
    else:
        correct = False
    print(input_value)
    ans = QuizMultipleAnswers(text=input_value['answer_text'], correct=correct,
                              question=QuizQuestion.objects.get(id=input_value['qus_id']))
    ans.save()
    return HttpResponse(input_value)


class UpdateQuestion(AllowUserMixin, generic.UpdateView):
    model = QuizQuestion
    form_class = UpdateQuestionForm
    template_name = 'quiz/quiz_create.html'
    success_url = reverse_lazy('quiz:quiz_list')
    allowed_users = ['is_superuser', 'is_manager']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "ویرایش آزمون"
        context['question'] = QuizQuestion.objects.get(id=self.kwargs['pk'])
        return context


@allow_user(['is_superuser', 'is_manager'])
def update_question(request):
    input_value = {
        'qus_id': request.POST['qus_id'],
        'question_text': request.POST['question_text'],
    }
    print(input_value)
    QuizQuestion.objects.filter(id=input_value['qus_id']).update(text=input_value['question_text'])
    return HttpResponse(input_value)


@allow_user(['is_superuser', 'is_manager'])
def update_answers(request):
    input_value = {
        'answer_id': request.POST['answer_id'],
        'answer_text': request.POST['answer_text'],
        'correct': request.POST['correct'],
    }
    print(input_value)
    if input_value['correct'] == 'true':
        correct = True
    else:
        correct = False
    QuizMultipleAnswers.objects.filter(id=input_value['answer_id']).update(text=input_value['answer_text'],
                                                                           correct=correct)
    return HttpResponse(input_value)


class CreateQuiz(AllowUserMixin, generic.CreateView):
    form_class = CreateQuizForm
    template_name = 'quiz/quiz_create.html'
    allowed_users = ['is_superuser', 'is_manager']
    success_url = reverse_lazy("quiz:quiz_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "ساخت آزمون"
        return context


class UpdateQuiz(AllowUserMixin, generic.UpdateView):
    model = Quiz
    form_class = UpdateQuizForm
    template_name = 'quiz/quiz_create.html'
    allowed_users = ['is_superuser', 'is_manager']

    def get_success_url(self):
        return reverse_lazy('quiz:quiz_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "ویرایش آزمون"
        return context


qus_ids = []

answers = []


@quiz_access()
@allow_user(['is_student'])
def quiz_start(request, pk, uuid):
    quiz = get_object_or_404(Quiz, pk=pk, uuid=uuid)
    questions = quiz.questions()
    if request.method == "POST":
        if request.is_ajax():
            qus_type = request.POST['type']
            if qus_type == "تشریحی":
                input_value = {
                    'id': request.POST['id'],
                    'type': request.POST['type'],
                    'answer_text': request.POST['answer_test'],
                }
                qus_id = input_value['id']
                if qus_id in qus_ids:
                    print(qus_id)
                else:
                    qus_ids.append(qus_id)
                    answers.append(input_value)
            elif qus_type == "چهار گزینه ای":
                input_value = {
                    'id': request.POST['id'],
                    'type': request.POST['type'],
                    'correct': request.POST['correct'],
                }
                qus_id = input_value['id']
                if qus_id in qus_ids:
                    print(qus_id)
                else:
                    qus_ids.append(qus_id)
                    answers.append(input_value)
    print(qus_ids)
    print(answers)
    quiz.students.add(request.user)
    quiz.save()
    context = {
        'quiz': quiz,
    }

    if quiz.show_quiz:
        if not request.session.get('random_exp'):
            request.session['random_exp'] = random.randrange(0, 5)
        object_list = cache.get('random_exp_%d' % request.session['random_exp'])
        if not object_list:
            object_list = list(quiz.questions().order_by('?'))
            cache.set('random_exp_%d' % request.session['random_exp'], object_list, 6000)
        paginator = Paginator(object_list, 1)
        page_number = request.GET.get('qus')
        display_list = paginator.page(page_number)
        context['questions'] = display_list
    else:
        display_list = questions.order_by('?')
        context['questions'] = display_list

    return render(request, "quiz/quiz_list.html", context)


@require_POST
def get_questions(request):
    """
    Get Questions when quiz show answers True
    """
    qus_type = request.POST['type']
    if qus_type == "تشریحی":
        input_value = {
            'id': request.POST['id'],
            'type': request.POST['type'],
            'answer_text': request.POST['answer_text'],
        }
        qus_id = input_value['id']
        if qus_id in qus_ids:
            answers.append(input_value)
            for i in range(len(answers)):
                if answers[i]['id'] == qus_id:
                    del answers[i]
                    break
        else:
            qus_ids.append(qus_id)
            answers.append(input_value)
    elif qus_type == "چهار گزینه ای":
        input_value = {
            'id': request.POST['id'],
            'type': request.POST['type'],
            'correct': request.POST['correct'],
        }
        qus_id = input_value['id']
        if qus_id in qus_ids:
            answers.append(input_value)
            for i in range(len(answers)):
                if answers[i]['id'] == qus_id:
                    del answers[i]
                    break
        else:
            qus_ids.append(qus_id)
            answers.append(input_value)
    print(answers)
    return HttpResponse("done")


@require_POST
def create_result(request):
    """
    Create result for main Quiz
    """
    quiz_data = {
        'uuid': request.POST['uuid'],
        'pk': request.POST['pk'],
    }
    quiz = get_object_or_404(Quiz, pk=quiz_data['pk'], uuid=quiz_data['uuid'])
    qus_type = request.POST['type']
    if qus_type == "تشریحی":
        input_value = {
            'id': request.POST['id'],
            'type': request.POST['type'],
            'answer_text': request.POST['answer_test'],
        }
        qus_id = input_value['id']
        if qus_id in qus_ids:
            print(qus_id)
        else:
            qus_ids.append(qus_id)
            answers.append(input_value)
    elif qus_type == "چهار گزینه ای":
        input_value = {
            'id': request.POST['id'],
            'type': request.POST['type'],
            'correct': request.POST['correct'],
        }
        qus_id = input_value['id']
        if qus_id in qus_ids:
            print(qus_id)
        else:
            qus_ids.append(qus_id)
            answers.append(input_value)
    QuizResult.objects.create(quiz=quiz, user=request.user, data=answers)
    qus_ids.clear()
    answers.clear()
    return HttpResponse("Done")


@require_POST
def create_result_2(request):
    quiz_data = {
        'uuid': request.POST['uuid'],
        'pk': request.POST['pk'],
    }
    quiz = get_object_or_404(Quiz, pk=quiz_data['pk'], uuid=quiz_data['uuid'])
    QuizResult.objects.create(quiz=quiz, user=request.user, data=answers)
    qus_ids.clear()
    answers.clear()
    return HttpResponse("Done")


def answers_data(request):
    if answers:
        return JsonResponse(answers, safe=False)
    else:
        return JsonResponse({})


@allow_user(['is_superuser', 'is_manager', 'is_teacher', 'is_student'])
def result_list(request):
    context = {
        'page_title': 'فهرست نتایج آزمون',
    }
    if request.user.is_superuser:
        context['filter'] = QuizResultFilter(request.GET, queryset=QuizResult.objects.all())
    elif request.user.is_student:
        context['filter'] = QuizResultFilter(request.GET, queryset=QuizResult.objects.filter(
            user=request.user))
    elif request.user.is_teacher:
        context['filter'] = QuizResultFilter(request.GET, queryset=QuizResult.objects.filter(
            quiz__quiz_class__teacher__pk=request.user.pk))
    return render(request, "quiz/quiz_list.html", context)


@allow_user(['is_superuser', 'is_manager', 'is_teacher', 'is_student'])
def result_detail(request, pk, stu_pk):
    result = get_object_or_404(QuizResult, pk=pk, user__pk=stu_pk)
    context = {
        'page_title': 'جزئیات آزمون',
        'result': result,
        'questions': QuizQuestion.objects.filter(quiz=result.quiz)
    }
    return render(request, "quiz/quiz_detail.html", context)


# This Return Data from Student Result
def result_data(request, pk):
    result = get_object_or_404(QuizResult, pk=pk)
    return JsonResponse({"data": result.data})
