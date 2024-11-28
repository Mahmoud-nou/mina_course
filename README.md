## venv
py -m venv .venv <!-- to create venv -->
.venv\Scripts\activate

## Use Git
gh auth login
gh repo clone jasoom-store/Mahmoud_DB
git config --global user.email "YourEmail"
git config --global user.name "YourUser"

- pull => 
git pull

- push => 
git add *
git commit -m ""
git pull <!-- if you have friends on your project. -->
git push

- fix .gitignore if it not working => 
git rm -rf --cached .
git add .
