# -*- coding: utf-8 -*-

import sys
import wxpy

sys.setdefaultencoding("utf8")

class WxBot():
    '''
    微信机器人
    '''

    def __init__(self, wxid):
        self.id = wxid

    def login(self):
        self.bot = wxpy.Bot()

    def logout(self):
        self.bot.logout()

    def getFriends(self):
        self.friends = self.bot.friends()
        print(type(self.friends), self.friends)

    def sendMsg(self, who, message):
        friend = self.bot.friends().search(who)[0]
        friend.send(message)

    def sendImg(self, who, img):
        friend = self.bot.friends().search(who)[0]
        friend.send_img(img)




def runBot():
    wx = WxBot(11111)
    wx.login()
    wx.getFriends()
    wx.sendMsg("木小南", "hello".encode("ascii"))
    wx.logout()

if __name__ == "__main__":
    runBot()
