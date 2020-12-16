import re

import phone as phone
from django.contrib.auth.hashers import make_password
from django_redis import get_redis_connection
from requests import Response
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user.models import UserInfo
from user.service import get_user_by_account


class UserModelSerializer(ModelSerializer):

    token = serializers.CharField(max_length=1024, read_only=True, help_text="用户token")
    sms_code = serializers.CharField(max_length=1024, write_only=True)

    class Meta:
        model = UserInfo
        fields = ('id', 'username', 'password', 'phone', 'token', 'sms_code')

        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'username': {
                'read_only': True
            },
            'password': {
                'write_only': True
            },
            'phone': {
                'write_only': True
            },
        }

    def validate(self, attrs):
        # attrs可以获取前端所有参数
        phone = attrs.get('phone')
        password = attrs.get('password')
        sms_code = attrs.get("sms_code")
        # print(sms_code)
        redis_connection = get_redis_connection("sms_code")
        phone_code = redis_connection.get("mobile_%s" % phone)
        print(phone_code)
        a = phone_code.decode('utf-8')
        print(a)
        if a != sms_code:
            raise serializers.ValidationError('code error')
        # 验证手机号
        if not re.match(r'^1[3-9]\d{9}$', phone):
            raise serializers.ValidationError("用户手机号格式不正确")

        #验证密码
        if not re.match(r'^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$', password):
            raise serializers.ValidationError('密码至少包含数字和英文，长度6-20')

        #验证手机号是否存在
        print(333)
        try:
            user = get_user_by_account(phone)
        except UserInfo.DoesNotExist:
            user =None
        print(4444)
        if user:
            print(555)
            raise serializers.ValidationError("手机号已存在")
        return attrs

    def create(self, validated_data):
        #用户信息
        password = validated_data.get('password')
        hash_pwd = make_password(password)
        phone = validated_data.get('phone')
        #添加数据
        user = UserInfo.objects.create(phone=phone, username=phone, password=hash_pwd)
        # 成功的用户生成token 完成自动登录
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)

        return user