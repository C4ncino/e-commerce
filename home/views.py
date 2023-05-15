from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        try:
            user_group = request.user.groups.all()[0].name
        except:
            user_group = ''
        context = {'user_group' : user_group}
        return render(request, 'index.html', context)