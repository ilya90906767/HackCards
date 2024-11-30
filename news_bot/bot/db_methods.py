import asyncio
from asgiref.sync import sync_to_async
from datetime import datetime
from users.models import UserProfile, UserPhoto

@sync_to_async
def get_user_from_db(user_id):
    return UserProfile.objects.get(telegram_id=user_id)

@sync_to_async
def update_user_fio(telegram_id, user_fio):
    user_profile = UserProfile.objects.get(telegram_id=telegram_id)  # Fetch the user profile
    user_profile.fio = user_fio  # Update the FIO field
    user_profile.save()  # Save the changes

@sync_to_async
def update_user_DateBirth(telegram_id, user_DateBirth):
    user_profile = UserProfile.objects.get(telegram_id=telegram_id)  # Fetch the user profile
    user_DateBirth = datetime.strptime(user_DateBirth, "%Y.%m.%d").date()
    user_profile.date_birth = user_DateBirth  # Update the FIO field
    user_profile.save()  # Save the changes

@sync_to_async
def update_user_DateDeath(telegram_id, user_DateDeath):
    user_profile = UserProfile.objects.get(telegram_id=telegram_id)
    user_DateDeath = datetime.strptime(user_DateDeath, "%Y.%m.%d").date()
    user_profile.date_death = user_DateDeath
    user_profile.save()

@sync_to_async
def update_user_Epigraph(telegram_id, user_Epigraph):
    user_profile = UserProfile.objects.get(telegram_id=telegram_id)
    user_profile.short_epigraphy = user_Epigraph
    user_profile.save()

@sync_to_async
def update_user_Photos(telegram_id, photo_path):
    user_profile = UserProfile.objects.get(telegram_id=telegram_id)
    user_photo = UserPhoto(user_profile=user_profile, image=f'{photo_path}')
    user_photo.save()

