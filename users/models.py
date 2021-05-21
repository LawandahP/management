from PIL import Image
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have a username")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.is_tenant = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_tenant = False
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    ADMIN = 'admin'
    STAFF = 'staff'
    STATUS = [
        (ADMIN, 'Admin User'),
        (STAFF, 'Staff User'),
    ]

    GENDER = (
        ('Male', ('Male')),
        ('Female', ('Female')),
        ('Unspecified', ('Unspecified')),
    )
    OCCUPATION = (
        ('Self-Employed', ('Self-Employed')),
        ('Employed', ('Employed')),
        ('Student', ('Student')),
    )
    email = models.EmailField(verbose_name='email address',
                              unique=True,
                              max_length=255)
    username = models.CharField(max_length=30, unique=True)
    Tenant_Full_Names = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=32,
                              choices=GENDER,
                              default='Male',
                              )

    National_ID = models.IntegerField(unique=True, null=True)

    phone_number1 = PhoneNumberField(unique=True, region='KE',
                                     verbose_name='phone number(work)')

    phone_number2 = PhoneNumberField(unique=True,
                                     region='KE',
                                     verbose_name='phone number(home)')

    occupation_status = models.CharField(max_length=32,
                                         choices=OCCUPATION,
                                         default='Employed',
                                         )

    at = models.CharField(max_length=255, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_tenant = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    def __str__(self):
        return f'{self.Tenant_Full_Names}'


class Profile(models.Model):
    STATUS = (
        ('SINGLE', ('SINGLE')),
        ('MARRIED', ('MARRIED')),
    )

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True
    )
    image = models.ImageField(default='kanjologo.png', upload_to='profile_pics/', blank=True)
    marital_status = models.CharField(default='SINGLE', choices=STATUS, max_length=255)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


