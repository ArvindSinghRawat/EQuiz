from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('EQuiz/main.html')
    context = {}
    return HttpResponse(template.render(context,request))

def signup(request):
    template = loader.get_template('EQuiz/Form.html')
    context = {}
    return HttpResponse(template.render(context,request))