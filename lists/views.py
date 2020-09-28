from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Exercise One - Static Web Page</title><h1 style="text-align: center;">Welcome to unlikely documents</h1><p style="padding-left: 30px;">This static web page is meant to fulfill exercise one of PMPL</p><p style="padding-left: 30px;">Ken Reinhart 2006507012</p></html>')