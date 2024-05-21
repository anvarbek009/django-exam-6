from django.forms import ModelForm
from django import forms
from clocks.models import Review,Watch

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = '__all__'

class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']


class UpdateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']