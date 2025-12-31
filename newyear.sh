git checkout --orphan newyear
git add -A
git commit -m "新年清理旧提交历史"
git branch -D master
git branch -m master
git push -f origin master