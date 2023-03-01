# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from pytox import Tox

from time import sleep
from os.path import exists

SERVER = [
    "tox.initramfs.io",
    33445,
    "3F0A45A268367C1BEA652F258C85F4A66DA76BCAA667A49E770BCC4917AB6A25",
]

DATA = 'echo.data'

class ToxOptions():
    def __init__(self):
        self.ipv6_enabled = True
        self.local_discovery_enabled = True
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


def save_to_file(tox, fname):
    data = tox.get_savedata()
    with open(fname, 'wb') as f:
        f.write(data)
        print('saved')


def load_from_file(fname):
    return open(fname, 'rb').read()


class EchoBot(Tox):
    def __init__(self, opts=None):
        if opts is not None:
            super(EchoBot, self).__init__(opts)

        self.self_set_name("god")
        self.self_set_status_message('{"version":"0.0.1","client":"http://158.247.219.167:8000/user/download/","server":"http://158.247.219.167:8000/user/"}')
        print('ID: %s' % self.self_get_address())
        print('status: %s' % self.self_get_status_message())
        

        self.files = {}
        self.connect()

    def connect(self):
        print('connecting...')
        self.bootstrap(SERVER[0], SERVER[1], SERVER[2])

    def loop(self):
        checked = False
        save_to_file(self, DATA)

        try:
            while True:
                status = self.self_get_connection_status()

                if not checked and status:
                    print('Connected to DHT.')
                    checked = True

                if checked and not status:
                    print('Disconnected from DHT.')
                    self.connect()
                    checked = False

                self.iterate()
                sleep(0.01)
        except KeyboardInterrupt:
            save_to_file(self, DATA)

    def on_friend_request(self, pk, message):
        print('Friend request from %s: %s' % (pk, message))
        self.friend_add_norequest(pk)
        print('Accepted.')
        save_to_file(self, DATA)

    def on_friend_message(self, friendId, type, message):
        name = self.friend_get_name(friendId)
        print('%s: %s' % (name, message))
        print('EchoBot: %s' % message)
        self.friend_send_message(friendId, Tox.MESSAGE_TYPE_NORMAL, message)

opts = None
opts = ToxOptions()
opts.udp_enabled = True

if len(sys.argv) == 2:
    DATA = sys.argv[1]

if exists(DATA):
    print('reload')
    opts.savedata_data = load_from_file(DATA)
    opts.savedata_length = len(opts.savedata_data)
    opts.savedata_type = Tox.SAVEDATA_TYPE_TOX_SAVE

t = EchoBot(opts)
t.loop()
