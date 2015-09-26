__author__ = 'rt'

from django.shortcuts import *
from django.template import *

def home(request):

    pageTitle="Blah Blah"
    cont = Context({'pageTitle':pageTitle})
    html = render_to_response('beta_test.html',cont)
    return html
