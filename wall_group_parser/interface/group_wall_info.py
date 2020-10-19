import requests
import psycopg2
import vk_api
from .config import version,login,pswd


class VK_API():

    def vk_session(login,pswd):
        session = vk_api.VkApi(login, pswd)
        session.auth()
        return session


    def connect_to_bd():
        con = psycopg2.connect(
        database="vk_groups", 
        user="postgres", 
        password="348275723", 
        host="127.0.0.1", 
        port="5432"
        )
        return con


    def disconnection_bd(connection):
        connection.close()


    def get_group_info(link):
        '''Получение информации о группе'''
        group_ids = link
        try:
            session = VK_API.vk_session(login,pswd)
        except:
            return {'error':'Не удалось авторизироваться в вк'}
        
        group_info = session.method('groups.getById', {'group_ids':group_ids,'fields':'description,members_count,status,wall'})[0]
        
        if 'deactivated' in group_info:
            return {'error':'Это сообщество не может быть обработано'}
        
        else:
            group_info.pop('photo_50')
            group_info.pop('is_member')
            group_info.pop('photo_100')
            group_info.pop('photo_200')
            group_info.pop('is_admin')
            group_info.pop('is_advertiser')
            if group_info['is_closed'] == 1:
                group_info['is_closed'] = True
            else:
                group_info['is_closed'] = False
            return group_info


    def get_wall(owner_id,count):
        '''Получение списка постов'''
        try:
            session = VK_API.vk_session(login,pswd)
        except:
            return {'error':'Не удалось авторизироваться в вк'}

        try:
            group_wall = session.method('wall.get', {'owner_id':owner_id,'count':count})
            
            return group_wall
        except:
            return {'error':'У вас нет доступа к стене сообщества'}


#print(VK_API.get_wall(-g['id'],1))
#print(VK_API.get_group_info('https://vk.com/club3'))