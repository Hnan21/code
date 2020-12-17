import requests

from edu_api.settings import constants


class Message(object):
    def __init__(self, api_key):
        self.api_key = api_key
        # 短信发送的接口
        self.single_send_url = constants.SINGLE_SEND_URL

    def send_message(self, phone, code):
        """
        短信发送
        :param phone: 手机号
        :param code: 验证码
        :return:
        """
        params = {
            "apikey": self.api_key,
            "mobile": phone,
            "text": "【蒋浩楠test】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }
        res = requests.post(self.single_send_url, data=params)
        print(res)

if __name__ == '__main__':
    message = Message(constants.API_KEY)
    message.send_message('15291222662', '123456')