from msilib.schema import ListView
import re
from sre_constants import SUCCESS
from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, FormView
from .forms import login_form
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth import logout, login , authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Books, cart
from django.shortcuts import get_object_or_404

# Create your views here.

class Index(ListView):
    model = Books
    template_name = 'rent/index.html'
    context_object_name = 'item'
    def post(self, request):
        users  = self.request.user
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Books, pk=book_id)
        non_usable, carts = cart.objects.get_or_create(user=users, book=book)
        print(non_usable.quantity)
        print(non_usable)
        print(carts)
        if carts == False and non_usable:
            print("this is used")
            non_usable.quantity += 1
            non_usable.save()
        else: 
            print("Book Added")

        

        return redirect('index')


class Login(FormView):
    template_name = 'rent/login.html'
    redirect_authenticated_user = True
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(Login, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            return HttpResponse('Invalid login details supplied.')
    def get(self, request, *args, **kwargs):
        form = login_form()
        return render(request, 'rent/login.html', {'form': form})


def Logout_view(request):
    logout(request)
    return render(request, 'rent/index.html')

class ItemView(DetailView):
    model = Books
    template_name = 'rent/item.html'
    context_object_name = 'item'

class Cart(LoginRequiredMixin, ListView):
    model = cart
    template_name = 'rent/cart.html'
    context_object_name = 'cart'

    # def post(self, request):
    #     users  = self.request.user
    #     book_id = request.POST.get('book_id')
    #     book = get_object_or_404(Books, pk=book_id)
    #     non_usable, carts = cart.objects.get_or_create(user=users, book=book)
    #     if non_usable:
    #         non_usable.quantity -= 1
    #         non_usable.save()
    #     else:
    #         cart.objects.create(user=users, book=book)        
    #     return redirect('cart')

    def cart_remove(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Books, id=product_id)
        cart.remove(product)
        return redirect('cart')
    
    

