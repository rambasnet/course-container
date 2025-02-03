# Docker Container with Git Best Practices for CMU Courses

![Tests](https://github.com/rambasnet/course-container/actions/workflows/ci-test.yml/badge.svg)
[![Code Coverage](https://img.shields.io/codecov/c/github/rambasnet/course-container?label=codecov&logo=codecov)](https://app.codecov.io/gh/rambasnet/course-container)

## Setup

1. Install [Docker](https://docs.docker.com/install/)
2. Create a GitHub repository for your project/course
3. Clone your repository to your local machine
4. Download setup.sh script into your repository and run it
    - `$ cd <your-repository>`
    - `$ curl -o setup.sh https://raw.githubusercontent.com/rambasnet/course-container/main/setup.sh`
    - `$ bash setup.sh`

### Chromebook Setup

- follow the instructions here: [https://www.techrepublic.com/article/install-docker-chromeos/](https://www.techrepublic.com/article/install-docker-chromeos/)
- You may have to explictly activate docker group everytime:
- `$ newgrp docker`

### What does setup.sh do?

1. Clones this repository into your working directory
2. Deep copies the following folders and files from this repository into your working directory:
    - `Dockerfile`
    - `.githooks`
    - `.github`
    - `.mypy.ini`
    - `.flake8`
    - `Makefile`
    - `run-docker.sh`
    - `run-jupyter.sh`
    - `script.sh`
    - `requirements.py`
    - `ci-cd-requirements.txt`
    - `demo-assignments/*`
3. Deletes the cloned repository and other files and folders not listed above

### Configure

1. Update the Dockerfile as needed for your project
    - E.g., if you need to install any Linux packages, add the package to the end of `apt install -y` line
    - after the docker is built, it runs as a non-root user `user` with sudo privileges
    - the default working directory is `/home/user`
    - your repository is mounted to `/home/user/<your-repository>`
    - no password is required for sudo commands

2. Update the Makefile as needed for your project
    - Makefile is used by git hooks to run test before pushing main to GitHub

3. Update the script.sh as needed for your project
    - you may rarely need to change the script.sh file

4. Update the requirements.py as needed for your project
    - this file is used by Docker to install Python packages

5. Update .github/workflows/ci-test.yml as needed for your project
    - this file is used by GitHub Actions to run tests on push to main

6. Update ci-cd-requirements.txt as needed for your project
    - this file is used by GitHub Actions to install Python packages

7. Update .githooks/pre-commit as needed for your project
    - this file is run by git hooks before commmitting to any branch

8. Update .githooks/pre-push as needed for your project
    - this file is run by git hooks before pushing to any branch

## Run Docker

1. `$ cd <your-repository>`
2. `$ bash ./run-docker.sh`

### What does run.sh do?

1. Builds the Docker image
2. Runs the Docker container
3. Mounts your repository to the Docker container
4. Sets the working directory to your repository
5. Configures git to use the git hooks in your repository
6. Runs the script.sh file in the Docker container

## Git Branch Management and Best Practices

- learn more about [git branch management](https://git-scm.com/docs/git-branch)
- CMU advanced courses deosn't allow committing to the main branch
    - only merge and push to main branch allowed
- CMU courses recommend and enforce using a branch name that starts with:
    - `lab|project|assignment|homework|issue|dev|feature|bugfix|improvement|library|prerelease|release|hotfix`
    - `main` - the main branch - only merge and push to main branch allowed
        - the main branch is protected and cannot be deleted
        - the main branch is the default branch
        - the main branch is the production branch
        - the main branch is the release branch from which tags and releases are made
    - `issue/<#>` - the issue branch
        - the issue branch is used to fix an issue, bug, or add a new feature
        - the issue branch is created from the main branch
        - the issue branch is merged to the main branch
    - `feature/<feature-name>` - the feature branch
    - `bug/<bug-name>` - the bug branch
    - `hotfix/<hotfix-name>` - the hotfix branch
    - `release/<release-name>` - the release branch
    - `lab/<lab-name>` - the lab branch for lab courses
    - `project/<project-name>` - the project branch for various sub projects within a course
    - `assignment/<assignment-name>` - the assignment branch for various assignments within a course

### Create a new branch, track it, and push it to GitHub

1. `$ cd <your-repository>`
2. `$ git checkout main`
3. `$ git pull`
4. `$ git branch` # list all branches
5. `$ git checkout -b <new-branch-name>` # create a new branch and switch to it
6. `$ git push -u origin <new-branch-name>` # push the new branch to GitHub and set the upstream
7. `$ git add <file-name>` # add a file to the staging area
8. `$ git commit -m "<commit-message>"` # commit the changes
9. `$ git push` # push the changes to GitHub to the current branch

### Rename a branch

1. `$ cd <your-repository>`
2. `$ git branch -m <old-branch-name> <new-branch-name>` # rename a branch; optional old-branch-name if you're on the old-branch-name
3. `$ git push origin -u <new-branch-name>` # push the new branch to GitHub and set the upstream

### Switch to an existing branch

1. `$ cd <your-repository>`
2. `$ git checkout <branch-name>` - switch to an existing branch

### List all branches

1. `$ cd <your-repository>`
2. `$ git branch` - list all branches
3. `$ git branch -a` - list all branches including remote branches
4. `$ git branch -r` - list all remote branches

### Merge a branch to main

- committing and pushing to main is not allowed
- you must work on a branch and merge it to main after all the checks and tests pass on the branch
- you can then push and tag the main branch

1. `$ cd <your-repository>`
2. make sure your tests pass on the branch you want to merge to main
3. `$ git checkout main`
4. `$ git pull`
5. `$ git merge <branch-name>` # merge the branch to main
6. `$ git push` # push the changes to GitHub

### Delete a branch

- you can only delete a branch that is not currently checked out
- you can keep the merged branch or delete it
- for courses, keep all the branches as proof of your work

1. `$ cd <your-repository>`
2. `$ git branch -d <branch-name>` # delete the branch locally
3. `$ git push origin --delete <branch-name>` # delete the branch on GitHub

### Revert a commit

- you can revert a commit on any branch

1. `$ cd <your-repository>`
2. `$ git checkout <branch-name>` # switch to the branch
3. `$ git log` # find the commit hash you want to revert
4. `$ git revert <commit-hash>` # revert the commit
5. `$ git push` # push the changes to GitHub

### Revert a merge

- you can revert a merge on any branch

1. `$ cd <your-repository>`
2. `$ git checkout <branch-name>` # switch to the branch
3. `$ git log` # find the commit hash you want to revert
4. `$ git revert -m 1 <commit-hash>` # revert the merge commit
5. `$ git push` # push the changes to GitHub


### Revert a merge conflict

- you can revert a merge conflict on any branch

1. `$ cd <your-repository>`
2. `$ git checkout <branch-name>` # switch to the branch
3. `$ git log` # find the commit hash you want to revert
4. `$ git revert -m 1 <commit-hash>` # revert the merge commit
5. `$ git push` # push the changes to GitHub


### Git Tagging

- learn more about [git tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
- Tags are used to mark a specific point in the history of a repository like a release
- Tags are immutable and cannot be changed once created
- Tags once created needs to be pushed to GitHub
- Assignments/Labs/Projects completions can be tagged and pushed to GitHub as a release

### Create a tag

- follow the naming convention for tags specified in the course
- must tag to submit the assignment/lab/project
- tag name must be unique across all branches

1. `$ cd <your-repository>`
2. `$ git tag -a <tag-name> -m "<tag-message>"` # create a tag
    - e.g., `$ git tag -a assignment-1 -m "Final Submission of Assignment/1"`
3. `$ git push origin <tag-name>` # push the tag to GitHub
4. git tag -d <tag-name> # delete a tag locally
5. git tag # show all tags

## Kattis-cli Setup and Usage

- Kattis-cli is already installed in the Docker container
- [See this document for Kattis setup and usage](https://github.com/rambasnet/kattis-cli)
