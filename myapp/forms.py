from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Button, ButtonHolder, Submit
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_name',
            'product_title',
            'product_info',
            'product_description',
            'product_price',
            'brand',
            'product_type',
            'product_status',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('product_name', css_class='form-group col-md-6'),
                Column('product_title', css_class='form-group col-md-6')
            ),
            Row(
                Column('product_info', css_class='form-group col-md-6'),
                Column('product_description', css_class='form-group col-md-6')
            ),
            Row(
                Column('product_price', css_class='form-group col-md-6'),
                Column('brand', css_class='form-group col-md-6')
            ),
            Row(
                Column('product_type', css_class='form-group col-md-6'),
                Column('product_status', css_class='form-group col-md-6')
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )

        )