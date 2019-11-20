# githubosint
Hunt for sensitive information in github repostiroies 

Introduction:

GitHub is used by millions of users to host and share their codes. It’s fantastic, but sometimes you/developers/code owner can accidentally dump confidential information in public repository which can be a disaster. 
There are many incidents where confidential data was leaked on GitHub. You can’t eliminate human error but can take action to reduce that.

How do you ensure your repository doesn’t contain a password or key?:

Searching with known list of passwords
Search with simple Github-Dorks to find the repositories matching with specific keyword.


How to automate the GitHub-dorks search's :

simple answer is  write a python script to scan the organization GitHub repository with each and every dork command for every iteration. 
In this project i used PyGitHub. PyGitHub is a Python (2 and 3) library to access the GitHub API v3 and Github Enterprise API v3. 
This library enables you to manage GitHub resources such as repositories, user profiles, and organizations in your Python applications.
