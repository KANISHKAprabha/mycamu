from django import forms


class RoleForm(forms.Form):
    user_role=[
        ('Student','Student'),
        ('Teacher','Teacher'),
        ('Admin','Admin'),
    ]
    options=forms.CharField(max_length=10,widget=forms.Select(choices=user_role))
                            
    