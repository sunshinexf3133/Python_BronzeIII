#coding:utf-8
#chatserver.py

#note1
#self表示创建的实例本身，在init方法内部，就可以把各种属性绑定到self，因为
#self就指向创建的实例本身,ChatRoom(self)中的self是ChatRoom的一个实例，
#并且创建ChatRoom实例需要一个ChatServer的参数，所以才会传self

class ChatServer(dispatcher):
    """
    聊天服务器
    """

    def __init__(self, port):
        dispatcher.__init__(self)
        #创建socket
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        #监听端口
        self.bind(('', port))
        self.listen(5) 
        self.users = {}
        #note1
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)
