import os

print("--------------------------------------")
user_name = input("User: ") # github user name
repo_name = input("Repository: ") # github repository

# Create the project folder
create_repo_string = "mkdir {}&&".format(repo_name)
create_repo_string += "cd {}&&touch x&&".format(repo_name)

# Using github's api to create (repo_name) at (user_name)'s profile
create_repo_string += """curl -u '{}' https://api.github.com/user/repos -d '{{"name":"{}"}}' > x""".format(user_name, repo_name, repo_name)

# set_up_repo is one long string with a bunch of commands tied with && to sync local machine to github
set_up_repo = "cd {}&&rm x&&".format(repo_name)
set_up_repo += """echo "## {} ##" > README.md&&""".format(repo_name) # Create README
set_up_repo += "git init&&" # Initialize git
set_up_repo += "git add .&&" # Add all files in current directory
set_up_repo += """git commit -m "first commit"&&""" # Make an initial commit
set_up_repo += "git remote add origin git@github.com:{}/{}.git&&".format(user_name, repo_name) # Syncing local and remote
set_up_repo += "git push -u origin master" # Pushing everything into master

# Excecuting (create_repo_string) & (set_up_repo) commands below
os.system(create_repo_string)
os.system(set_up_repo)

print("\n\n:::::::Created: " + repo_name + " @ " + user_name + "\n\n")