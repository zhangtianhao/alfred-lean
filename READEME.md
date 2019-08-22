[toc]

> 使用一个库来快速实现自己的 alfred workflow.

[库地址](https://github.com/deanishe/alfred-workflow)


1. 从 [github](https://github.com/deanishe/alfred-workflow.git) 将代码 clone 下来。
```bash
git clone https://github.com/deanishe/alfred-workflow.git
```

2. 创建一个文件夹作为这个项目的根目录
```bash
mkdir alfred-lean
```  
这个根目录下的文件如下：

    alfred-lean
        info.plist
        icon.png
        myscript.py
        workflow/
            __init__.py
            background.py
            notify.py
            Notify.tgz
            update.py
            version
            web.py
            workflow.py
            
                      
其中 `workflow/` 目录以及下面的文件可以从前面 clone 下的项目中拷贝过来。
