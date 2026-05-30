#!/bin/bash
#datime=$(date "+%Y-%m-%d %H:%M")
datime=$(date "+%Y年%m月%d日 %H:%M")
cd ~/S1PlainTextBackup
#find ./ -type d -empty -delete
# 设置环境变量，仅本次 commit 生效
export GIT_AUTHOR_NAME="Anonymous"
export GIT_AUTHOR_EMAIL="anonymous@example.com"
# committer 也需要设置，否则可能仍用原身份
export GIT_COMMITTER_NAME="Anonymous"
export GIT_COMMITTER_EMAIL="anonymous@example.com"
git add .
git commit -m "[脚本]自动上传于 $datime"
echo "git commit: 上传于 $datime"
git push origin master
echo "finished..."

