from django.db import models
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

# class CategoryWatch(models.Model):
#     name=models.CharField(max_length=100)

#     class Meta:
#         db_table = 'category_watch'

#     def __str__(self):
#         return self.name
    

class Watch(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='watch_images/',blank=True,null=True,default='default_images/watch_image.png')
    price=models.IntegerField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'watch'
    
    def __str__(self):
        return self.name
    

class Review(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    watch=models.ForeignKey(Watch,on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'Review {self.comment} by {self.user}' 
# ----------------------------------------------------------------
# class Order(models.Model):
#     user=models.CharField(max_length=100)
#     number=models.IntegerField()

#     class Meta:
#         db_table = 'order'

#     def __str__(self):
#         return self.number
# Ishlamadi
# ------------------------------------------------

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f"{self.user.username}'s cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'cart_item'

    def __str__(self):
        return f"{self.quantity} of {self.watch.name}"
    
