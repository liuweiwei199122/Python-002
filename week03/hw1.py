# 要求：编写一个基于多进程或多线程模型的主机扫描器。

# 使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
# 使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
# IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
# 需考虑网络异常、超时等问题，增加必要的异常处理。
# 因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。
# 命令行参数举例如下：
# python3 test.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100

# python3 test.py -n 10 -f tcp -ip 10.9.58.162 -w result.json
import os,re
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor,TimeoutError
import time
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-f', type=str, default = None)
parser.add_argument('-ip', type=str, default = None)
parser.add_argument('-n', type=int)
parser.add_argument('-w', type=str)
args = parser.parse_args()
#print(args.f, args.ip, args.n,args.w)
def ping(i):
    pat = re.compile(r'0 received')
    ip = f'192.168.0.{i}'
    res = os.popen(f'ping -w 2 {ip} 2> /dev/null').readlines()
    text = ','.join(res)
    res = pat.search(text)
    if res is None:
        print(ip)

def tcp(port):
    pat = re.compile(r'succeeded')
    res = os.popen(f'nc -nvz {args.ip} {port} 2> /dev/null').readlines()
    text = ','.join(res)
    res = pat.search(text)
    if res is not None:
        if args.w is not None:
            with open(f'./{args.w}',mode='a+',encoding='utf-8') as f:
                f.write(port)

if args.f == 'ping':
    with ThreadPoolExecutor(args.n) as executor:
        try:
            executor.map(ping, [x for x in range(1,5)], timeout=3)
        except TimeoutError:
            print('网络超时')
elif args.f == 'tcp':
    with ThreadPoolExecutor(args.n) as executor:
        try:
            executor.map(tcp, [x for x in range(80,83)], timeout=3)
        except TimeoutError:
            print('网络超时')
    
else:
    print('参数错误')


