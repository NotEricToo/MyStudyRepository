======================= Git Study

== config username and email :
# user.name
git config --global user.name "NotEricToo"
# user.email 
git config --global user.email "450098674@qq.com"

== init the folder as a repository: 
cd xxx folder .
git init 

== create a file in xxx folder 
# put the file to repository 
git add xxxfile 

# commit the file to git :
# -m �� comment 
git commit -m "��һ���ύ"


== git command:
# show git current status 
git status

# git diff : check the different between files in repository and local file. 
git diff 

# show the commit log you committed
git log 
# this command will show all log info : version code and the comment and author and commit time.

# we also can only show the comment of the commit:
git log --pretty=oneline
# this will show version code: absdajkljdlksajdlksajdkljfkljkslafjlksaj  and the commit comment.
# sajodjsaodjasoidjasoidjsiao "The first time commit"


# Version rollback:
git reset --hard HEAD^ # rollback to the previous version. ^ means 1 version. 
git reset --hard HEAD^^ # rollback to the previous 2 version. ^ means 1 version. 

git reset --hard version_code # rollback to the specified version . # ���˵�ָ���İ汾
# version_code no need type all code here, only 4-5 words is fine

# show all history command you used 
git reflog

# checkout the file: # ���� 
git checkout -- filename 

========================= use remote repository to manage you code:

# login to the Git 
ssh-keygen -t rsa -C "email@qq.com"
# this will gen your ssh key to /c/Users/xlg/.ssh/id_rsa
cd /c/Users/xlg/.ssh/
# In this folder, will have 2 files, one is private key, other is public key.
id_rsa id_rsa.pub 
cat id_rsa.pub 
---- begin ----
ssh-key=sdjsakldjsakldjlaskdjaslk
sajdkjsakldaslkdjaskl
asjdkslajdlaskjdlkasjdlk=xx 450098674@qq.com 
---- end  ---- 
# the middle code is the public key 
# add the public key to your Git repository :
# ���Ժ��Ժ��������
Login to Git:
https://github.com 

upper right:
click -> settings-> SSH and GPG keys -> New SSH key -> paste your key and input the title. -> Add SSH key 

# test if the setting is right:
ssh -T git@github.com 

# relate the remote repository
git remote add origin Remote_Repository_address 

# pull the code to local folder:
git pull origin master 
# the first time to pull files to local, may ocurs errors: refusing to merge unrelated histories, we need to add a argument:
git pull origin master --allow-unrelated-histories 

# clone the remote repository to local :
git clone git@github.com:usernamexxxxx
# remote address can get from git repository. 


== ignore files :
# we can no upload some files which is in the file : .gitignore
.gitignore 


============================== ��֧����branch manage. 
== create a branch :
git branch new_branch 

== show branches
git branch 

== �л���֧:
git checkout new_branch 

git checkout -b new_branch # �л��� new_branch ��֧�����û�и÷�֧���ʹ����÷�֧

== ��֧����ϲ���master��
git checkout master # �л���master ��֧

git merge new_branch # �� new_branch �ķ�֧���ݣ��ϲ��� master ����

# all above behaviour is doing in local branch :


== To create a remote branch and push the code to remote repository :
git push --set-upstream origin new_branch 

== only push the code to a branch ��
git checkout new_branch 
git push origin # push the code to new_branch 









































 




