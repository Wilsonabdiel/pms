from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("messages", views.messages, name="messages"),
    path("add", views.add, name="add"),
    path("all/<int:id>", views.all, name="all"),
    path('delete/<int:id>', views.delete, name="delete"),
    path("edit/<int:id>", views.edit, name="edit"),
    
    
    
    # API Routes
    path("emails", views.compose, name="compose"),
    path("emails/<int:email_id>", views.email, name="email"),
    path("emails/<str:mailbox>", views.mailbox, name="mailbox"),
]
