from django import forms
from .models import Workspace, Card, CardAttachment
from django.forms import FileInput

# class WorkspaceForm(forms.ModelForm):
#     description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    
#     class Meta:
#         model = Workspace
#         fields = ['title', 'type_space', 'description']
        
#     def __init__(self, *args, **kwargs):
#         super(WorkspaceForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['autocomplete'] = 'off'
#             self.fields[field].widget.attrs['class'] = 'form-control'
    
#         self.fields['title'].required = True
#         self.fields['type_space'].required = True
#         self.fields['description'].required = False
        
    
class CardForm(forms.ModelForm):
    card_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    file_imagen = forms.ImageField(required=False, error_messages={'invalid': ('Image files only')}, widget=forms.FileInput)  
    class Meta:
        model = Card
        fields = ['card_title', 'card_description', 'file_imagen']
        
        
        
        
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = 'off'
            self.fields[field].widget.attrs['class'] = 'form-control'
    
        self.fields['card_title'].required = True
        self.fields['card_description'].required = False
        self.fields['file_imagen'].required = False

class CardAttachmentForm(forms.ModelForm):
    class Meta:
        model = CardAttachment
        fields = ['file']
        
        file = forms.FileField()

        
    def __init__(self, *args, **kwargs):
        super(CardAttachmentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = 'off'
            self.fields[field].widget.attrs['class'] = 'form-control'
    
        self.fields['file'].required = False
        
        
class ImagenForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['file_imagen']