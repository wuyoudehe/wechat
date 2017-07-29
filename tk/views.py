# -*- coding: utf-8 -*-
#import json, tracebacK, requests
from __future__ import unicode_literals

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
import json,requests
tuling_key = '7efc4394c8ba4c93a41db810bcc70af1'
tuling_secret = 'd5bc9d529662b8d7'
tuling_url = 'http://www.tuling123.com/openapi/api'
WECHAT_TOKEN = 'zqxt'
AppID = 'wx0c527d441612f64d'
AppSecret = 'ba973131b0411f1a2410f712910307d7'
# 实例化 WechatBasici
wechat_instance = WechatBasic(
	token=WECHAT_TOKEN,
	appid=AppID,
	# 关注事件以及不匹配时的默认回复
	appsecret=AppSecret
)


@csrf_exempt
def index(request):
	if request.method == 'GET':
		# 检验合法性
		# 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
		signature = request.GET.get('signature')
		timestamp = request.GET.get('timestamp')
		nonce = request.GET.get('nonce')

		if not wechat_instance.check_signature(
				signature=signature, timestamp=timestamp, nonce=nonce):
			return HttpResponseBadRequest('Verify Failed')

		return HttpResponse(
			request.GET.get('echostr', ''), content_type="text/plain")

	# 解析本次请求的 XML 数据
	try:
		wechat_instance.parse_data(data=request.body)
	except ParseError:
		return HttpResponseBadRequest('Invalid XML Data')

	# 获取解析好的微信请求信息
	message = wechat_instance.get_message()  # 关注事件以及不匹配时的默认回复
	response = wechat_instance.response_text(
		content=(
			'感谢您的关注！\n回复【功能】两个字查看支持的功能，还可以回复任意内容开始聊天'
			'\n【<a href="http://www.ziqiangxuetang.com">自强学堂手机版</a>】'))
	if isinstance(message, TextMessage):
		content = message.content.strip()
		if content == '功能':
			reply_text = (
				'目前支持的功能：\n1.自动回复 ，'
				'\n'
				'2. 其他\n')
		else:
			tuling_data = {'key': tuling_key, 'info': content}
			reply_text = json.loads(requests.post(tuling_url, data=tuling_data).text)['text']
		response = wechat_instance.response_text(content=reply_text)

	return HttpResponse(response, content_type="application/xml")
