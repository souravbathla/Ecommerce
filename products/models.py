from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):

    title = models.CharField(max_length=255, blank=True, null=True,
                             db_index=True)
    slug = models.SlugField(max_length=255, blank=True, null=True,
                            unique=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True, db_index=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Category, self).save()


class Product(models.Model):

    title = models.CharField(max_length=255, blank=True, null=True,
                             db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                blank=True, null=True)
    active = models.BooleanField(default=True, db_index=True)
    categories = models.ManyToManyField(Category)
    brand = models.CharField(max_length=255, blank=True, null=True,
                             db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False,
                                      db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False,
                                      db_index=True)

    def __str__(self):
        return self.title



class Variation(models.Model):

    product = models.ForeignKey(Product)
    title = models.CharField(max_length=255, blank=True, null=True,
                             db_index=True)
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                blank=True, null=True)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2,
                                     blank=True, null=True)
    active = models.BooleanField(default=False, db_index=True)
    inventory = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Variation"


class ProductFeature(models.Model):

    product = models.ForeignKey(Product)
    model_number = models.CharField(max_length=255, blank=True, null=True,
                                    db_index=True)
    model_name = models.CharField(max_length=255, blank=True, null=True,
                                  db_index=True)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    sim_type = models.CharField(max_length=255, blank=True, null=True)
    internal_storage = models.IntegerField(default=0)
    expandable_storage = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    primary_camera = models.IntegerField(default=0)
    secondary_camera = models.IntegerField(default=0)
    battery_capacity = models.IntegerField(default=0)








