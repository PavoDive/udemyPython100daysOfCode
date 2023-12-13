# This lesson is about using git

Initialize git:


```shell
git init
```

Check the overall status of the project:

```shell
bash status
```

Add a file to the stagin area:

```shell
git add chapter1.txt
```

Commit changes with a message

```shell
git commit -m "message in present tense"
```

Check what was done:

```shell
git log
```

After creating files `chapter2.txt` and `chapter3.txt`:

Commit all non-staged files in the directory:

```shell
git add .
```
Commit the new changes:

```shell
git commit -m "complete chapters 2 and 3"
```

And check that everything worked:

```shell
git log
```

Suppose I mess chapter 3 because I felt asleep in my keyboard.

Check the differences:

```shell
git diff chapter3.txt 
```

Restore `chapter3.txt` to the previous version that was commited:

```shell
git checkout chapter3.txt 
```

I just created a dummy repo in github, so I can use it as a remote for my local git:

```shell
git remote add origin https://github.com/PavoDive/day70_git.git
git branch -M main
```

Now I can push my local work to github:

```shell
git push -u origin main
```

## Ignoring files

Imagine I have a file with some secret keys or passwords `secrets.txt`. I can avoid git tracking it by adding its name to a special file called `.gitignore`. This file accepts comments (lines starting with #) and wildcards.

I will create another file, say `chapter4.txt` to demonstrate the value of `.gitignore`.

Github has a very interesting repo called "gitignore" with many example templates of gitignore files.

```shell
git add .
git status
git push -u origin main
```

## Cloning

We may want to clone a pice of open software for different reasons: modify the software, enhance it or customize it, etc.

```shell
git clone http://url.of/the/repo 
```

## Branching

Sometimes we are working on features or bug fixes that may break our code, therefore we don't want to do it in the main branch, lest we break everything. We may have one or multiple branches, in which we develop a feature, and only merge it with the main branch once we're confident that it works and doesn't break anything.

In order to display what branches there are:

```shell
git branch 
```

If I want to create a new branch:

```shell
git branch alien-plot 
```

If I want to switch to a specific branch:

```shell
git checkout alien-plot
```

Once switched to the new (or specific branch), I can start making modifications to the files.

In order to merge a branch, I have to switch to the main (or target branch)

```shell
git checkout main
git merge alien-plot
```

## Cherry-picking, rebasing and othr stuff

[https://learngitbranching.js.org/](https://learngitbranching.js.org/)

**REBASING** is an additional form of combining work between branches.  I essentially moves a branch _in front_ of another.

```shell
git branch xyz
git checkout xyz
git commit -m "this commits into xyz branch"
git checkout main
git commit -m "this one commits to main"
git checkout xyz
git rebase main
```

The last line moves the xyz commit beyond the last main commit.

**HEAD**: is the name of the currently checked out commit: the commit I'm working on.
It's possible to detach head from a branch, and attach it to a commit.

```shell
git checkout HASH-OF-COMMIT 
```

**RELATIVE REFERENCES**: it's better to use relative references than long hashes.

- `^` moves upward one commit. saying `main^` is equivalent to say "the first parent of main". `main^^` is the "second parent (grandparent) of main".
- `~4` moves upward 4 commits

```shell
git checkout HEAD^ 
```

## Reversing changes

`git reset` moves back in history, as if the commit did never occur.

```shell
git reset HEAD~1 
```

`git revert` works differently as other people may be working on previous commits, so I can't simply reset them:

```shell
git revert HEAD 
```

actually creates a new commit that happens to reverse the changes in the previous one.

## Forking and pull-requests

 forking repos and doing pull requests.
