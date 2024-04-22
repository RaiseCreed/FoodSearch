from typing import Any
from django.forms import ModelForm
from django import forms
from .models import Recipe, Review


class RecipeForm(ModelForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            
    class Meta:
        model = Recipe
        fields = ['name','image','intro','description','tags']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']

        labels = {
            'value': 'Place your vote',
            'body':'Add a comment with your vote'
        }

        

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        self.fields['value'].empty_label = None

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            field.widget.attrs.update({'style': 'width: 100% !important;'})
