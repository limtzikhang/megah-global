import random
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length=15, unique=True, editable=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField()
    bank_account = models.CharField(max_length=50)
    upline_id = models.CharField(max_length=15, null=True, blank=True)
    is_b2b = models.BooleanField(default=False)
    
    # Track the 1-time free bottle award criteria for B2B sponsor
    has_claimed_free_bottle = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.user_id:
            # Generates a clear custom user id: e.g., MH-847291
            self.user_id = f"MH-{random.randint(100000, 999999)}"
        super().save(*args, **kwargs)

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# FUTURE PROOFING: Placeholder structure for future 3MP MLM progression node assignment
class MLM3MPNode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='mlm_node')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    matrix_level = models.PositiveIntegerField(default=1) # Track 3MP matrix position
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Node: {self.user.user_id} - Level {self.matrix_level}"
