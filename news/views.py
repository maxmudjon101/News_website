from django.shortcuts import render ,get_object_or_404
from .models import News
# Create your views here.
def HomeView(request):
    latest_new=News.published.order_by('-id').first()
    news=News.published.order_by('-id')[:5]
    sport_news=News.published.filter(category__name="Sport")
    texnalogiya_news=News.published.filter(category__name="texnalogiya")
    xorich_news=News.published.filter(category__name="xorich")
    mahali_news=News.published.filter(category__name="mahaliy")
    context={
        "latest_new":latest_new,
        "news":news,
        "sport_news":sport_news,
        "texnalogiya_news":texnalogiya_news,
        "xorich_news":xorich_news,
        "mahali_news":mahali_news

    }
    return render(request,'index.html',context)


def DeteilNew(request,slug):
    news=get_object_or_404(News,slug=slug)
    context={
        "news":news
    }
    return render(request,"single-page.html",context)


def aloqa(request):
    return render(request,'contact.html')















































































































