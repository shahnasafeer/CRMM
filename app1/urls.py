from django.urls import path
from .views import IndexView, LoginView, SignUp, SignOutView, AboutView, ProductListView, ContactView,DetailesView,CategoryProductsView

urlpatterns = [
    path('', LoginView.as_view(), name='signin'),
    path('index/', IndexView.as_view(), name='index'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('about/', AboutView.as_view(), name='about'),
    path('products/', ProductListView.as_view(), name='products'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/<int:pk>/', DetailesView.as_view(), name='product_detail'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),

]
