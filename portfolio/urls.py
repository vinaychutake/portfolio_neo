from django.conf.urls import url

from portfolio.views import IndexView, ProjectDetailsView, PortfolioView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^portfolio/$', PortfolioView.as_view(), name='portfolio'),
    url(r'^projects/(?P<pid>[0-9]+)/$', ProjectDetailsView.as_view(), name='project_details'),
]