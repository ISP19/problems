## Git fork vs Git clone

### Question

Question 1: What is the difference between git fork and git clone? 

Question 2: Which of the following can you do with your forked repository? (can answer more than 1 choice)
    
    a. Create branches
    
    b. Open pull request
    
    c. Can see commits and branch that have in original repository
    
    d. Make forked repository private
    
    e. Create a local clone of your fork
    
    f. Directly commit to the original repository
    
    g. Pull changes from the original repository

### Answer

Answer 1:

* Forking

    A fork is a copy of a repository that allows you to commit changes without affecting the original project. A forked repository differs from a clone in that a connection exists between your fork and the original repository itself. In this way, your fork acts as a bridge between the original repository and your personal copy where you can contribute back to the original project using Pull Requests.

* Cloning

    The cloned repository exists as a remote location where your project is stored. You can clone your repository to create a local copy on your computer so that you can sync between both the local and remote locations of the project. But if the project is owned by someone else you won't be able to contribute back to it unless you are specifically invited as a collaborator. So that's why you have the forked repo, so you can push changes to it for others to see and review.

Answer 2: a, b, c, e, g

### Reference

* Pro Git book - [Contributing to a Project](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)
* GitHub Community Forum - [Protips](https://github.community/t5/Support-Protips/The-difference-between-forking-and-cloning-a-repository/ba-p/1372)
