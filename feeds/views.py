from django.shortcuts import render
from .models import Feed  # 추가. (참고: .models == feeds.models)

def index(request):
    feeds = Feed.objects.all()
    return render(request, 'feeds/index.html', {'feeds': feeds})
