# python2exe

the simple method of packaging python project to executable file

## implement to change pics colour to gray and normalize the nam

file structure

|project
    |--imgs_id        # -----运行原始图片存放位置
    |--main           # 打包文件夹
        |--main.exe   #
    |--imgs_result    #------运行后图片存储位置
    |--*.ico          # ------图标

##command of packaging

pyinstaller -D main.spec -i I_img.ico

##runing method：

in the terminal run:dist/mian/main.exe
