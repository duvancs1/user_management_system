from django.contrib.auth.models         import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation           import gettext as _
from django.db                          import models

from apps.admin.common.model_mixins     import AuditFields


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))

        return self.create_user(email, password, **extra_fields)


POSITION_CHOICES = (
    (0, 'None'),
    (1, 'Backend Developer'),
    (2, 'Frontend Developer'),
    (3, 'Full-stack Developer'),
    (4, 'DevOps Engineer'),
    (5, 'UI/UX Designer'),
    (6, 'QA Engineer'),
    (7, 'Project Manager')
)


class User(AuditFields, AbstractBaseUser, PermissionsMixin):

    reporting_line_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='reports_to')

    email                  = models.EmailField(unique=True)

    first_name             = models.CharField(max_length=30, blank=True)
    last_name              = models.CharField(max_length=30, blank=True)
    contact_number         = models.CharField(max_length=30, blank=True)
    employee_number        = models.CharField(max_length=30, blank=True)
    hashed_email_gravatar  = models.CharField(max_length=250, blank=True)
    position               = models.IntegerField(choices=POSITION_CHOICES, blank=True, null=True)

    birth_date             = models.DateField(null=True, blank=True)

    is_active              = models.BooleanField(default=True)
    is_staff               = models.BooleanField(default=False)
    is_admin               = models.BooleanField(default=False)

    salary                 = models.DecimalField(verbose_name='Salary', default=0, max_digits=9, decimal_places=2)

    description            = models.TextField(max_length=300, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.reporting_line_manager:
            return f"{self.first_name} {self.last_name} (Reports to: {self.reporting_line_manager.first_name})"
        elif self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} (No Manager)"
        else:
            return f"{self.email} (No Manager)"

    def str(self):
        return self.email

    def save(self, *args, **kwargs):
        # Ensure an employee cannot be their own manager
        if self.reporting_line_manager == self:
            raise ValueError("An employee cannot be their own manager.")
        super().save(*args, **kwargs)
