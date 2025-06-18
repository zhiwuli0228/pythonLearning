from typing import Dict

user_info: Dict[str, str] = {}

user_info['name'] = input('请输入姓名\n')
user_info['passWord'] = input('密码\n')
user_info['sex'] = input('请输入性别\n')

print(user_info)
