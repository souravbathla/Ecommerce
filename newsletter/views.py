from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


# from .forms import ContactForm
# from products.models import ProductFeatured, Product

# Create your views here.
def home(request):
    # featured_image = ProductFeatured.objects.first()
    # products = Product.objects.all().order_by('?')
    context = {
        "featured_image": "sourav",
        "products": "bathla"
    }

    return render(request, "home.html" ,context )