# python2exe
the method of packaging python project to executable file

#实现图片灰化及统一命名的可执行文件
目录结构
|project
    |--imgs_id        # -----运行原始图片存放位置
    |--main           # 打包文件夹
        |--main.exe   #
    |--imgs_result    #------运行后图片存储位置
    |--*.ico          # ------图标

#打包命令
pyinstaller -D main.spec -i I_img.ico

#运行方法：
终端运行dist/mian/main.exe即可
