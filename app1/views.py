from django.shortcuts import render,get_object_or_404
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignInForm, CustomUserCreationForm,CustomerForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .models import Product,Category,Customer

class IndexView(View):
    def get(self, request):
        form = CustomerForm()
        categories = Category.objects.all()

        context = {
            'form': form,
            'index': {
                'categories': categories,
            },
        }
        return render(request, 'index.html', context)

class SignUp(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request,'signup.html', {'form': form})
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signin') 
        return render(request,'signup.html', {'form': form})
class SignOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            request.session.flush()
            return redirect('signin')  
        else:
            return redirect('signin')
    
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['id'] = user.id
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission. Please check the form data.')

        return render(request, 'signin.html', {'form': form})
class AboutView(View):
    def get(self, request):
        return render(request,'about.html')
class ProductListView(View):
    def get(self, request):
        query = request.GET.get('q')
        products = Product.objects.all()
        
        if query:
            products = products.filter(name__icontains=query)
        
        context = {
            'products': products,
        }
        return render(request, 'product_list.html', context)
class ContactView(View):
    def get(self, request, pk=None):
        if pk is not None:
            instance1 = Customer.objects.get(pk=pk)
            form = CustomerForm(instance=instance1)
            return render(request, 'contact.html', {'form': form, 'instance': instance1})
        else:
            form = CustomerForm()
            data = Customer.objects.all()
            return render(request, 'contact.html', {'form': form, 'data': data})
   
    def post(self, request, pk=None):
        instance_id = request.POST.get('instance')
        if instance_id:
            instance = Customer.objects.get(pk=instance_id)
            form = CustomerForm(request.POST, request.FILES, instance=instance)
        else:
            form = CustomerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            data = Customer.objects.all()
            return render(request, 'contact.html', {'form': form, 'data': data})
class DetailesView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'why.html', {'product': product})
class CategoryProductsView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        context = {
            'category': category,
            'products': products,
        }
        
        return render(request, 'product_list.html', context)