from django.contrib import admin

from products.models import Product, ProductFeature, Category,Variation

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductFeature, ProductAdmin)
admin.site.register(Variation, ProductAdmin)
admin.site.register(Category, ProductAdmin)
