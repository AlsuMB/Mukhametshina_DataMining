import re

import vk_api


def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def vk_craw(login, password):
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
            word = deEmojify(word)
            if answer.get(word):
                answer[word] = answer[word] + 1
            else:
                answer[word] = 1

    answer = {k: v for k, v in sorted(answer.items(), key=lambda item: item[1])}

    return answer
