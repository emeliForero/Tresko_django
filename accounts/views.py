from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserCreateForm, UserProfileCreateForm, UserForm, UserProfileForm
from accounts.models import *
from task.models import Workspace
# Create your views here.


def login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Inicio de sesion correcto')
            return redirect('dashboard')
        else:
            messages.error(request, 'Las credenciales son incorrectas')
            return redirect('login')
        
    return render (request, 'account/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Has salido de sesion')
    
    return redirect('login')

def create_account(request):
        user_create = UserCreateForm(request.POST)
        profile_create = UserProfileCreateForm(request.POST, request.FILES)
        if request.method == 'POST':
            if user_create.is_valid() and profile_create.is_valid():
                password = user_create.cleaned_data['password']
                email = user_create.cleaned_data['email']
                user_created = user_create.save(commit=False)
                username = Account.objects.generate_username(user_created.first_name, user_created.last_name)
                user_created.username = username
                user_created.emai = Account.objects.normalize_email(email)
                user_created.set_password(password)
                user_created.save()
                
                photo = profile_create.cleaned_data['photo']
                print(photo)
                if not photo:
                    photo = 'default/profile.png'
                    print('1', photo)
                
                profile = profile_create.save(commit=False)
                profile.user = user_created
                profile.photo =  photo
                profile.save()
                messages.success(request, 'cuenta creado correctamente')
                return redirect('login')
            else:
                print('error')
                messages.error(request, user_create.errors)
                messages.error(request, profile_create.errors)
        context = {
                'user_create': user_create,
                'profile_create': profile_create,
            }
        
        return render (request, 'account/create_account.html', context)
   

@login_required(login_url='login')
def list_accounts(request):
        
        professionals = Account.objects.all()
    
        context = {
            'professionals' : professionals,
        }
        
        return render(request, 'account/list_account.html', context)
    
        

@login_required(login_url='login')
def update_account(request, user_id):

        user_read = get_object_or_404(Account, id=user_id)
        workspaces = Workspace.objects.all().filter(user_create=user_read)
        profile_read = get_object_or_404(UserProfile, user=user_read)
        user_session = get_object_or_404(Account, id=request.user.id)
        
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=user_read)
            
            if user_read == user_session:
                profile_form = UserProfileForm(request.POST, request.FILES, instance=profile_read)
            else:
                profile_form = UserProfileCreateForm(request.POST, request.FILES, instance=profile_read)
                    
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile_form.save()
                username = user.first_name.title() + ' ' + user.last_name.title()
                user.username = username
                user.save()
                messages.success(request, 'cuenta editado correctamente')       
                
                return redirect ('view_account', user_id=user_id)
              
            else:
                messages.error(request, user_form.errors)
                messages.error(request, profile_form.errors)
        else:
            user_form = UserForm(instance = user_read)
            profile_form = UserProfileForm(instance = profile_read)
            

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'user_read': user_read,
            'profile_read': profile_read,
            'workspaces' : workspaces,
        }
        
        return render(request, 'account/update_account.html', context)
    

@login_required(login_url='login')
def delete_account(request, user_id):
        professionals = get_object_or_404(Account, id=user_id)
        professionals.delete()
        messages.success(request, 'Profesinal eliminado correctamente')
        return redirect('list_accounts')
    

@login_required(login_url='login')
def view_account(request, user_id):
    
        user_read = get_object_or_404(Account, id=user_id)
        profile_read = get_object_or_404(UserProfile, user=user_read)
        workspaces = Workspace.objects.all().filter(user_create=user_read)
        
        context = {
        'user_read' : user_read,
        'profile_read' : profile_read,
        'workspaces' : workspaces,
        }
        
        return render (request, 'account/view_account.html', context)
    
    