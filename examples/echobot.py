from pytox import Tox

class ToxOptions(object):
    def __init__(self):
        self.ipv6_enabled = True
        self.udp_enabled = True
        self.proxy_type = 0  # 1=http, 2=socks
        self.proxy_host = ''
        self.proxy_port = 0
        self.start_port = 0
        self.end_port = 0
        self.tcp_port = 0
        self.savedata_type = 0  # 1=toxsave, 2=secretkey
        self.savedata_data = b''
        self.savedata_length = 0


class EchoBot(Tox):
    def __init__(self, opts):
        super(EchoBot, self).__init__(opts)

    def loop(self):
        while True:
            self.iterate()
            time.sleep(0.03)

    def on_friend_request(self, pk, message):
        print 'Friend request from %s: %s' % (pk, message)
        self.friend_add_norequest(pk)
        print 'Accepted.'

    def on_friend_message(self, fid, message):
        name = self.self_get_name(fid)
        print '%s: %s' % (name, message)
        print 'EchoBot: %s' % message
        self.friend_send_message(fid, Tox.MESSAGE_TYPE_NORMAL, message)


EchoBot(ToxOptions()).loop()
