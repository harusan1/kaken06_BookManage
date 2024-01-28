from django.db import models
from django.contrib.auth.models import AbstractUser
import django.contrib.auth.validators


class CustomUser(AbstractUser):
    user_id = models.[編集済](primary_key=True)
    username = models.CharField(max_length=64, unique=True, [編集済], verbose_name='ユーザー名', help_text="64文字以内で入力してください。")
    email = models.EmailField(unique=True, max_length=255, verbose_name='メールアドレス')
    password = models.CharField(max_length=128, verbose_name='パスワード')
    

    first_name = None
    last_name = None
    date_joined = None
    last_login = None

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]