import requests
from datetime import datetime, timedelta
from django.conf import settings


def _request_to_api(method: str, params: str, token: str, version: float) -> dict:
    """Make request to vk API"""
    response = requests.get(f'https://api.vk.com/method/{method}?{params}&access_token={token}&v={version}')
    return response.json()


def get_group_info(link: str) -> dict:
    """Method return vk group information by group link"""
    group_ids = link.split('/')[-1]
    group_info = _request_to_api(
        method='groups.getById',
        params=f'group_ids={group_ids}&fields=description,members_count,status,wall',
        token='66320aec66320aec66320aec2566468bc56663266320aec39bcc3108c904fe8a5860896',
        version=settings.VK_API_VERSION
    )['response'][0]
    not_need_fields = ['photo_100', 'photo_50', 'wall', 'type']
    group_info = {key: value for key, value in group_info.items() if key not in not_need_fields}
    return group_info


def get_best_worst_meme(domain: str, token: str, count: int = 30) -> list:
    """Return list of most(on place 1) and less(on place 0) liked memes
    of the group at last 24 hours (not advertising)"""
    memes = _request_to_api(
        method='wall.get',
        params=f'domain={domain}&count={count}&offset=1',
        token=token,
        version=settings.VK_API_VERSION
    )['response']['items']
    memes_last_24 = [mem for mem in memes
                     if mem['date'] > datetime.timestamp(datetime.now()-timedelta(days=1)) and
                     mem['marked_as_ads'] != 1]
    like_values = [mem['likes']['count'] for mem in memes_last_24]
    output_memes = [mem for mem in memes_last_24
                    if mem['likes']['count'] == max(like_values) or
                    mem['likes']['count'] == min(like_values)]
    not_need_fields = ['owner_id', 'marked_as_ads', 'post_type', 'copy_history', 'post_source', 'attachments', 'donut',
                       'short_text_rate', 'carousel_offset']
    format_output_memes = []
    for mem in output_memes:
        format_output_memes.append({key: value for key, value in mem.items() if key not in not_need_fields})
    return sorted(format_output_memes, key=lambda mem: mem['likes']['count'])


# print(get_group_info(link='https://vk.com/the_gates_of_orgrimmar'))
# print(get_best_worst_meme('https://vk.com/chop.choppp',
# count=100, token='66320aec66320aec66320aec2566468bc56663266320aec39bcc3108c904fe8a5860896'))
