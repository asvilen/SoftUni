from django.db import models
from django.db.models import Count, Sum, Q, F


class Category(models.Model):
    name = models.CharField(max_length=100)


class ProductManager(models.Manager):
    def available_products(self):
        return self.filter(is_available=True)

    def available_products_in_category(self, category_name: str):
        return self.filter(
            is_available=True,
            category__name=category_name
        )


class Product(models.Model):
    objects = ProductManager()

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category.name}: {self.name}"


class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


def product_quantity_ordered():
    agg_result = Product.objects\
        .annotate(products_ordered=Sum('orderproduct__quantity'))\
        .exclude(products_ordered=None)\
        .order_by(('-products_ordered'))

    result = [
        f"Quantity ordered of {product.name}: {product.products_ordered}"
        for product
        in agg_result
    ]
    return '\n'.join(result)


def ordered_products_per_customer():
    prefetched_orders = Order.objects\
        .prefetch_related('orderproduct_set__product__category')\
        .order_by('id')
    result = []
    for order in prefetched_orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for order_product in order.orderproduct_set.all():
            result.append(f"- Product: {order_product.product.name}, Category: {order_product.product.category.name}")

    return "\n".join(result)


def filter_products():
    query = Q(is_available=True) & Q(price__gt=3)
    filtered_products = Product.objects.filter(query).order_by('-price', 'name')
    result = [
        f"{product.name}: {product.price}lv."
        for product
        in filtered_products
    ]
    return "\n".join(result)


def give_discount():
    query = Q(is_available=True) & Q(price__gt=3)
    filtered_products = Product.objects.filter(query)
    filtered_products.update(price=F('price') * 0.7)
    products_after_discount = Product.objects.filter(is_available=True).order_by("-price", "name")
    result = [
        f"{product.name}: {product.price}lv."
        for product
        in products_after_discount
    ]
    return "\n".join(result)
