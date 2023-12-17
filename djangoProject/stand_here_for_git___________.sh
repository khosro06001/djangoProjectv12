###################################### FIRST DESKTOP #########################
####################################### FIRST DESKTOP #########################
D=/home/k/wp_cs416/final_project
F=djangoProject
FV=${F}v12
APP01=tma01
TEMPLATES=templates
cd $D/$FV/$F/$APP01 || exit 127
####################################### SECOND DESKTOP #########################
#############

#### first commit and push
cd /home/k/wp_cs416/final_project/djangoProjectv12/djangoProject
git init
git add .
git commit -m "django commit"
###git remote add origin <yourGithubRepositoryUrl>
git remote add origin https://github.com/khosro06001/djangoProjectv12.git
git remote -v
git push -u origin master
username: ...
password: YOUR TOKEN not your password!!!
ghp_kw...

### next commit and push
git add .
git commit -m "some new changes"
git push

