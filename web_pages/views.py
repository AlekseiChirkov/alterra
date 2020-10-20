from django.http import HttpResponseRedirect
from django.shortcuts import render

from web_pages.models import Recommendation
from web_pages.forms import RequestForm


def index(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RequestForm()
        recommendations = Recommendation.objects.order_by('date')[:9]
        context = {
            'recommendations': recommendations,
            'form': form,
        }
        return render(request, 'web_pages/index.html', context)
    recommendations = Recommendation.objects.order_by('date')[:9]
    context = {
        'recommendations': recommendations,
        'form': form,
    }
    return render(request, 'web_pages/index.html', context)