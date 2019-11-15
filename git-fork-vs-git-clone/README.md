## Git fork vs Git clone

**Question**

1. What is the difference between git fork and git clone? 

2. Which of the following can you do with your forked repository? (can answer more than 1 choice)
    
    a. Create branches
    
    b. Open pull request
    
    c. Can see commits and branch that have in original repository
    
    d. Make forked repository private
    
    e. Create a local clone of your fork
    
    f. Directly commit to the original repository
    
    g. Pull changes from the original repository

**Answer**

Answer 1 :

* Forking

The forked repository is mostly static. It exists in order to allow you to publish work for code review purposes. You can't do active development in your forked repository because it doesn't exist on your computer, it exists on GitHub's server in the cloud. The changes must then be pulled into the source repository by the project maintainer.

* Cloning

The cloned repository exists as a remote location where your project is stored. You can clone your repository to create a local copy on your computer so that you can sync between both the local and remote locations of the project. But if the project is owned by someone else you won't be able to contribute back to it unless you are specifically invited as a collaborator. So that's why you have the forked repo, so you can push changes to it for others to see and review.

Answer 2: a, b, c, e, g

**Reference**

* Pro Git book - [Contributing to a Project](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)
* GitHub Community Forum - [Protips](https://github.community/t5/Support-Protips/The-difference-between-forking-and-cloning-a-repository/ba-p/1372)
