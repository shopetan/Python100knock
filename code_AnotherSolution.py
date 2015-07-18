#coding:utf-8

print("Please input plain text")
plain = input()

print("Please input key(0~26)")
key = int(input())

code = list(map(lambda x:chr(ord(x)+ key), plain))
code = ''.join(code)
print(code)
