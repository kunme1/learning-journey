# 每日学习 GitHub 上传命令

在当天的笔记整理、代码检查和文件保存都完成后，打开 PowerShell，按下面的顺序操作。这个流程适用于 `learning-journey` 仓库的 `main` 分支。

## 1. 进入仓库并查看改动

```powershell
Set-Location -LiteralPath 'D:\专业技能\learning-journey'
git status --short --branch
```

确认分支是 `main`，并查看新增、修改和删除的文件。

## 2. 选出本次要上传的文件

如果这次要提交列表里的全部改动，运行下面两条。

```powershell
git add -A
git diff --cached --name-status
```

如果只想提交某节课，把第一条换成 `git add -- '相对于仓库根目录的文件或目录路径'`。路径有空格时保留引号。第二条会列出实际进入这次提交的文件，提交前核对一遍。

## 3. 提交并推送

```powershell
git commit -m "补充 Python 包与模块的学习笔记和练习"
```

把引号里的文字换成当天实际学的内容。看到 `[main 提交编号]` 后，继续推送到 GitHub。

```powershell
git push origin main
```

如果本地已经提交过，只需要执行这条推送命令。`LF will be replaced by CRLF` 是换行符提醒，看到它以后仍然可以检查提交结果并继续推送。

## 4. 确认上传完成

```powershell
git status --short --branch
git log -1 --oneline
```

本地分支与远端同步后，状态首行通常是 `## main...origin/main`，没有 `[ahead 数字]`。也可以打开 [GitHub 的 main 分支](https://github.com/kunme1/learning-journey/tree/main)，确认最新提交号和本地输出一致。
