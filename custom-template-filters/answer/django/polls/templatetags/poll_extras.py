from django import template

register = template.Library()


@register.filter
def latest_question(questions):
    """ Return 5 latest questions by using custom template filter"""
    return questions.order_by('-pub_date')[:5]
