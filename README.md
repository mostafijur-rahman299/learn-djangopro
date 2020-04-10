# GIT
### Branch:
```
**Create local branch:	
	git branch branch_name
**Create local branch and checkout:
	git checkout -b branch_name
**Create remote branch:
	git push remote_name branch_name
**Delete remote branch:
	git push remote_name --delete branch_name
	or
	git push origin :branch_name
**Force to delete local branch:
	git branch -D branch_name
**Delete local branch safe:
	git branch -d branch_name
**Rename current branch:
	git branch -m new_branch_name
**Merge locally
	git merge branch_name
```
### Commit:
```
** -m for message
** --amend rewrite last commit
** Show commited content
	git show commit_hash
** Soft reset change rekha back a jaoa
	git reset --soft commit_hash
** Hard reset change falai dea back a jaoa
	git reset --hard commit_hash
```
```
**git fetch
	update local repo from the remote but don't merge
**git diff master origin/master
	after downloading the updates, let's see the difference
**git pull
	if happy with those updates,the merge
```

### Stash:
```
jodi kono file temporary vabe safe korte hoi tahola stash bebohar korta hoi
**git stash
**git stash list
**git stash apply or pop
```
```
**Delete all untrack file:
	git clean -f
**Try before delete file:
	git clean -f -n
```
