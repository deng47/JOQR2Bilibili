# JOQR2Bilibili

upload_sub.py 主程序

json 包含字幕的文件

vtt2json.sh 把vtt字幕转成json的shell脚本

cookie 当然不会上传到github了


测试中：

测试从youtube下载vtt格式字幕，然后转换成json格式，再利用b站新的外挂字幕功能，上传到b站视频

目前问题：

[deng47@myhost JOQR2Bilibili]$ ./upload_sub.py

{"code":79013,"message":"字幕时间不合法","ttl":1}

貌似因为b站字幕不支持时间重叠，正在想办法解决
