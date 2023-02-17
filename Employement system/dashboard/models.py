from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('I.T','I.T'),
    ('Accounting','Accounting'),
    ('HR','HR'),
)

class Roles(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity = models.PositiveBigIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Staff Roles'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Hired(models.Model):
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    hired_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Staff Hired'

    def __str__(self):
        return f'{self.roles} order by {self.staff.username}'



