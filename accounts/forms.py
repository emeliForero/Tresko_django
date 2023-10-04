from django import forms
from .models import *

# Formularios para Crear usuarios
class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta:
        model = Account
        fields = ['first_name','last_name', 'phone_number', 'email','password']
        
    
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = 'off'
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True
            

class UserProfileCreateForm(forms.ModelForm):
    photo = forms.ImageField(required=False, error_messages={'invalid': ('Solo archivos de imagen')}, widget=forms.FileInput, label='Foto de perfil')
    
    class Meta:
        model = UserProfile
        fields = [
            'photo',
            ]
    
    def __init__(self, *args, **kwargs):
        super(UserProfileCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = 'off'
            self.fields[field].widget.attrs['class'] = 'form-control'
            
        self.fields['photo'].required = False
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number', 'email']
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'phone_number': 'Celular',
        }
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = 'off'        
            self.fields[field].widget.attrs['class'] = 'form-control'
            
            
            
class UserProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=True, error_messages={'invalid': ('Solo archivos de imagen')}, widget=forms.FileInput, label='Foto de perfil')  
    class Meta:
        model = UserProfile
        fields = fields = [
            'photo']
        
        
    def __init__(self, *args, **kwargs):
        self.user_session = kwargs.pop('user', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = 'off'
            self.fields[field].widget.attrs['class'] = 'form-control'
            
        self.fields['photo'].required = True

       

     

    