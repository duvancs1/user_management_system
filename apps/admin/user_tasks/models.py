from django.db                      import models

from apps.admin.common.model_mixins import AuditFields
from apps.admin.user.models         import User


class UserTask(AuditFields):

    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'In Progress'),
        (3, 'Completed'),
    )

    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    status      = models.IntegerField(choices=STATUS_CHOICES, default='Pending')
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name}'s Task: {self.description[:20]}..."
