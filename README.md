Fibonappi - Generate n integers of the Fibonacci sequence.
=========================================================

Install
-------
Use pyenv, virtualenv, or virtualenv wrapper to create a virtualenv using python 2.7.x.

For example:
```
pyenv virtualenv 2.7.6 fibonappi
pyenv activate fibonappi
```

Run Tests
---------
```
python setup.py test
```


Test Application
----------------------
```
python fibonappi/fibonappi.py
```

Now navigate to http://localhost:5000 for some Swagger!

Run Application - Hard Way
----------------------------
```
apt-get update
apt-get install -y git nginx python-dev python-virtualenv supervisor
cd /opt
git clone https://github.com/jessegonzalez/fibonappi.git
virtualenv /opt/fibonappi/venv
/opt/fibonappi/venv/bin/pip install -r fibonappi/requirements.txt
source /opt/fibonappi/venv/bin/activate
cd /opt/fibonappi
/opt/fibonappi/venv/bin/python setup.py install
mkdir /var/run/fibonappi
chmod 0777 /var/run/fibonappi
chown www-data:www-data /var/run/fibonappi
mkdir /var/log/fibonappi
chown www-data:www-data /var/log/fibonappi
cp /opt/fibonappi/salt/fibonappi/files/etc/supervisor/conf.d/fibonappi.conf /etc/supervisor/conf.d/
supervisorctl reread && supervisorctl reload
rm /etc/nginx/sites-enabled/default
cp /opt/fibonappi/salt/fibonappi/files/etc/nginx/sites-available/fibonappi /etc/nginx/sites-available/fibonappi
ln -s /etc/nginx/sites-available/fibonappi /etc/nginx/sites-enabled/fibonappi
service nginx restart
```

Run Application - Easy Way
-----------------------
Use the SaltStack formula under salt/fibonappi to make it happen. Just drop it under your configured file_roots and update your salt/top.sls file.
