# coding: utf-8

from goolabs import GoolabsAPI
import sys

APPID = sys.argv[1]
api = GoolabsAPI(APPID)

req = api.hiragana(sentence='ファイナルファンタジーⅤをやって、うるせえぶっ殺すぞ！', output_type='hiragana')

print(req['converted'])
# ふぁいなるふぁんたじーごを やって、 うるせえぶっころすぞ！
