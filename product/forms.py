from django import forms
from product.models import ProductReview


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = [
            'message'
        ]
        widgets = {
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'cols' : 30,
                'rows' : 5,
                'placeholder' : 'Write your review.'
            })
        }