# coding: utf-8

from goolabs import GoolabsAPI
import sys
import re


def multiple_replace(text, adict):
    '''
    一度に複数のパターンを置換する関数
    text中からdicのkeyに合致する文字列を探し、対応の値で置換して返す
    '''
    rx = re.compile('|'.join(adict))

    def dedictkey(text):
        '''
        マッチした文字列の元であるkeyを返す
        '''
        for key in adict.keys():
            if re.search(key, text):
                return key

    def one_xlat(match):
        return adict[dedictkey(match.group(0))]

    return rx.sub(one_xlat, text)


original_text = '大変だ！抽選10回もできるぞ！（基本5回、ツイートで5回）'

trans_tone = {
    'あい': 'えぇ',
    'かい': 'けぇ',
    'さい': 'せぇ',
    'たい': 'てぇ'
}

APPID = sys.argv[1]
api = GoolabsAPI(APPID)

req = api.hiragana(sentence=original_text, output_type='hiragana')

after = multiple_replace(req['converted'], trans_tone)

print('Before:\t' + original_text)
print('After:\t' + after)
