from django.shortcuts import render
from .models import Questiontype
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
    name = ''
    try:
        if request.session['name'] == None or request.session['name'] == '':
            name = ''
        else:
            name = request.session['name']
    except:
        print('Name Error')
    finally:
        return render(request, 'QuizAdmin/MakeQuiz.html', {'name': name, 'options': option_list, })
