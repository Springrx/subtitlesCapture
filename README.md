# subtitlesCapture
Capture subtitles from videos

如何运行：
自动下载b站视频：python getVideo.py
需要在cookies.txt中写入b站的cookie信息


如何将text转换为embedding？
1、在test.txt中写入使用的句子
2、安装[all-MiniLM-L6-v2模型](https://blog.csdn.net/m0_65609016/article/details/134020029)可以直接进入链接看方法二
3、安装faiss等必要的包
4、运行python textToEmbedding.py