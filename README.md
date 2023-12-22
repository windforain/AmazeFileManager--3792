# AmazeFileManager-3.8.4-#3792



## 脚本运行参数

`python script-#3792.py abc`

其中，abc为模拟器名或设备名，例如

`python script-#3792.py emulator-5554`



## 其他

### 新BUG

在复现该BUG的过程中，我发现了一个3.8.4版本没有，而最新版本3.8.5存在的BUG。

该BUG依然与SSH/SFTP连接有关，在和苏老师交流后提交了Issue，目前（12/22）已被开发者Confirm

详情如下：

[SSH/SFTP connection shows "No File" · Issue #4018 · TeamAmaze/AmazeFileManager (github.com)](https://github.com/TeamAmaze/AmazeFileManager/issues/4018)

### 文件修改

我所提交的分支内，将gradle下载链接用腾讯云镜像替换，加速构建，如下图所示：

![image-20231222180312170](C:\Users\微笑\AppData\Roaming\Typora\typora-user-images\image-20231222180312170.png)

注释掉的那行为原本的，下边那行是新加的，除此以外没有任何更改。

