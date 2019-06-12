#!/usr/bin/python
# -*- coding: UTF-8 -*-

import itchat

itchat.auto_login(hotReload=True)

# author = itchat.search_friends(nickName='LittleCoder')[0]

chatRooms = itchat.get_chatrooms(update=True)
friends = itchat.get_friends(update=True)
chatName1 = "铲屎官联络站🐈🐩"
chatName3 = 'Yocn'
chat1 = ""
chat3 = ""
for room in chatRooms:
    nickname = room["NickName"]
    chatName = room["UserName"]
    if chatName1 == nickname.encode("utf-8"):
        chat1 = chatName
        print "群聊", chatName, chatName1, chat1
for friend in friends:
    nickname = friend["NickName"]
    chatName = friend["UserName"]
    # print "好友", friend["UserName"], friend["NickName"]
    if chatName3 == nickname.encode("utf-8"):
        chat3 = chatName
        print "好友", chatName, chatName3, chat3

itchat.send_msg(u'666', toUserName=chat3)
itchat.add_friend(u'吹风机儿', verifyContent=u'小号，从itchat发起的好友请求')
# itchat.run()
