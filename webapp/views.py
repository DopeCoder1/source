from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from webapp.models import Book, thesis, Student, Order, Publisher, Request, RequestBook, Article, Staff
from webapp.forms import OrderForm, BookForm, RequestBookForm, PublisherForm, RequestForm, ArticleForm, ThesisForm, \
    StudForm, StaffForm
from collections import Counter
from django.contrib.auth.models import Group
from .forms import UserForm
from .decarator import unauthenticated_user,allow_users
from django.utils.decorators import method_decorator

def base_acc(request):
    user = request.user
    return render(request,"acc.html",{"user":user})

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_staff(user):
    return user.groups.filter(name='STAFF').exists()
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def adminbar(request):
    book = Book.objects.all()
    return render(request,"adminbar.html",{"book":book})

def admin_stud_list(request):
    student = Student.objects.all()
    return render(request,"admin_list_student.html",{"student":student})

def staffbar(request):
    return render(request,"staffbar.html")

def studentbar(request):
    books = Book.objects.all()
    return render(request, "student_book.html", {"books": books})


def student_book(request):
    books = Book.objects.all()
    return render(request, "student_book.html", {"books": books})

def student_publisher(request):
    pub = Publisher.objects.all()
    return render(request, "student_publisher.html", {"pub": pub})

def student_acc(request):
    user = request.user
    return render(request,"student_acc.html",{"user":user})

def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('webapp:book_list')
    elif is_staff(request.user):
        return redirect('webapp:staffbar')
    elif is_student(request.user):
        return redirect('webapp:student')
    # elif is_patient(request.user):
    #     accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
    #     if accountapproval:
    #         return redirect('patient-dashboard')
    #     else:
    #         return render(request,'hospital/patient_wait_for_approval.html')




def admin_signup_view(request):
    form = UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.is_staff = True
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            my_admin_group = Group.objects.get_or_create(name='STAFF')
            my_admin_group[0].user_set.add(user)
            return redirect("webapp:login")
    return render(request,'reg.html',{'form':form})



def staff_signup_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.is_staff = True
            user.save()
            my_admin_group = Group.objects.get_or_create(name='STAFF')
            my_admin_group[0].user_set.add(user)
            return redirect("webapp:stafflogin")
    return render(request, 'reg.html', {'form': form})





def student_signup_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.is_staff = True
            user.save()
            my_student = Student.objects.create(user=user,iin=user.id)
            my_admin_group = Group.objects.get_or_create(name='STUDENT')
            my_admin_group[0].user_set.add(user)
            return redirect("webapp:studentlogin")
    return render(request, 'reg.html', {'form': form})


def registrationPage(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        form  = UserForm()
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("webapp:login")
        context = {
            "form":form
        }
        return render(request,"reg.html",context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("webapp:regis")
        else:
            messages.error(request, 'username and password doesn\'t match')
    context = {"messages":messages}
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    return redirect("webapp:login")

@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_staff),name='get')
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='put')
@method_decorator(user_passes_test(is_staff),name='put')
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='delete')
@method_decorator(user_passes_test(is_staff),name='delete')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'

    def get_success_url(self):
        return reverse('webapp:book_list')

@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_staff),name='get')
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='put')
@method_decorator(user_passes_test(is_staff),name='put')
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='delete')
@method_decorator(user_passes_test(is_staff),name='delete')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'

    def get_success_url(self):
        return reverse('webapp:book_list')



def home_view(request):
    book = Book.objects.all()
    article = Article.objects.all()
    thesiss = thesis.objects.all()

    context = {"book":book,"article":article,"thesiss":thesiss}
    return render(request,"all_list.html",context)

class BookListView(ListView):
    model = Book
    template_name = 'index.html'



@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_staff),name='get')
class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderbooks'] = RequestBook.objects.filter(book__publisher=self.object.publisher)
        list = []
        for orderbook in context['orderbooks']:
            list.append(orderbook.book.id)
        a = set(list)
        context['list'] = a
        context['len'] = len(list)

        for orderbook in context['orderbooks']:
            if orderbook.book.id in list:
                amount = orderbook.amount
                amount += orderbook.amount
                context['amount'] = amount

        return context


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='put')
@method_decorator(user_passes_test(is_staff),name='put')
class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm


    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})

# class OrderBookCreateView(CreateView):
#     model = OrderBook
#     form_class = OrderBookForm
#     template_name = 'order_book_create.html'
#
#     def get_success_url(self):
#         return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['order'] = Order.objects.get(pk=self.kwargs.get('pk'))
#         return context
#
#     def form_valid(self, form):
#         form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
#         return super().form_valid(form)
#
# class OrderBookUpdateView(UpdateView):
#     model = OrderBook
#     form_class = OrderBookForm
#     template_name = 'order_book_update.html'
#
#     def get_success_url(self):
#         return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})
#
# class OrderBookDeleteView(DeleteView):
#     model = OrderBook
#     template_name = 'order_book_delete.html'
#
#     def get_success_url(self):
#         return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_staff),name='get')
class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'publisher_detail.html'


class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher_list.html'

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'publisher_create.html'
    form_class = PublisherForm

    def get_success_url(self):
        return reverse('webapp:publisher_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='put')
@method_decorator(user_passes_test(is_staff),name='put')
class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher_update.html'
    form_class = PublisherForm

    def get_success_url(self):
        return reverse('webapp:publisher_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='delete')
@method_decorator(user_passes_test(is_staff),name='delete')
class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publisher_delete.html'


    def get_success_url(self):
        return reverse('webapp:publisher_list')

@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_staff),name='get')
class RequestDetailView(DetailView):
    model = Request
    template_name = 'request_detail.html'

def admin_stud_lists(request):
    students = Student.objects.all()
    return render(request,"admin_stud_list.html",{"students":students})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class StudentCreateView(CreateView):
    model = Student
    template_name = 'admin_stud_create.html'
    form_class = StudForm

    def get_success_url(self):
        return reverse('webapp:adminstud_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_staff),name='get')
class StudentDetailView(DetailView):
    model = Student
    template_name = 'admin_stud_detail.html'
    context_object_name = "students"

@method_decorator(login_required(login_url='webapp:stafflogin'),name='put')
@method_decorator(user_passes_test(is_staff),name='put')
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'admin_stud_update.html'
    form_class = StudForm

    def get_success_url(self):
        return reverse('webapp:adminstud_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='webapp:stafflogin'),name='delete')
@method_decorator(user_passes_test(is_staff),name='delete')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'admin_stud_delete.html'
    context_object_name = "staff"

    def get_success_url(self):
        return reverse('webapp:adminstud_list')


class RequestListView(ListView):
    model = Request
    template_name = 'request_list.html'
    context_object_name = "request"

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class RequestCreateView(CreateView):
    model = Request
    template_name = 'request_create.html'
    form_class = RequestForm

    def get_success_url(self):
        return reverse('webapp:request_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class RequestBookCreateView(CreateView):
    model = RequestBook
    form_class = RequestBookForm
    template_name = 'request_book_create.html'

    def get_success_url(self):
        return reverse('webapp:request_detail', kwargs={'pk': self.object.request.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = Request.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.request = Request.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

def book_list(request):
    book = Book.objects.all()
    return render(request,"book_list.html",{"book":book})

def article_list(request):
    article = Article.objects.all()
    return render(request,"article_list.html",{"article":article})




@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_staff),name='get')
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = "article"

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='put')
@method_decorator(user_passes_test(is_staff),name='put')
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='delete')
@method_decorator(user_passes_test(is_staff),name='delete')
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'

    def get_success_url(self):
        return reverse('webapp:home')

####
def thesis_list(request):
    thesiss = thesis.objects.all()
    return render(request,"thesis_list.html",{"thesiss":thesiss})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_staff),name='get')
class ThesisDetailView(DetailView):
    model = thesis
    template_name = 'thesis_detail.html'
    context_object_name = "thesis"

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_staff),name='post')
class ThesisCreateView(CreateView):
    model = thesis
    template_name = 'thesis_create.html'
    form_class = ThesisForm

    def get_success_url(self):
        return reverse('webapp:thesis_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_student),name='post')
class ThesisCreateView2(CreateView):
    model = thesis
    template_name = 'student_thesis.html'
    form_class = ThesisForm

    def get_success_url(self):
        return reverse('webapp:thesis_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='webapp:stafflogin'),name='put')
@method_decorator(user_passes_test(is_staff),name='put')
class ThesisUpdateView(UpdateView):
    model = thesis
    template_name = 'thesis_update.html'
    form_class = ThesisForm

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='delete')
@method_decorator(user_passes_test(is_staff),name='delete')
class ThesisDeleteView(DeleteView):
    model = thesis
    template_name = 'thesis_delete.html'

    def get_success_url(self):
        return reverse('webapp:home')


###
def staff_lists(request):
    staff = Staff.objects.all()
    return render(request,"admin_staff_list.html",{"staff":staff})

@login_required(login_url="webapp:stafflogin")
@user_passes_test(is_staff)
def staff_book(request):
    book = Book.objects.all().filter(publisher__user_id=request.user.id)
    return render(request,"book_list.html",{"book":book})


@login_required(login_url="webapp:stafflogin")
@user_passes_test(is_staff)
def staff_article(request):
    article = Article.objects.all().filter(teacher__user_id=request.user.id)
    return render(request,"article_list.html",{"article":article})

@login_required(login_url="webapp:stafflogin")
@user_passes_test(is_staff)
def staff_thesis(request):
    thesiss = thesis.objects.all().filter(student__user_id=request.user.id)
    return render(request,"thesis_list.html",{"thesiss":thesiss})

@login_required(login_url="webapp:stafflogin")
@user_passes_test(is_staff)
def staff_students(request):
    students = Student.objects.all().filter(user_id=request.user.id)
    return render(request,"admin_stud_list.html",{"students":students})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='post')
@method_decorator(user_passes_test(is_admin),name='post')
class StaffCreateView(CreateView):
    model = Staff
    template_name = 'admin_staff_create.html'
    form_class = StaffForm

    def get_success_url(self):
        return reverse('webapp:adminstaff_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='webapp:stafflogin'),name='get')
@method_decorator(user_passes_test(is_admin),name='get')
class StaffDetailView(DetailView):
    model = Staff
    template_name = 'admin_staff_detail.html'
    context_object_name = "staff"

@method_decorator(login_required(login_url='webapp:stafflogin'),name='put')
@method_decorator(user_passes_test(is_admin),name='put')
class StaffUpdateView(UpdateView):
    model = Staff
    template_name = 'admin_staff_update.html'
    form_class = StaffForm

    def get_success_url(self):
        return reverse('webapp:adminstaff_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='webapp:stafflogin'),name='delete')
@method_decorator(user_passes_test(is_admin),name='delete')
class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'admin_staff_delete.html'
    context_object_name = "staff"

    def get_success_url(self):
        return reverse('webapp:adminstaff_list')
