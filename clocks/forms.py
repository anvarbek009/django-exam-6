from django.forms import ModelForm
from django import forms
from clocks.models import Review,Watch,Order

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
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'number']