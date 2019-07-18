from django.shortcuts import render
from .models import Questiontype,Question
from django.http import JsonResponse


def send_code(request):
    id = request.GET.get('id', None)
    QType = Questiontype.objects.get(pk=id)
    qcode = (str)(QType.code)
    qtype = (str)(QType.type)
    qimage = (str)(QType.questionimage)
    qansimage = (str)(QType.answerimage)
    data = {
        'code': qcode,
        'type': qtype,
        'image': qimage,
        'ansimage': qansimage,
    }
    return JsonResponse(data)

def create_quiz(request):
    option_list = Questiontype.objects.only('id')
    return render(request, 'QuizAdmin/MakeQuiz.html', {'name': request.session['name'], 'options': option_list, })
