import asyncio
from asgiref.sync import sync_to_async
from datetime import datetime
from users.models import UserProfile, UserPhoto
import re
from django.conf import settings
import os
from .gpt import generate_one

from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip
from moviepy.video.fx import fadein, fadeout

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
    user_photo = UserPhoto(user_profile=user_profile, image=f'{photo_path.file_id}')
    user_photo.save()

@sync_to_async
def generate_short(telegram_id):
    user_profile = UserProfile.objects.get(telegram_id=telegram_id)
    sentences = re.split(r'(?<=[.!?]) +', user_profile.short_epigraphy)
    tg_id = user_profile.telegram_id
    media_dir = settings.MEDIA_ROOT
    new_directory = os.path.join(media_dir, str(tg_id))
    os.makedirs(new_directory, exist_ok=True)
    big_path = []
    for sentence in sentences:
        name = sentence[:5]
        one_path = generate_one(sentence,new_directory,name)
        big_path.append(one_path)
    image_folder = new_directory
    image_files = [f"{image_folder}/{f}" for f in os.listdir(image_folder) if f.endswith('.jpg')]
    clips = []
    image_duration = 2  # seconds
    for i, image_file in enumerate(image_files):
        clip = ImageClip(image_file).set_duration(image_duration)

        if i > 0: 
            clip = fadein(clip, 1) 
        if i < len(image_files) - 1:  
            clip = fadeout(clip, 1)  
        
        clips.append(clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(f"{image_folder}/output_video.mp4", codec='libx264', fps=24)
    return big_path
    


