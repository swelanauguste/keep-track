import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    pass


class Profile(models.Model):
    GENDER_LIST = [
        ("F", "Female"),
        ("M", "Male"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    phone = models.CharField(max_length=25, null=True, default="+1")

    # def get_absolute_url(self):
    #     return reverse("user-profile-detail", kwargs={"slug": self.slug})

    # def get_absolute_update_url(self):
    #     return reverse("user-profile-update", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.uid)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user.email}"

    # def get_profile_initials(self):
    #     if self.first_name and self.last_name:
    #         return f"{self.first_name[0]}{self.last_name[0]}"
    #     return self.user.email[0].upper()

    # def __str__(self) -> str:
    #     if self.first_name and self.last_name:
    #         return f"{self.first_name} {self.last_name}"
    #     return f"{self.user}"
