from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import  ContactForm


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


def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = "innovation contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,'souravbathla@gmail.com']
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)
        message = contact_message
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  html_message=message,
                  fail_silently=True)
    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center
    }
    return render(request, "forms.html", context)

