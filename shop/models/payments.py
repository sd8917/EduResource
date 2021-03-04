from django.db import models
from shop.models import Product,User

class Payment(models.Model):
    
    user = models.ForeignKey(User , null=False,on_delete=models.CASCADE)
    product  = models.ForeignKey(Product,null=False,on_delete=models.CASCADE)
    payment_request_id = models.CharField(max_length=200,null=False,unique=True)
    payment_id = models.CharField(max_length=200, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,default='failed')

    