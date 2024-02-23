


from django.db import models

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projects.settings')

class Inventory(models.Model):
    category = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    creation_date = models.CharField(max_length=100)
    task_type = models.CharField(max_length=100)
    version_capacity = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    in_out_date = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    production_quantity = models.CharField(max_length=100)
    delivery_quantity = models.CharField(max_length=100)
    as_in_quantity = models.CharField(max_length=100)
    as_repair_quantity = models.CharField(max_length=100)
    as_out_quantity = models.CharField(max_length=100)
    input_complete = models.CharField(max_length=100)
    final_edit_timestamp = models.CharField(max_length=100)
    as_replacement = models.CharField(max_length=100)

Inventory.objects.create(category ='속성')
# Create your models here

