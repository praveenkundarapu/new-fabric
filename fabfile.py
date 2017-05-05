from fabric.api import local

def touch():

  local("./manage.py")

def commit():

	local("git add . && git commit -m 'test1' ")

def push():
  
	local("git push origin master")

def pull():
  
	local("git pull")

def deploy():
  
	touch()
	commit()
  	push()
  	pull()
