from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from users.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    api_url = urlunparse(('http', 'api.vk.com', 'method/users.get', None,
                          urlencode(
                              OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'personal', 'photo_200')),
                                          access_token=response['access_token'],
                                          v=5.131)), None))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    data_sex = {
        1: UserProfile.FEMALE,
        2: UserProfile.MALE,
        0: None
    }
    user.userprofile.gender = data_sex[data['sex']]

    if data['about']:
        user.userprofile.about = data['about']

    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
    age = timezone.now().date().year - bdate.year

    if age < 18:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    user.age = age

    langs = data['personal']['langs']
    if langs:
        user.userprofile.langs = langs[0] if len(langs[0]) > 0 else 'RU'

    # if data['photo_200']:
    #     short_path_photo = f'{settings.MEDIA_ROOT_SHORT}/users_images/{user.id}.jpeg'
    #     path_photo = f'users_images/{user.id}.jpeg'
    #
    #     if not os.path.exists(short_path_photo) and not user.image:
    #         with open(short_path_photo, 'wb') as ph:
    #             photo_response = requests.get(data['photo_200'])
    #             ph.write(photo_response.content)
    #             user.image = path_photo
    path_photo = f'{user.id}.jpg'
    with open(f'media/users_images/test.txt', 'w') as ph:
        ph.writelines("test")

    photo = data['photo_200']
    if photo:
        photo_response = requests.get(photo)
        path_photo = f'{user.id}.jpg'
        with open(f'media/users_images/{path_photo}', 'wb') as ph:
            ph.write(photo_response.content)
        user.image = path_photo
    user.save()
