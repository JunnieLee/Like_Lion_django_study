from django.shortcuts import render
from .models import Feed  # 추가. (참고: .models == feeds.models)
from django.shortcuts import redirect

def index(request):
    if request.method == 'GET': # 목록 조회
        feeds = Feed.objects.all()
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST': # create
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')
