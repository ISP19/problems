## Visualizing the Git commit graph.
### Question
Draw a graph and specify the latest position of HEAD and all branches from the following git command.

```sh
git commit "first commit"
git branch aaa
git checkout master
git commit -m "second commit"
git commit -m "third commit"
git branch bbb
git checkout bbb
git commit -m "forth commit"
git commit -m "fifth commit"
git commit -m "sixth commit"
git checkout master
git commit -m "seventh commit"
git reset HEAD^
git reset HEAD^
git branch ccc
git checkout ccc
git commit -m "eighth commit"
git commit -m "ninth commit"
```

### Answer
![1573566784485](https://user-images.githubusercontent.com/47658385/68677429-b053d380-058e-11ea-9674-1c94fc9f4969.jpg)
- ``` git commit -m "<comment>" ``` is used to save a latest change.
- ``` git branch <name> ``` is used to create a new branch.
- ``` git checkout <specified branch> ``` is used to switch to specified branch.
- ``` git reset HEAD^ ``` is used to move HEAD to previous commit.

**References**
- [Visualizing Git](https://git-school.github.io/visualizing-git/)
