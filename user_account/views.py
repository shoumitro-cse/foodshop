from django.shortcuts import render, redirect
from django.views.generic import TemplateView #Import TemplateView

# Create your views here.

class UserIndexPage(TemplateView):
    template_name = "dashboard.html"

class orderPage(TemplateView):
    template_name = "order.html"

def dashboard(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "dashboard.html")

def profile(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "profile.html")

def order(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "order.html")

def order_view(request, id):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "order_view.html")

def wishlist(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "wishlist.html")

def comment_review(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "comment_review.html")

def addresses(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "addresses.html")

def help_support(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "help_support.html")

def settings(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "settings.html")

def change_password(request):
    if not request.session.has_key('username'):
        return redirect("/foodshop")
    return render(request, "change_password.html")

