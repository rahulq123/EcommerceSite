from django import forms
from .models import Order


# this form is used when the user click on checkout after done with shopping
# it than display the fields name in the form such as; firstname, lastname, email, address, postal_code and city
# for the user to fill in before placing the order
# the fields name are used from the order model which is used to create the database for the cutomer order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                 'postal_code', 'city']