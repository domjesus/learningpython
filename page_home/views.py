
from http.client import HTTPResponse
from django.template import RequestContext
from django.shortcuts import render

def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def index(request):
    # template = Template('{{ title }}: {{ ip_address }}')
    context = RequestContext(request, {
        'title': 'Your IP Address',
    }, [ip_address_processor])
    context2 = {"my_name":"Jose da Silva","ip":ip_address_processor(request)}
    print(context)    
    return render(request,'page_home/index.html', context2)