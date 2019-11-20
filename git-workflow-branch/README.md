# Branch in git work flow

## Question
From the picture below, please describe what does the label on the left side mean for each branch.

![pic](https://leanpub.com/site_images/git-flow/git-workflow-release-cycle-4maintenance.png)
Credit: leanpub

## Answer

- ## Master Branches
    **Master branch** stores the official release history (abridged version of all history). 

- ## Develop Branches
    **Develop branch** contains all history of the project, use as an integration branch for features.

- ## Feature Branches
    **Feature branch** a branch for each new feature, merge into develop after finish working on it. 
    
- ## Release Branches
    **Release branch** a place to update the documentation and do any other kind of preparation for the upcoming release.
    
- ## Hotfix Branches
    **Hotfix branch** (Maintenance branch) used to quickly fix production releases.

## Reference
1. How Git Flow Works [Click here](https://leanpub.com/git-flow/read?fbclid=IwAR09d77f39fE_iOV9F461FZFius4ubxRxpOFGnBP-L4g5-ve0kJpOLaLDg0#leanpub-auto-git-flow-example)
2. Atlassian [Click here](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)