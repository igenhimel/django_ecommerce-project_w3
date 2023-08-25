from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):

    PRODUCT_TYPE_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Fashion', 'Fashion'),
        ('Groceries', 'Groceries'),
        ('Home & Lifestyle', 'Home & Lifestyle'),
    ]

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(
        max_length=255, choices=PRODUCT_TYPE_CHOICES)
    product_details = models.TextField()
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    product_discount = models.PositiveIntegerField(
        null=True, blank=True, default=0, validators=[MaxValueValidator(100)])
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.product_name}"
