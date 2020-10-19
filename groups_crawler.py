import requests
import psycopg2
import vk_api
from vk_api.execute import VkFunction
from config import VK_TOKEN, version


def vk_session():
    session = vk_api.VkApi(token=VK_TOKEN)
    return session


def get_groups(ids, fields=''):
    code = VkFunction(args=('ids','fields'), code='''
    var ids = %(ids)s;
    var iter = 0;
    var groups = []
    while (iter < 25) {
         groups = groups + API.groups.getById({'group_ids':ids[iter], %(fields)s});
         iter = iter+1;
         
};
    return groups
''')
    #groups = vk_session().method('groups.getById',{'group_ids':ids, 'fields':fields})
    session = vk_session().get_api()
    groups = code(session, ids ,{'fields':fields})
    return groups


def make_str_ids(max_id):
    
    ids = []
    for _ in range(25):
        ids.append(','.join([str(i) for i in range(max_id//25*_,max_id//25*(_+1))]))

    return ids

def get_all_groups():
    con = connect_to_bd()
    flag = True
    max_id = 2026500
    while max_id< 200000000:
        groups_12500 = get_groups(make_str_ids(max_id),fields= ','.join(['description','members_count','trending','verified']))
        for groups in groups_12500:
            for group in groups:
                if group['is_closed'] == 0 and group['name'] != 'DELETED' and 'deactivated' not in group and group['type'] != 'event' and 'members_count' in group:
                    data = ['','','','','','','']
                    group['name'] = group['name'].replace("'",' ')
                    group['description'] = group['description'].replace("'",' ')
                    data[0]=str(group['id'])
                    data[1]=f"'{group['screen_name']}'"
                    data[2]=f"'{group['name']}'"
                    data[3]=f"'{group['description']}'"
                    data[4]=str(group['members_count'])
                    data[5]=str(group['trending'])
                    data[6]=str(group['verified'])
                    writing_to_bd(con, data)

        print(f'Ready {max_id}')
        max_id+=12500

    disconnection_bd(con)

        

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


def writing_to_bd(connection, data):
    cur = connection.cursor()
    data_str = ','.join(data)
    cur.execute(
  f'''INSERT INTO GROUPS (GROUP_ID,SCREEN_ID,NAME,DESCRIPTION,MEMBERS_COUNT,TRENDING, VERIFIED) VALUES ({data_str})'''
)
    connection.commit()


get_all_groups()
print('Allredy Done!')