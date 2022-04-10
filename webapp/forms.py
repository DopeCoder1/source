from django import forms
from django.contrib.auth.models import User

from webapp.models import Book, Order, Publisher, Request, RequestBook, Student, Staff, Article, thesis


class StudForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class ThesisForm(forms.ModelForm):
    class Meta:
        model = thesis
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","password"]

class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","password"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StaffUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","password"]

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = []

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []

class RequestBookForm(forms.ModelForm):
    class Meta:
        model = RequestBook
        exclude = ['request']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        exclude = []

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = []

