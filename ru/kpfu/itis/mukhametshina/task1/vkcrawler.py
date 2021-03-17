import vk_api

print('Напишите логин')
login = input()
print('Напишите пароль')
password = input()
vk_session = vk_api.VkApi(login, password)

try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

tools = vk_api.VkTools(vk_session)

wall = tools.get_all('wall.get', 8, {'domain': 'itis_kfu'}, limit=25)
answer = {}
for i in range(200):
    words = wall['items'][i]['text'].split(' ')
    for word in words:
        if answer.get(word):
            answer[word] = answer[word] + 1
        else:
            answer[word] = 1

answer = {k: v for k, v in sorted(answer.items(), key=lambda item: item[1])}
for i in answer.keys():
    print(str(i) + " " + str(answer[i]))
