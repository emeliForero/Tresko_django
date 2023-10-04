from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from task.models import Workspace
# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    professional = Account.objects.all().count()
    user_login = request.user.id
    workspaces = Workspace.objects.all().filter(user_create=user_login)
    context ={
        'professional' : professional,
        'workspaces' : workspaces,
    }
    return render(request, 'homepage/dashboard.html', context)