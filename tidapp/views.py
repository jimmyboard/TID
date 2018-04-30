from django.shortcuts import get_object_or_404, render
from .models import News, Cases
from tidapp.forms import AdvisoryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    latest_news_list = News.objects.order_by('-pub_date')
    latest_cases_list = Cases.objects.order_by('-pub_date')
    return render(request, 'tidapp/index.html', {'latest_news_list': latest_news_list, 'nav': 'index', 'latest_cases_list': latest_cases_list})

def cases(request):
    latest_cases_list = Cases.objects.order_by('-pub_date')
    return render(request, 'tidapp/cases.html', {'latest_cases_list': latest_cases_list, 'nav': 'cases'})

def about(request):
    return render(request, 'tidapp/about.html', {'nav': 'about'})

def services(request):
    return render(request, 'tidapp/services.html', {'nav': 'services'})

def news(request):
    # print request.GET
    # page = int(request.GET["page"])
    # latest_news_list = News.objects.order_by('-pub_date')[(page-1)*5:page*5]
    # return render(request, 'tidapp/news.html', {'latest_news_list': latest_news_list})

    limit = 10
    latest_news_list = News.objects.order_by('-pub_date')

    paginator = Paginator(latest_news_list, limit)

    # print paginator

    page = request.GET.get('page')

    try:
        latest_news_list = paginator.page(page)
    except PageNotAnInteger:
        latest_news_list = paginator.page(1)
    except EmptyPage:
        latest_news_list = paginator.page(paginator.num_pages)

    # print latest_news_list
    # print latest_news_list.paginator
    
    return render(request, 'tidapp/news.html', {'latest_news_list': latest_news_list, 'nav': 'news'})

def contact(request):
    if request.method == 'POST':
        form = AdvisoryForm(request.POST)

        print request.POST

        if form.is_valid():
            form.save(commit=True)
            return success(request)
        else:
            print form.errors
    else:
        form = AdvisoryForm()

    return render(request, 'tidapp/contact.html', {'form': form, 'nav': 'contact'})

def blogs(request, news_id):
    context_dict = {}

    latest_news_list = News.objects.order_by('-pub_date')
    blogs = get_object_or_404(News, pk=news_id)

    context_dict['latest_news_list'] = latest_news_list
    context_dict['blogs'] = blogs

    blogs.views = blogs.views + 1
    blogs.save()

    return render(request, 'tidapp/blogs.html', context_dict)

def design(request):
    latest_news_list = News.objects.filter(news_category='design').order_by('-pub_date')
    return render(request, 'tidapp/news.html', {'latest_news_list': latest_news_list, 'nav': 'news'})

def internet(request):
    latest_news_list = News.objects.filter(news_category='internet').order_by('-pub_date')
    return render(request, 'tidapp/news.html', {'latest_news_list': latest_news_list, 'nav': 'news'})

def success(request):
    return render(request, 'tidapp/success.html')

def work(request, work_id):
    context_dict = {}

    latest_cases_list = Cases.objects.order_by('-pub_date')
    work = get_object_or_404(Cases, pk=work_id)

    limit = 1
    paginator = Paginator(latest_cases_list, limit)

    try:
        latest_cases_list2 = paginator.page(work_id)
    except PageNotAnInteger:
        latest_cases_list2 = paginator.page(1)
    except EmptyPage:
        latest_cases_list2 = paginator.page(paginator.num_pages)

    context_dict['latest_cases_list2'] = latest_cases_list2
    context_dict['latest_cases_list'] = latest_cases_list
    context_dict['work'] = work

    return render(request, 'tidapp/work.html', context_dict)

def uiux(request):
    latest_cases_list = Cases.objects.filter(news_category='uiux').order_by('-pub_date')
    return render(request, 'tidapp/cases.html', {'latest_cases_list': latest_cases_list, 'nav': 'cases'})

def application(request):
    latest_cases_list = Cases.objects.filter(news_category='application').order_by('-pub_date')
    return render(request, 'tidapp/cases.html', {'latest_cases_list': latest_cases_list, 'nav': 'cases'})

def website_design(request):
    latest_cases_list = Cases.objects.filter(news_category='website_design').order_by('-pub_date')
    return render(request, 'tidapp/cases.html', {'latest_cases_list': latest_cases_list, 'nav': 'cases'})
