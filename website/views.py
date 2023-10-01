from django.shortcuts import render
from siteadmin.models import news, socialmedia, category, herosection
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Subquery, OuterRef, F
from django.db import connections
from django.template import *


def CreateCategory():
    category_list = ['राष्ट्रीय', 'आंतरराष्ट्रीय', 'राजकिय', 'सामाजिक', 'आरोग्य', 'साहित्य', 'युवा',
                     'कला', 'क्रिडा', 'मार्केट', 'गृहेगरी', 'नोकरी', 'कृषीवर्ता', 'आरोग्य व शिक्षण', ' क्रीडा व मनोरंजन']
    # all_tables = connection.introspection.table_names()
    # if category in all_tables:
    for i in range(len(category_list)):
        inserval = category(category=category_list[i])
        inserval.save()


def index(request):
    get_disticut = category.objects.values_list('id').distinct()
    out = [item for t in get_disticut for item in t]
    return render(request, 'website/index.html', {'heorsection': herosection.objects.all().order_by('-date').first,
                                                  'national': news.objects.filter(category_id=out[0]).order_by('-date').first(),
                                                  'international': news.objects.filter(category_id=out[1]).order_by('-date').first(),
                                                  'political': news.objects.filter(category_id=out[2]).order_by('-date').first(),
                                                  'social': news.objects.filter(category_id=out[3]).order_by('-date').first(),
                                                  'health': news.objects.filter(category_id=out[4]).order_by('-date').first(),
                                                  'literature': news.objects.filter(category_id=out[5]).order_by('-date').first(),
                                                  'youth': news.objects.filter(category_id=out[6]).order_by('-date').first(),
                                                  'art': news.objects.filter(category_id=out[7]).order_by('-date').first(),
                                                  'sports': news.objects.filter(category_id=out[9]).order_by('-date').first(),
                                                  'market': news.objects.filter(category_id=out[10]).order_by('-date').first(),
                                                  'housing': news.objects.filter(category_id=out[11]).order_by('-date').first(),
                                                  'jobs': news.objects.filter(category_id=out[12]).order_by('-date').first(),
                                                  'agriculture': news.objects.filter(category_id=out[13]).order_by('-date').first(),
                                                  'healthandeducation': news.objects.filter(category_id=out[14]).order_by('-date').first(),
                                                  'sportsandentertainment': news.objects.filter(category_id=out[14]).order_by('-date').first(),
                                                  'category_list_desktop': category.objects.all()[0:6],
                                                  'category_list_mobile': category.objects.all()})


def showcat(request, category):
    showcat = news.objects.select_related('category').filter(category=category).order_by('-date')
    page = Paginator(showcat, 12)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    # return HttpResponse('<h1>Hello HttpResponse</h1>')
    return render(request, 'website/showcat.html', context)


def read(request, id):
    return render(request, 'website/read.html', {'readdata': news.objects.filter(id=id), 'category_list_desktop': category.objects.all()[0:6],
                                                 'category_list_mobile': category.objects.all(),"siteurl":'www.spnewsmarathi.co.in'})


def heroread(request, id):
    return render(request, 'website/heroread.html', {'hreaddata': herosection.objects.filter(id=id)})


# CreateCategory()
