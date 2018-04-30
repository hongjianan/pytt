# -*- coding: utf-8 -*-
'''
    163邮箱的密码是，授权码和登录密码不一样
'''
import sys
import string
from smtplib import SMTP

class Mail():
    '''

    '''
    def __init__(self, host, port = 25):
        self.server = SMTP()
        self.server.connect(host, str(port))
        # self.server.starttls()  # 启动安全传输模式

    def login(self, user, passwd):
        self.user = user
        return self.server.login(self.user, passwd)

    def send(self, To, Subject, text):
        body = string.join((
            "From: %s" % self.user,
            "To: %s" % To,
            "Subject: %s" % Subject,
            "",
            text
            ), "\r\n")
        return self.server.sendmail(self.user, [To], body)

    def close(self):
        return self.server.quit()

def test():
    passwd = sys.argv[1]
    server = Mail("smtp.163.com")
    server.login("hjnhong@163.com", passwd)
    server.send("1429934448@qq.com", "python mail test", "11111111")
    server.close()
    print("email send success")


if __name__ == "__main__":
    test()
