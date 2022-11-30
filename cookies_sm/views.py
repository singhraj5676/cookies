from django.shortcuts import render

# Create your views here.
def count(request):
    if 'count' in request.COOKIES:
        newcount = int(request.COOKIES['count'])+1
    else:
            newcount = 1
    response = render(request, 'cookies_sm/index.htm',{'count': newcount})
    # response.set_cookie('count', newcount)
    response.set_cookie('count', newcount, 60)
    response.set_cookie('count', newcount, max_age = 60)
    return response
