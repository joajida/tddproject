Provisioning a new site
==============================

##Required packages:

nginx
python3
git
pip
virtualenv

On Ubuntu: 
	sudo apt-get install nginx git python3 python3-pip
	sudo pip install virtualenv

##Virtual host config with nginx
	
see nginx.template.conf, replace sitename with relevant name

##Upstart job

see gunicorn-upstart.template.conf, replace sitename with relevant name

##Folder structure:
user account as /home/username

/home/username
|__sites
	|__SITENAME
		|__database
		|__source
		|__static
		|__virtualenv