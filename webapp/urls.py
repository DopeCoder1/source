from django.contrib.auth.views import LoginView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import BookCreateView, BookDetailView, BookListView, BookDeleteView, \
    BookUpdateView, OrderListView, OrderDetailView, PublisherDetailView, \
    PublisherListView, OrderUpdateView, OrderCreateView, PublisherCreateView, PublisherDeleteView, PublisherUpdateView, \
    RequestListView, \
    RequestDetailView, RequestCreateView, RequestBookCreateView, loginPage, logoutUser, registrationPage, \
    afterlogin_view, admin_signup_view, staff_signup_view, staffbar, student_signup_view, studentbar, student_book, \
    student_publisher, student_acc, home_view, ArticleCreateView, ArticleDetailView, ArticleUpdateView, \
    ArticleDeleteView, ThesisDetailView, ThesisCreateView, ThesisUpdateView, ThesisDeleteView, base_acc, thesis_list, \
    article_list, book_list, admin_stud_list, StudentDetailView, admin_stud_lists, StudentUpdateView, StudentDeleteView, \
    StudentCreateView, staff_lists, StaffDetailView, StaffDeleteView, StaffUpdateView, StaffCreateView, staff_students, \
    staff_thesis, staff_book, staff_article, ThesisCreateView2

app_name = 'webapp'

urlpatterns = [
    path("adminstud_list",admin_stud_lists,name="adminstud_list"),
    path("adminstud_detail/<int:pk>", StudentDetailView.as_view(), name="adminstud_detail"),
    path("adminstud_delete/<int:pk>", StudentDeleteView.as_view(), name="adminstud_delete"),
    path("adminstud_update/<int:pk>", StudentUpdateView.as_view(), name="adminstud_update"),
    path("adminstud_create", StudentCreateView.as_view(), name="adminstud_create"),

    path("adminstaff_list",staff_lists,name="adminstaff_list"),
    path("adminstaff_detail/<int:pk>", StaffDetailView.as_view(), name="adminstaff_detail"),
    path("adminstaff_delete/<int:pk>", StaffDeleteView.as_view(), name="adminstaff_delete"),
    path("adminstaff_update/<int:pk>", StaffUpdateView.as_view(), name="adminstaff_update"),
    path("adminstaff_create", StaffCreateView.as_view(), name="adminstaff_create"),

    path("thesis_list",thesis_list,name="thesis_list"),
    path("thesis_detail/<int:pk>",ThesisDetailView.as_view(),name="thesis_detail"),
    path("thesis_create",ThesisCreateView.as_view(),name="thesis_create"),
    path("thesis_create2", ThesisCreateView2.as_view(), name="thesis_create2"),
    path("thesis_update/<int:pk>",ThesisUpdateView.as_view(),name="thesis_update"),
    path("thesis_delete/<int:pk>",ThesisDeleteView.as_view(),name="thesis_delete"),
    path("article_detail/<int:pk>",ArticleDetailView.as_view(),name="article_detail"),
    path("article_create",ArticleCreateView.as_view(),name="article_create"),
    path("article_update/<int:pk>",ArticleUpdateView.as_view(),name="article_update"),
    path("article_delete/<int:pk>",ArticleDeleteView.as_view(),name="article_delete"),
    path("artice_list/",article_list,name="article_list"),
    path("",home_view,name="book_list"),
    path("book_List",book_list,name="book_lists"),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/create', BookCreateView.as_view(), name='book_create'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('orders', OrderListView.as_view(), name='order_list'),
    path('publisher/<int:pk>', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publishers', PublisherListView.as_view(), name='publisher_list'),
    path('publisher/create', PublisherCreateView.as_view(), name='publisher_create'),
    path('publisher/update/<int:pk>', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher/delete/<int:pk>', PublisherDeleteView.as_view(), name='publisher_delete'),
    # path('order/<int:pk>/book/create', OrderBookCreateView.as_view(), name='order_book_create'),
    # path('order/book/<int:pk>/update', OrderBookUpdateView.as_view(), name='order_book_update'),
    # path('order/book/<int:pk>/delete', OrderBookDeleteView.as_view(), name='order_book_delete'),
    path('request/<int:pk>', RequestDetailView.as_view(), name='request_detail'),
    path('requests', RequestListView.as_view(), name='request_list'),
    path('request/create', RequestCreateView.as_view(), name='request_create'),
    path('request/<int:pk>/book/create', RequestBookCreateView.as_view(), name='request_book_create'),
    path('adminlogin', LoginView.as_view(template_name='login.html'),name="login"),
    path('stafflogin', LoginView.as_view(template_name='login.html'),name="stafflogin"),
    path('studentlogin', LoginView.as_view(template_name='login.html'),name="studentlogin"),
    path("adminsign/",admin_signup_view,name="adminsign"),
    path("staffsign/",staff_signup_view,name="staffsign"),
    path("studentsign/",student_signup_view,name="studentsign"),
    path("logoutpage/",logoutUser,name="exit"),
    path('afterlogin', afterlogin_view,name='afterlogin'),
    path('staffbar/',staffbar,name='staffbar'),
    path("staffstudent/",staff_students,name="staff_stud"),
    path("staffthesis/",staff_thesis,name="staff_thesis"),
    path("staffbook/",staff_book,name="staff_book"),
    path("staffarticle",staff_article,name="staff_article"),
    path('student/', studentbar, name='student'),
    path('student_book/',student_book,name='student_book'),
    path('student_publisher/', student_publisher, name='student_pub'),
    path('student_acc/',student_acc,name="student_acc"),
    path('acc/',base_acc,name="acc"),

]

