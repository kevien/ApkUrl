# -*- coding: UTF-8 -*-
#!/usr/bin/python
#__author__ = 'croxy'
import os
import re
import optparse
import sys


def find_file_text(root_dir):
    regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    suffix=['xml','smali','txt','log']
    blacklist = 'android.com|umeng.com|weibo.com|weibo.cn|xmlpull.org|alipay.com|apache.org|qq.com|w3.org|umsns.com|umeng.co|myapp.com|soso.com|alipay.net|ronghub.com|baidu.com|alipaydev.com|example.com|skyhookwireless.com|google.com|qplus.com|jivesoftware.com|sina.cn'
    blacklistre = re.compile(blacklist)
    for root,dirs,files in os.walk(root_dir):
        for file in files:
            file_suffix=file[file.find('.')+1:len(file)]
            if file_suffix in suffix:
                file_obj=open(os.path.join(root, file)).read()
                urls = regex.findall(file_obj)
                if urls:
                    for i in range(len(urls)):
                        if not blacklistre.findall(urls[i]):
                            print urls[i]


def apktosmail(apk):
    apkname = apk[:-4]
    cmd = 'java -jar ./script/apktool.jar d %s >/dev/null 2>&1' %apk
    os.popen(cmd)
    find_file_text(apkname)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'python %s apkname' %(sys.argv[0])
        sys.exit(0)
    else:
        apktosmail(sys.argv[1])

