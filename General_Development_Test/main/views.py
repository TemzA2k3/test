from django.shortcuts import render, redirect
from .models import Questions


def index(request):
    return render(request, 'main/main.html')


def question(request, question_id):
    if question_id < 11:
        q = Questions.objects.filter(id=question_id)
    answer = getAnswer(request)
    if type(answer) is not type(None):
        if not answer or not answer.isdigit():
            q = Questions.objects.filter(id=question_id-1)
            return render(request, "main/questions.html", {'quest': q, 'validation': True})
        q2 = Questions.objects.filter(id=question_id - 1)
        if int(answer) == int(q2[0].rightAnswer):
            if request.session.get("mark") is None:
                request.session["mark"] = '0'
            request.session["mark"] = int(request.session.get("mark")) + 1
        if check_action(request) == 'cont_test':
            return render(request, 'main/questions.html', {'quest': q, 'validation':False})
        else:
            return redirect('res')
    return render(request, 'main/questions.html', {'quest': q, 'validation': False})


def check_action(request):
    action = request.POST.get("action")
    return action


def about(request):
    return render(request, 'main/about.html')


def about_project(request):
    return render(request, 'main/about_project.html')


def getAnswer(request):
    user_data = request.POST.dict()
    answer = user_data.get("answer_field")
    return answer


def results(request):
    result = {'value': request.session.get("mark")}
    request.session["mark"] = None
    return render(request, 'main/finish_test.html', {'result': result})


def rules(request):
    return render(request, 'main/rules.html')
