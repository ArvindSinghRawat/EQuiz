from django.shortcuts import render


def create_quiz(request):
    return render(request, 'QuizAdmin/MakeQuiz.html', {'name': request.session['name'], })