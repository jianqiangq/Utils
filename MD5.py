import time
import hashlib as hl

localtime = time.strftime("%Y%m%d", time.localtime())
token = localtime + "31301"
print("token str is " + token)
hash = hl.md5()
hash.update(token.encode('utf-8'))
token_md5 = hash.hexdigest()
print(token_md5)