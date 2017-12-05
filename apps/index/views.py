from django.shortcuts import render
from django.views.generic.base import View
from .models import Feeds


# Create your views here.

class FeedsView(View):
    def get(self, request):
        all_feeds = Feeds.objects.all()
        return render(request, 'index.html', {'all_feeds': all_feeds})
