'''
ウェルノウンポート（0~1023）
登録済みポート（1024~49151）
動的・プライベートポート番号（49152~65535）
'''

import socket

'''
AF_INET	    IPv4 によるソケット
AF_INET6	IPv6 によるソケット
AF_UNIX	    ローカルなプロセス間通信用のソケット
AF_INET	    デバイスレベルのパケットインターフェース

SOCK_STREAM	順序性と信頼性があり、双方向の接続されたバイトストリーム（byte stream）を提供する(TCP)
SOCK_DGRAM	データグラム（接続、信頼性なし、固定最大長メッセージ）をサポートする(UDP)
フロー図->https://qiita.com/__init__/items/5c89fa5b37b8c5ed32a4
'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50007))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if not data:
                    break
                print('data : {}, addr: {}'.format(data, addr))
                # クライアントにデータを返す(b -> byte でないといけない)
                conn.sendall(b'Received: ' + data)

# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#     s.bind(('127.0.0.1', 50007))
#     while True:
#         data, addr = s.recvfrom(1024)
#         print("data: {}, addr: {}".format(data, addr))
