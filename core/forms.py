from django import forms
from .models import Todo


 


class TodoForm(forms.ModelForm):


    class Meta:
        model = Todo
        fields = ('bg_color','txt_color', 'topic', 'title','description')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control my-1','id':'Form'}),
            'topic':forms.TextInput(attrs={'class':'form-control my-1','id':'Form'}),
            'bg_color':forms.Select(attrs={'class':'form-select my-1','id':'Form'}),
            'txt_color':forms.Select(attrs={'class':'form-select my-1 ','id':'Form'}),
            'description':forms.Textarea(attrs={'class':'form-control my-1','style':'height:4rem','id':'Form'}),
        }

