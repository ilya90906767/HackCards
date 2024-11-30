from django.db import models

class UserProfile(models.Model):
    telegram_id = models.BigIntegerField(unique=True)  # Telegram ID, уникальный для каждого пользователя
    date_birth = models.DateField(null=True, blank=True)  # Дата рождения
    date_death = models.DateField(null=True, blank=True)  # Дата смерти (может быть None, если человек жив)
    short_epigraphy = models.TextField(null=True, blank=True)  # Краткая эпитафия
    is_generated = models.BooleanField(default=False)  # Указывает, сгенерирован ли профиль
    fio = models.CharField(max_length=255, null=True, blank=True)  # Фамилия Имя Отчество

    def __str__(self):
        return f"User Profile(telegram_id={self.telegram_id}, date_birth={self.date_birth}, is_generated={self.is_generated})"

class UserPhoto(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='photos', on_delete=models.CASCADE)  # Связь с UserProfile
    image = models.TextField(null=True, blank=True)  # Путь для хранения изображений

    def __str__(self):
        return f"Photo for {self.user_profile.telegram_id}"