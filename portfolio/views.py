from django.template import RequestContext
from django.views.generic import View
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_object_or_404

from portfolio import models

# Create your views here.
class IndexView(View):
    """
    """
    def get(self, request):
        projects = models.Project.objects.filter(is_active=True)
        tech_list = models.Technology.objects.all()
        data = {'projects': projects, 'tech_list': tech_list}
        return render(request, 'pages/index.html', data)

class ProjectDetailsView(View):
    """
    """

    def get(self, request, pid):

        project = get_object_or_404(models.Project, **{'id': pid})
        return render(request, "pages/project_details.html", {'project': project})

class PortfolioView(View):
    """
    """
    def get(self, request):
        projects = models.Project.objects.filter(is_active=True)
        categories = models.Category.objects.all()
        data = {'projects': projects, 'categories': categories}
        return render(request, 'pages/portfolio.html', data)

