from django.views import View
from django.http import HttpResponse

class MyView(View):
    def get(self, request):
        return HttpResponse('Welecome to library book page')
    