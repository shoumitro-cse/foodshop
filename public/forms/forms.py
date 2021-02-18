from django import forms
from public.models import Users, Login

# from public.users_form import UsersForm, LoginForm

class UsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = "__all__"
        # fields = ['fullname', 'email']

    def send_email(self):
        print()
        print()
        print("Send Mail")
        print()
        print()
        pass


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        #fields = "__all__"
        fields = ['u_password', 'u_re_password']