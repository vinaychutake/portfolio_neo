from django.template import RequestContext
from django.views.generic import View
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_object_or_404

from portfolio.models import Project, Technology, Category
from zinnia.models import entry

# Create your views here.
class IndexView(View):
    """
    """
    def get(self, request):
        projects = Project.objects.filter(is_active=True)
        tech_list = Technology.objects.all()
        categories = Category.objects.all()
        category_list = []
        category_name_list = []

        for category in categories:
            category_list.append(category.projects.count())
            category_name_list.append(str(category.name))

        blog_entries = entry.Entry.objects.filter(status=2)[:3]

        data = { 'projects': projects, 'tech_list': tech_list, 'categories':categories, 
                'category_list': category_list,'category_name_list':category_name_list,
                'blog_entries':blog_entries }
        return render(request, 'pages/index.html', data)

class ProjectDetailsView(View):
    """
    """

    def get(self, request, pid):

        project = get_object_or_404(Project, **{'id': pid})
        return render(request, "pages/project_details.html", {'project': project})

class PortfolioView(View):
    """
    """
    def get(self, request):
        projects = Project.objects.filter(is_active=True)
        categories = Category.objects.all()
        data = {'projects': projects, 'categories': categories}
        return render(request, 'pages/portfolio.html', data)

