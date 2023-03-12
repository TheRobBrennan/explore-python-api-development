# Welcome
Let's refer to the `How to create an API in Python with FastAPI` section in the blog post [How to create an API in Python](https://anderfernandez.com/en/blog/how-to-create-api-python/) as a starting point.

## Local development

### Install dependencies and run our project

```sh
# Verify that you have Python installed on your machine
% python3 --version

# Create a new virtual environment for the project
% python3 -m venv .venv

# Select your new environment by using the Python: Select Interpreter command in VS Code
#   - Enter the path: ./.venv/bin/python

# Activate your virtual environment
# % source /Users/rob/repos/explore-python-api-development/fastapi/.venv/bin/activate
% source /path/to/explore-python-api-development/fastapi/.venv/bin/activate
(.venv) %

# Make sure you are in the FastAPI directory
(.venv) % cd fastapi

# Install Python packages in a virtual environment
(.venv) % pip install fastapi
(.venv) % pip install uvicorn
(.venv) % pip install pandas
(.venv) % pip install matplotlib
(.venv) % pip install requests
(.venv) % pip install gunicorn

# Let's start our FastAPI server - Available at http://127.0.0.1:8000/
(.venv) % uvicorn main:app --reload

# When you are ready to generate a requirements.txt file
(.venv) % pip freeze > requirements.txt

# What happens if you want to uninstall a package?

# Uninstall the package from your virtual environment
# (.venv) % pip uninstall simplejson

# Remove the dependency from requirements.txt if it exists
# (.venv) % pip uninstall -r requirements.txt

# Install the packages from requirements.txt
(.venv) % pip install -r requirements.txt
```

## Digital Ocean

Thank you to Rohith ND for writing the [Deploy FastAPI application on Digital Ocean with Nginx and Gunicorn](https://ndrohith09.hashnode.dev/deploy-fastapi-application-on-digital-ocean-with-nginx-and-gunicorn) blog post:

![](./images/thank_you_rohith_nd.png)

For the purposes of this example, my Droplet has been configured as outlined in the blog post and available at the IP address `161.35.228.138`

### Copy files to our Droplet

```sh
# Test the connection to our Droplet
% ssh root@161.35.228.138
Welcome to Ubuntu 22.10 (GNU/Linux 5.19.0-23-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat Mar 11 23:38:44 UTC 2023

  System load:  0.0               Users logged in:       0
  Usage of /:   6.9% of 24.06GB   IPv4 address for eth0: 161.35.228.138
  Memory usage: 19%               IPv4 address for eth0: 10.48.0.5
  Swap usage:   0%                IPv4 address for eth1: 10.124.0.2
  Processes:    92

101 updates can be applied immediately.
78 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


Last login: Sat Mar 11 23:32:22 2023 from 24.19.44.189
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~# exit

```

Awesome. Let's get back to our local machine and copy our files over to the `/root` directory on our Droplet:

```sh
# Make sure we're in the top level directory of our project
% pwd
/path/to/explore-python-api-development

# Use scp to copy my local files to the remote server
% scp -r fastapi root@161.35.228.138:/root

# Once copying is done you can navigate to `/root/fastapi` path and find your files.
% ssh root@161.35.228.138
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~# cd /root/fastapi/
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi# ls -al
total 36
drwxr-xr-x 3 root root 4096 Mar 11 23:49 .
drwx------ 6 root root 4096 Mar 11 23:49 ..
-rw-r--r-- 1 root root 8196 Mar 11 23:49 .DS_Store
-rw-r--r-- 1 root root 3389 Mar 11 23:49 README.md
drwxr-xr-x 2 root root 4096 Mar 11 23:49 images
-rw-r--r-- 1 root root 2277 Mar 11 23:49 main.py
-rw-r--r-- 1 root root  944 Mar 11 23:49 requirements.txt
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi# 
```

### Create a virtual environment on our Droplet

```sh
# Connect to our Droplet
% ssh root@161.35.228.138

# Navigate to the files we just copied over
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~# cd /root/fastapi/
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi#

# Create a virtual environment in the /root/fastapi folder
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi# apt install python3-pip
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi# pip install virtualenv
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi# virtualenv venv
root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi# source venv/bin/activate
(venv) root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi# 
```

### Nginx Configuration

I had to install Nginx on my Droplet by following the guide at [How To Install Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04):

```sh
# Install Nginx
% sudo apt update
% sudo apt install nginx

# OPTIONAL: Check and see if the firewall is enabled and running
% sudo ufw status
Status: inactive

# Enable the firewall
% sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup

# Adjust the firewall
% sudo ufw app list
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH

# It is recommended that you enable the most restrictive profile that will still allow the traffic you’ve configured. Right now, we will only need to allow traffic on port 80.
% sudo ufw allow 'Nginx HTTP'

# Let's make sure we're allowing HTTP traffic in our firewall on port 80
% sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
Nginx HTTP                 ALLOW       Anywhere                  
Nginx HTTP (v6)            ALLOW       Anywhere (v6)             

```

To serve the application over HTTP we have to make an Nginx config for our application. You can add any name to your app. Here I have specified as `fastapi-demo`:

```sh
(venv) root@ubuntu-s-1vcpu-1gb-intel-sfo3-01:~/fastapi# sudo nano /etc/nginx/sites-available/fastapi-demo
```

Add the following lines to the file - replacing `server_name` with your IP address (`161.35.228.138` in my case)

```
server{
       server_name 161.35.228.138; 
       location / {
           include proxy_params;
           proxy_pass http://127.0.0.1:8000;
       }
}
```

Let's make sure our Nginx service is up and running:

```sh
% systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; preset: enabled)
     Active: active (running) since Sun 2023-03-12 00:04:09 UTC; 8min ago
       Docs: man:nginx(8)
    Process: 9266 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 9267 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
   Main PID: 9351 (nginx)
      Tasks: 2 (limit: 1116)
     Memory: 5.2M
        CPU: 37ms
     CGroup: /system.slice/nginx.service
             ├─9351 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             └─9354 "nginx: worker process"
```

Let's open a web browser to our IP address - `161.35.228.138` in this example - at [http://161.35.228.138](http://161.35.228.138).
