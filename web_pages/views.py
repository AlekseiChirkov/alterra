from django.shortcuts import render

from web_pages.models import Recommendation


def index(request):
    recommendations = Recommendation.objects.order_by('date')[:7]
    context = {'recommendations': recommendations}
    return render(request, 'web_pages/index.html', context)
