---
layout: post
title: Deployment Blog
permalink: /deployment
menu: nav/home.html
search_exclude: true
show_reading_time: false
---





Neptune is your gateway to a world where students collaborate, connect, and aim for the stars. With features like an AI chatbot, class lists, chatrooms, a friends list, and customizable themes, Neptune fosters a thriving student community.

Follow these steps to deploy Neptune and ensure everything runs smoothly!

---



## System Architecture

Below is an overview of Neptune's architecture:

![System Architecture](/neptune_frontend/images/image.png)

Here is an image of the chatroom in depth, since it uses WebSocket.
![Chatroom](/neptune_frontend/images/chatroom.png)

---
## Roles:

`Scrum Master: Nolan`

`Assistant Scrum: Shawn`

`UX: Akshaj & Shawn`

`Deployment Admin: Kanhay`

`Assistant Deployment Admin: Yash`

`Backend Engineers: Arya & Yash`

## Accessing AWS EC2

**Log in to Cockpit: https://cockpit.stu.nighthawkcodingsociety.com/system/terminal**
    
`Username: ubuntu`

`Password:`

### Nginx

**1. Navigate to nginx**: `cd /etc/nginx/sites-available`

**2. Create an nginx config file**: `sudo nano neptune_backend`

**3. Activate configuration**: `cd /etc/nginx/sites-enabled`, then `sudo ln -s /etc/nginx/sites-available/neptune.stu /etc/nginx/sites-enabled`

**4. Validate**: `sudo nginx -t`

**5. Restart nginx**: `sudo systemctl restart nginx`
    - Nginx: **reverse proxy** that exposes our localhost server to the web through our website
    - The website is an **ip address** given a name through a **dns (domain name service)**

**6. Certbot**: `sudo certbot --nginx`
    - Gives the website a **https certificate**


### Changing Code will require Deployment Updates

**1. Run git pull before making changes**

**2. Open terminal in VSCode and run python main.py**

**3. Make changes that are needed**

**4. Commit the changes locally**

**5. Test `docker-compose up` or `sudo docker-compose up` in VSCode terminal**

**6. Sync change from UI/git push from terminal**


### Pulling Changes into AWS EC2 deployment

**1. Navigate to repo**: `cd ~/neptune_backend`

**2. docker-compose down**

**3. `git pull`**

**4. Rebuild docker container**: `docker-compose up -d --build`


### Troubleshooting checks on AWS EC2

**1. Try to curl**: `curl localhost:8204`

**2. Run `docker-compose ps`**

**3. Run `docker ps`**



### **Changing Code in VSCode**

**1.  Run `git pull` before making changes**.

**2.  Open terminal in VSCode and run `python main.py`**.

**3.  Make changes that are needed**.

**4.  Commit the changes locally**.

**5.  Test `docker-compose up` or `sudo docker-compose up` in VSCode terminal**.

**6.  Push changes to GitHub**.
    
### **Resetting Database**
**1. Open AWS terminal**
**2. Run `cd neptune_backend`**
**3. Run `source venv/bin/activate`**
----------

  
