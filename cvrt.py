# coding: utf-8

from goolabs import GoolabsAPI
import sys

APPID = sys.argv[1]
api = GoolabsAPI(APPID)

req = api.hiragana(sentence='ファイナルファンタジーⅤ', output_type='hiragana')

print(req['converted'])
