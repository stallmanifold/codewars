select rpad(md5, 64, '1') as md5,
       lpad(sha1, 64, '0') as sha1,
       sha256
from encryption
