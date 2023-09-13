from django.forms import ModelForm
from main.models import Product

class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]