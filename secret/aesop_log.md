aesop log:

8/25

run sudo yum update | kernel update to 4.9.43-17.38

install conda on linux (Version: 4.4.0 | Release Date: May 31, 2017):
	wget https://repo.continuum.io/archive/Anaconda3-4.4.0.1-Linux-ppc64le.sh
	installer doesn't seem to be compatible with amazon flavor of linux.  [?]
	terminated amazon linux, spun up ubuntu
	wget https://repo.continuum.io/archive/Anaconda3-4.4.0.1-Linux-ppc64le.sh
	still get the same error....  GDI.
	using this installer instead:
	wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

	- this didn't work 
	- https://www.continuum.io/downloads

	- this does
	- https://conda.io/miniconda.html

	omg where do i install shit 
	- https://askubuntu.com/questions/6897/where-to-install-programs
	- http://www.pathname.com/fhs/pub/fhs-2.3.html#LIBESSENTIALSHAREDLIBRARIESANDKERN

	ok so ... i installed miniconda to /usr/bin/miniconda3..
	i had to run the installer as root, so the PATH was exported to /root/.bashrc
	i had to copy the path export to the ec2-user's .bashrc which looks like this:
# added by Miniconda3 4.3.21 installer
export PATH="/usr/bin/miniconda3/bin:$PATH"

install jupyter with conda (as ec2 user)
	but first - sudo su; conda update python;
	conda install ipython
	conda install jupyter

https://chrisalbon.com/cloud-computing/run_project_jupyter_on_amazon_ec2.html
http://docs.aws.amazon.com/mxnet/latest/dg/setup-jupyter-coenfigure-server.html
install jupyter notebook

ipython
from IPython.lib import passwd
passwd() #will return encrypted password! save this!

Console
jupyter notebook --generate-config

Console
mkdir .jupyter/certs/; cd .jupyter/certs/
$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout "cert.key" -out "cert.pem" -batch


Console
vim .jupyter/jupyter_notebook_config.py #add the following to the top of the file:

c = get_config()  # Get the config object.
c.NotebookApp.certfile = u'/home/rlander/.jupyter/certs/cert.pem'
c.NotebookApp.keyfile = u'/home/rlander/.jupyter/certs/cert.key'
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = {YOUR ENCRYPTED PASSWORD}

* HAD TO MODIFY EC2 INBOUND RULE TO ACCEPT ALL TRAFFIC...  ACTUALLY: TRAFFIC FROM ONLY MY IP...  AND RESTRICT TO PROTOCOLS SSH, HTTP, HTTP, and CUSTOM (8999)

sudo su; conda install pandas
pip install bs4 (cuz we'll prob use it later...)


OKAY.  now the REAL journey begins.  

Looking at real estate market prices and trends..  it's already 2 AM.



8/26

I want to move my blog to my ec2.

oh god https://www.airpair.com/python/posts/django-flask-pyramid i don't care THIS much.

I'll keep my stuff in github for now i guess...




8/28

i want to generate a large file and post it up on s3
need to configure aws stuff...

in iam > groups, 
create a group, attach policies, then add users.

ok so generating a large file...

heyyy look asyncio https://hackernoon.com/asynchronous-python-45df84b82434
what ... does await do?  https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

---

pulling open data... reading excel files.. need to install xlrd



8/29

oooo sick elastic ip to ec2!

https://passingcuriosity.com/2015/installing-python-from-source/


8/31

AWS EC2 -- Adding new users

1. [GENERATE PRIVATE KEY] in aws console:
create new key, save pem file and be prepared to distribute as needed

2. [GENERATE PUB KEY WITH PRIVATE KEY] once downloaded, run:
ssh-keygen -y
<pem file>
copy public key - will be saved into the server

3. [CREATE REMOTE USER] in ec2 instance:
sudo adduser <username>
sudo mkdir /home/<username>/.ssh
sudo touch /home/<username>/.ssh/authorized_keys
paste public key into authorized_keys.

*permission requirements may apply
[SET PERMISSIONS]
sudo chmod 500 /home/<username>/.ssh
sudo chmod 400 /home/<username>/.ssh/authorized_keys

4. connect to server with:
ssh -v -o IdentitiesOnly=yes -i ~/.ssh/<pem file> <user name>@ec2-34-233-144-81.compute-1.amazonaws.com



9/2
creating staging server for reporting tools
- add pypacks alias
- add reporting tools alias


oh god... need to install git now..
sudo yum install git


did you know?
adding __init__.py to a directory will allow you to import the directory


9/3 
WHAAAAT THE FUCK IS THIIIIIIIIIIS
print(*['one','two']) >> 'one two'



SPHINX!	
10/2

pip install sphinx
make directory with sub-directories rst, html, scripts
run sphinx-quickstart
modify conf.py (template if anything)
put code to have docs generated for in scripts folder

run sphinx-apidoc -o rst/ {location of mapytools dir}
copy config file to rst directory
run sphinx-build -b html rst html
install apache2, create /var/www/html/sphinx/ directory
sudo cp -r html/* /var/www/html/sphinx/
sudo service httpd start (or stop or restart) +2/26/18


10/14

ADDING NEW USERS TO EC2 ITS SUPER EASY SO

aws ec2 create-key-pair --key-name ctirol-analytics.pem (or create in aws console)
chmod 700 ctirol-analytics.pem
ssh-keygen -y >> ~/Desktop/ctirol-analytics.pem
copy into .bashrc:

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# added by Miniconda3 4.3.21 installer
export PATH="/usr/bin/miniconda3/bin:$PATH"


configure jupyter notebook:





CREATED CRONUSER (USERS CANNOT LOG INTO CRONUSER, only su)
other users can modify master cron with
>> su cronuser
>> Enter Password:
>> crontab -e


OPEN USER FOLDER 
sudo chmod 705 -R /home/user

RESET .ssh, authorized_keys
sudo chmod 500 /home/user/.ssh
sudo chmod 400 /home/user/.ssh/authorized_keys


CREATE ANETELKOS USER
1. create key in aws
2. keygen with pem
3. create user in ec2
4. create password
5. create .ssh, .ssh/authorized_keys file
6. .ssh: 500, authorized_keys: 400
7. alias e1 >> anetelkos


8* chown folder


st
11/17

EFS

create in same vpc, sgroup
mount via vpc


# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
# User specific aliases and functions

# added by Miniconda3 4.3.21 installer
export PATH="/usr/bin/miniconda3/bin:$PATH"



# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin

export PATH




AUTOMATING ENVIRONMENT SET UP
 - edit /etc/bashrc to 
  - import conda path
  - git clone
 - edit /etc/bash.bash_logout to
  - delete git repo


did you know rundeck can't point to an EFS.

duh.



11/19

RUNDECK

1. ssh-keygen on remote
2. copy private to rundeck ui
3. copy public to remote auth keys

12/7
freakin.  vault.
ON UBUNTU:
Job for supervisord.service failed because the control process exited with error code. See "systemctl status supervisord.service" and "journalctl -xe" for details.


12/8

freakin.  rundeck
add user: sudo vim /etc/rundeck/realm.properties
add permissions: sudo vim /etc/rundeck/admin.aclpolicy (add to both top and bottom groups)


12/20 - N2

[PULLING DOWN REPOS ONTO A NEW MACHINE]
1. have key in settings
2. set remote directory permissions
3. make sure public key on remote machine is saved as id_rsa

[INSTALLING REPORTING_TOOLS]
1. pull repo down
2. git clone into /usr/lib/python2.7/dist-packages/
3. requirements:
qds-sdk
retry
db -- i think this is custom on N1


12/29 - S3 MULTIPART UPLOADS, STREAMING

create multipart upload
stream into part
upload part
complete multipart upload

#### 4/4/18 - TO DO...

- update mapytools.transport_utils.s/ftp
- migrate saatchi modular dashboard ETL to e1
- complete fraud stuff by 4/15
- identify perf migration items for E1
- send kristian to tech sol for flight editor
- DIY to Hadoop 2

4/17/18

E1 requirements:

boto
boto3
pandas
qds-sdk
psycopg2 (pip install psycopg2-binary)
pymysql

4/25/18
Notes:

2.	add gil to aeng distro
3.	ask eric for aws admin to add gil/ask eric to add gil to aws account
4.	wrap KYLE TURNER OMG
5.	wrap fraud
6.	N1 is your problem now
7.	Qubole/Databricks Clusters/AWS are your problems now

What were your problems before?

1. Standup
2. Custom reporting
3. N1/E1
4. Oracle/Data Modelling
5. EDA projects -> dashboards

HADOOP 2


for each:
- see if it works at all
- see how much faster than h1

shashwat -> adama

1. candidates:

- metadata...  [144716881]
broke - ran out of memory after an hour 26 minutes?

- custom attribution [144735055]
uh... 

FAILED: ParseException line 3:0 character ' ' not supported here

line 3:1 character ' ' not supported here
line 4:0 character ' ' not supported here
line 4:1 character ' ' not supported here
line 5:0 character ' ' not supported here
line 5:1 char...

- custom performance [144714024]

date is a func and will break stuff
timestamp is a func??

5/2/18

For next 1:1 with Gil:
- are all salesforce cases up to date?  lets spend 15 minutes closing anything that is closeable/expired

5/4/18

pkill -9 PID doesn't work (in some cases a command run with "screen" will prevent this)
use sudo kill -9 PID

5/17/18

Guess what.  Spark.
Scala is faster than Python when there are less number of cores. As the number of cores increases, the performance advantage of Scala starts to dwindle.


6/9/18

RUNDECK - adding a new node!

created an AMI from E1 (took like 30 minutes)
put the E1 clone (e1r) under jfk direct connect
turned on hostnames in jfk dc vpn
went into e1r
deleted human-users + associated home directories

went into rundeck server
edited /var/rundeck/projects/E1Reporting/etc/resources.json - switched hostname and osversion from e1 to e1r
sudo service rundeck restart


tried running date, ls /home/ but rundeck would time out
generated new ssh key on rundeck server, added pub to auth key file on e1r, added private to rundeck ui
sudo service rundeck restart again


restarted from beginning but in non-jfk vpc :(


update /var/rundeck/projects/E1Admin/etc/resources.json



6/30/18

[ GITHUB GIT UNDO COMMIT ]
committed something with passwords?  are you the most recent commit?

easy peasy.  we can completely undo all changes!  

$ git log | head -n 1 #to get the most recent commit id (e.g. 62c9d93a5b8960532385740663248238ff3edcce)
$ git reset 62c9d93a5b8960532385740663248238ff3edcce --hard
$ git push origin -f

that's it!

[ ELASTIC IPS ]
when re-associating an ip to a new server, the following response may be returned:

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:RGQlHOzQranLH0pBSg7Sb5KcaO7dHOPqNKOizx7A3ZM.
Please contact your system administrator.
Add correct host key in /Users/ctirol/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /Users/ctirol/.ssh/known_hosts:71
ECDSA host key for ec2-18-205-133-81.compute-1.amazonaws.com has changed and you have requested strict checking.
Host key verification failed.

to address this, /Users/ctirol/.ssh/known_hosts must be edited
look for the line entry containing the name of the dns, e.g. "ec2-18-205-133-81.compute-1.amazonaws.com"
comment out or delete the line, then retry logging into the server

* unclear how this may affect remote connections to this server, or remote servers that whitelist an IP that is re-associated to a new server...







7/16/18

[ n0 ]

- sudo yum install postgresql
- sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs

... followed this instead: https://github.com/snowplow/snowplow/wiki/Setting-up-PostgreSQL


- created analytics-adama
- "we've had to make our own read-only" - Bannon
- analytics may need to deploy its own resurrection ship


7/17/18
- jars in java - udf reg is different; rewrap
- leave the guts, update the wrapper

- lift and shift
- 2 day freeze
- lift and shift metastore OR databricks connects to metastore (mysql!)

- commands vs notebooks
- managing commands:
- 


use i3s
broadcasting
explicit shuffle partitions - try and adhere to at least 200MB partitions when possible - call to s3 more expensive than reading large files
 - run spark job on bucket to recondense files in s3
 - 



more advanced:
use multithreading
checkpointing

- skewed data - lopsided dataset
- spilling to disk
- overloaded executor
- look for 200 stage jobs


- rules of engagement - (how big are your executors?  data skew?  spilling to disk?  scaling!  
- subset of data with everything cached - confirm theory that evrything works the way you want it to

scaling: once you've confirmed it works, scale up data size used in job to larger sample, then scale with math...
- before production, review team looks at production job, then give knowledge sharing

tuning:  how to do skew joins efficiently

databricks: performance tuning training (how udfs affect your jobs, how udfs work)
- fastest way to build intuition: 1-3 days of training
- RSA hours: work together with people like Daniel to optimize 1-2 jobs to address tuning
- also online - 5 days, 4 hours each day (RSA - add-ons)
- 10 people for instruction/training course




increase compute hours - migration factory - 


7/20/18

[ e1 ]

MOVING TO JFK

1. create image of e1 (1000 GB) 
2. rename e1 to e1-old in aws console 
3. spin up new instance, call it e1 
4. detach e1-old ip address, attach to (new) e1
5. remove e1 line item from known hosts
6. connect to (new) e1
7. test adama connection on (new) e1



7/24/18

imaged e1r
launched cloned instance from ami in jfk vpc (security group analytics offices)
disassociated ip from e1r-old
associated ip to new e1r (private ip changed)
removed e1r from known hosts file
logged into e1r, git pull mm-analytics-e1 and reptools

sudo vim /var/rundeck/projects/E1Reporting/etc/resources.json
update entry for e1 (new osVersion)

sudo service rundeckd restart

ran into same issue as last month, running date does not work, rundeck server can not talk to e1r
adding rundeck private (because its in the same vpc) ip to e1r's inbound acl


8/7/18

RUNDECK API!


NODE!
sudo npm install -g n


8/10/18
cid dash broke
looked in darkplace (cid dash pulls from psql view)
most recent data in view is from june, no recent campaign data (att reports no q3 campaigns)
confirmed no data in md perf table
traced back data update proc to n1 (found/remembered/forgot that scheduling was moved to rundeck)
went to rundeck, saw that default update proc was timing out after 10 hours
ran update for just att, last 14 days - succeeded
confirmed data was in psql table m_d_performance
did not know how to tie data from m_d_perf in mysql to cid_results in darkplace (so found that actually 2 things were broken)
saw that darkplace view had coolumns like "unique devices", so deduced that view reads from some qubole data
checked qubole scheduler, searching for column names in cid_results
found qubole command 171867629

saw that it was breaking because of s3://mediamath/chopped_impressions - missing partitions
- java.io.FileNotFoundException: File s3n://mediamath/chopped_impressions/impression_date=2018-07-03/organization_id=100075 does not exist
eric confirmed root cause may be gdpr compliance change
looked for "chopper" in n1 crontab

config file for qubole job in n1
d1/analytics/reporting/platform_reports/modular_dashboard$ config_connected_id.json
18 10 * * 0 $REPDIR/platform_reports/modular_dashboard/handler.py config_connected_id.json >> $REPDIR/platform_reports/modular_dashboard/handler.log 2>&1

9/02/18

offboarding users:

sudo userdel ssit;
sudo chown -R ec2-user /home/ssit;
sudo chgrp -R ec2-user /home/ssit;
rm -rf /home/ssit/mm-analytics-e1;



i just did some shit.

password in plain text in really old file that i deleted recently.

https://blog.ostermiller.org/git-remove-from-history:

git filter-branch --tag-name-filter cat --index-filter 'git rm -r --cached --ignore-unmatch FILE_LIST' --prune-empty -f -- --all
git push origin --force --all
git push origin --force --tags


https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase



9/17/18
WHATS A SOCKET
size of request cap: originally defaulted to wsgi default (4kb)
update cap to 32kb
- uses sockets instead of ports
nginx connects to diy via etc/nginx/sites-aailable/rest_diy_api.conf: uwsgi_pass: /home/ubunti/aeng-rest-diy/socket.sock

nginx is just the proxy
nginx config: says to wait for request on port 8080, divert to socket
translator : uwsgi (must receieve a callable)
uwsgi.ini (config file)
socket file


queue: rabbitmq


9/29/18

RUNDECK - adding a new project: E1HiFrequency!

Create new project in UI
Copy some config stuff (most importantly the config file on the rundeck server)
In rundeck_analytics server, copy folder from a project to new project (need to create new folder first)


11/7/18

Add Explorer Node to [RUNDECK]



12/23/18

Attemping to upgrade Rundeck server...

$ sudo yum update --exclude=rundeck*

... it worked this time?  no errors..
-----
config files are stored here: /etc/rundeck/
logs are stored here: /var/log/rundeck/

/etc/rundeck/framework.properties contains:
framework.plugin.Notification.HipChatNotification.apiAuthToken=4b4153d843fa865d1ab3d60ab5ba4a

-----
JK it doesn't work.  Jobs won't run.

Tried running this:
http://rundeck-1355411209.us-east-1.elb.amazonaws.com/project/E1Reporting/jobs/mm-analytics-e1/analytics/ctirol/helloworld

Error:
Failed request: runJobInline. Result: Server Error
Caused by: com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: Unknown column 'workflowst1_.fail_on_disable' in 'field list'

------

in rundeck-config.properties, uncommented:
dataSource.url = jdbc:h2:file:/var/lib/rundeck/data/rundeckdb;MVCC=true
dataSource.dbCreate = update

sudo service rundeckd restart

to check if restart worked:
tail -n 500 /var/log/rundeck/service.log

errors:

2018-12-23 08:38:25.385  WARN --- [           main] o.h.e.j.e.i.JdbcEnvironmentInitiator     : HHH000341: Could not obtain connection metadata : Driver:com.mysql.jdbc.Driver@4b1abd11 returned null for URL:jdbc:h2:file:/var/lib/rundeck/data/rundeckdb;MVCC=true

2018-12-23 08:38:25.407 ERROR --- [           main] o.s.boot.SpringApplication               : Application startup failed

org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'methodValidationPostProcessor' defined in class path resource [org/springframework/boot/autoconfigure/validation/ValidationAutoConfiguration.class]: Unsatisfied dependency expressed through method 'methodValidationPostProcessor' parameter 0; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'hibernateDatastoreServiceRegistry': Cannot resolve reference to bean 'hibernateDatastore' while setting constructor argument; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'hibernateDatastore': Bean instantiation via constructor failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [org.grails.orm.hibernate.HibernateDatastore]: Constructor threw exception; nested exception is org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment]

Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'hibernateDatastoreServiceRegistry': Cannot resolve reference to bean 'hibernateDatastore' while setting constructor argument; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'hibernateDatastore': Bean instantiation via constructor failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [org.grails.orm.hibernate.HibernateDatastore]: Constructor threw exception; nested exception is org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment]

Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'hibernateDatastore': Bean instantiation via constructor failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [org.grails.orm.hibernate.HibernateDatastore]: Constructor threw exception; nested exception is org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment]

Caused by: org.springframework.beans.BeanInstantiationException: Failed to instantiate [org.grails.orm.hibernate.HibernateDatastore]: Constructor threw exception; nested exception is org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment]

Caused by: org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment]

Caused by: org.hibernate.HibernateException: Access to DialectResolutionInfo cannot be null when 'hibernate.dialect' not set


-----


in rundeck-config.properties, recommented:
#dataSource.url = jdbc:h2:file:/var/lib/rundeck/data/rundeckdb;MVCC=true




12/26/18

heap analytics

export csv from heap, then:

filename = 'PageviewsoverTime.csv'

df = pd.read_csv(filename)

master = pd.DataFrame()

output = 'pivoted-pageviews-over-time.csv'

for col in df:
    if col != 'series':
        xf = df[['series',col]]
        xf.columns = ['date','count']
        xf['page'] = col
        master = master.append(xf)

master.to_csv(output,index=False)

then:
load csv to table


1/2/19

ec2-user@ip-10-150-8-63:/d1/analytics/reporting$ sudo pip install mysqlclient
Collecting mysqlclient
  Using cached https://files.pythonhosted.org/packages/f7/a2/1230ebbb4b91f42ad6b646e59eb8855559817ad5505d81c1ca2b5a216040/mysqlclient-1.3.14.tar.gz
    Complete output from command python setup.py egg_info:
    sh: mysql_config: command not found
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-0GqEoQ/mysqlclient/setup.py", line 16, in <module>
        metadata, options = get_config()
      File "setup_posix.py", line 53, in get_config
        libs = mysql_config("libs_r")
      File "setup_posix.py", line 28, in mysql_config
        raise EnvironmentError("%s not found" % (mysql_config.path,))
    EnvironmentError: mysql_config not found

ec2-user@ip-10-150-8-63:/d1/analytics/reporting$ sudo yum install mysql-devel

  gcc -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -Dversion_info=(1,3,14,'final',0) -D__version__=1.3.14 -I/usr/include/mysql -I/usr/include/python2.7 -c _mysql.c -o build/temp.linux-x86_64-2.7/_mysql.o
  unable to execute 'gcc': No such file or directory
  error: command 'gcc' failed with exit status 1

  ----------------------------------------
  Failed building wheel for mysqlclient
  Running setup.py clean for mysqlclient
Failed to build mysqlclient
Installing collected packages: mysqlclient
  Running setup.py install for mysqlclient ... error
    Complete output from command /bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-Pr9Ffj/mysqlclient/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-v8bR3s/install-record.txt --single-version-externally-managed --compile:
    /usr/lib64/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'long_description_content_type'
      warnings.warn(msg)
    running install
    running build
    running build_py
    creating build
    creating build/lib.linux-x86_64-2.7
    copying _mysql_exceptions.py -> build/lib.linux-x86_64-2.7
    creating build/lib.linux-x86_64-2.7/MySQLdb
    copying MySQLdb/__init__.py -> build/lib.linux-x86_64-2.7/MySQLdb
    copying MySQLdb/compat.py -> build/lib.linux-x86_64-2.7/MySQLdb
    copying MySQLdb/connections.py -> build/lib.linux-x86_64-2.7/MySQLdb
    copying MySQLdb/converters.py -> build/lib.linux-x86_64-2.7/MySQLdb
    copying MySQLdb/cursors.py -> build/lib.linux-x86_64-2.7/MySQLdb
    copying MySQLdb/release.py -> build/lib.linux-x86_64-2.7/MySQLdb
    copying MySQLdb/times.py -> build/lib.linux-x86_64-2.7/MySQLdb
    creating build/lib.linux-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/__init__.py -> build/lib.linux-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/CLIENT.py -> build/lib.linux-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/CR.py -> build/lib.linux-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/ER.py -> build/lib.linux-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/FIELD_TYPE.py -> build/lib.linux-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/FLAG.py -> build/lib.linux-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/REFRESH.py -> build/lib.linux-x86_64-2.7/MySQLdb/constants
    running build_ext
    building '_mysql' extension
    creating build/temp.linux-x86_64-2.7
    gcc -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -Dversion_info=(1,3,14,'final',0) -D__version__=1.3.14 -I/usr/include/mysql -I/usr/include/python2.7 -c _mysql.c -o build/temp.linux-x86_64-2.7/_mysql.o
    unable to execute 'gcc': No such file or directory
    error: command 'gcc' failed with exit status 1

    ----------------------------------------
Command "/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-Pr9Ffj/mysqlclient/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-v8bR3s/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-install-Pr9Ffj/mysqlclient/

ec2-user@ip-10-150-8-63:/d1/analytics/reporting$ sudo yum install gcc

ec2-user@ip-10-150-8-63:/d1/analytics/reporting$ sudo pip install mysqlclient
Collecting mysqlclient
  Using cached https://files.pythonhosted.org/packages/f7/a2/1230ebbb4b91f42ad6b646e59eb8855559817ad5505d81c1ca2b5a216040/mysqlclient-1.3.14.tar.gz
Building wheels for collected packages: mysqlclient
  Running setup.py bdist_wheel for mysqlclient ... done
  Stored in directory: /root/.cache/pip/wheels/6d/7d/cb/181963137c414938d4faac9a57c966fb3a6ef675c25641c41a
Successfully built mysqlclient
Installing collected packages: mysqlclient
Successfully installed mysqlclient-1.3.14


2019-01-04

Serving Jupyter Lab Slides:
jupyter nbconvert slideshow-template.ipynb --to slides --post serve --ServePostProcessor.ip="0.0.0.0" --ServePostProcessor.port=8998



2019-01-14

- upgraded mysql instance from t4.micro to r4.xl
- copied workflow_step table, renamed workflow_step to workflow_step_bkp


2019-01-15

- truncated geo data
- updated permissions table in aurora to match mysql
- 




2019-01-17

performance io

old placements that ran on a campaign from 5 months ago are rerunning on new campaign
placements exist in dcm report, but aren't getting passed through to campaign_report_3pas_summary
end dates needed to be set for placements for old campaign (in campaign_meta_3pas)
same placements needed to then be duplicated, with start dates set (in campaign_meta_3pas)
t1as + 3pas data join needed a backfill (re-run mm_reporting.campaign_insert_3p_summary('2019-01-01','2019-01-17'))
reporting database then needed a backfill (re-run mm_external_02.insert_creative_strategy_day_3p(13961,date) (for dates between '2019-01-07','2019-01-17'))

2019-01-24

more performance io

what is the current config for starwood?  why does the report not show dcm numbers?

check github:

- when was the existing client report set up?
	- gturetsky committed on Jul 18, 2018 (it only pulls t1 performance metrics)

check mysql:

- what are current flights?
	- only 1 flight, campaign
	- 3pas (not t1as), dcm

- what are mapped placements?
	- none

- what are mapped 3pas reports?
	- most recent is Starwood_2018.csv

check webmail

- what is the most recent starwood report?
	- last report received 10/18


2019-02-04

[databricks]
can't access a mounted bucket in databricks?
remount, change location from dbfs to s3a...


2019-02-07

[selenium]

1. https://sites.google.com/a/chromium.org/chromedriver/downloads

