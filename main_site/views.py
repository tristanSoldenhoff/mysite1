from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Skill

def index(request):
    latest_skill_list = Skill.objects.order_by('-language')[:5]
    template = loader.get_template('main_site/index.html')
    context = {'latest_skill_list': latest_skill_list}
    return render(request, 'main_site/index.html', context)
    # return HttpResponse("""Code running from main_site/views.py def index() \n...
    # - Will map this def to a URL so that it can be called. \n...
    # URL is created in main_site/urls.py \n...
    # URL is finally collected on mysite/urls   urlpatterns = [] \n...""")

def detail(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    return render(request, 'main_site/detail.html', {'skill':skill})
    # return HttpResponse("Type in http://localhost:8000/main_site/3/ to get onto this page. This is from views.py def detail - skill number %s." % skill_id)

def results(request, skill_id):
    response = "Type in http://localhost:8000/main_site/333/results/ to get onto this page. This is from def results %s"
    return HttpResponse(response % skill_id)
