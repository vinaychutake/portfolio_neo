
from django import template

register = template.Library()

# @register.simple_tag(takes_context=True)
# def get_response(context, question):
#     test_attempt = context['test_attempt']
#     try:
#         response  = question.get_response(test_attempt)
#         return response
#     except:
#         return None

@register.filter
def in_category(projects, category):
	print("in template tags!!!!")
	print(projects)
	return projects.filter(category__name=category.name)
