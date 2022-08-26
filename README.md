# note

## 问题1:迟迟上传不了

**在github上修改过readme.md后，在本地执行git push origin master后会提示：**

```bash
$ git push origin master
To [github](https://so.csdn.net/so/search?q=github&spm=1001.2101.3001.7020).com:taozhuowei/StoreMyToys.git
 ! [rejected]     master -> master (fetch first)
error: failed to push some refs to 'git@github.com:taozhuowei/StoreMyToys.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

 

**解决方式：git pull --rebase origin master 将github修改的文件更新到本地**

```bash
$ git pull --rebase origin master
remote: Enumerating objects: 21, done.
remote: Counting objects: 100% (20/20), done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 17 (delta 4), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (17/17), 3.99 KiB | 5.00 KiB/s, done.
From github.com:taozhuowei/StoreMyToys
 \* branch       master   -> FETCH_HEAD
  5afe506..b843c89  master   -> origin/master
First, rewinding head to replay your work on top of it...
Applying: commit Vue to-do
 
```

**再次提交：git push origin master**

```bash
$ git push origin master
Enumerating objects: 26, done.
Counting objects: 100% (26/26), done.
Delta compression using up to 8 threads
Compressing objects: 100% (22/22), done.
Writing objects: 100% (25/25), 49.42 KiB | 153.00 KiB/s, done.
Total 25 (delta 0), reused 0 (delta 0)
To github.com:taozhuowei/StoreMyToys.git
  b843c89..bc04ef1  master -> master
```


## 问题2:git push的时候出现
2022.8.26
```bash
Connection reset by 20.205.243.166 port 22
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```
**应该网络的问题,打开梯子多试几遍**
