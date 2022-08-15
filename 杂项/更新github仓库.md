改自知乎

## 1：git status

进入到需要更新的目录下，输入git status，查看文件修改的状态。红色的就是修改过的文件。

![img](https://pic2.zhimg.com/80/v2-5b6735fed3dde1918158c9c220165f09_1440w.jpg)

## 2：git add -A

键入git add *，把所有文件都加入，这时候在输入git status，就看到编程了绿色。这个时候文件已经添加都本地仓库了

![img](https://pic2.zhimg.com/80/v2-959ffd790aba1097dd0e99c522369959_1440w.jpg)

## 3：git commit -m "update".

将add的文件commit到仓库

![img](https://pic2.zhimg.com/80/v2-754dce4bfcbf0b0123f379e1d53e35d5_1440w.jpg)

## 4：git push -u origin master

将代码上传到GitHub。

## 5：备注：

1：如果遇到commit 过的，但是没有push成功的文件。 使用git reset HEAD^1 回退到上个版本

2：如果遇到没有push 成功的，报错如下，并且确信只有你一个人在操作GitHub时，进行强制push . 输入 git push -f origin main.

![img](https://pic3.zhimg.com/80/v2-3a869cb8506348b5b39101924d69b88e_1440w.jpg)