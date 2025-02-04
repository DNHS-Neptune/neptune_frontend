---
layout: post
title: "Deploying Neptune: Reaching for the Stars"
permalink: /deployment/
menu: nav/home.html
search_exclude: true
show_reading_time: false
---

# Deploying Neptune: Reaching for the Stars

Neptune is your gateway to a world where students collaborate, connect, and aim for the stars. With features like an AI chatbot, class lists, chatrooms, a friends list, and customizable themes, Neptune fosters a thriving student community.

Follow these steps to deploy Neptune and ensure everything runs smoothly!

---

## Deployment Checklist

Use this checklist to track your progress while deploying Neptune:

- [ ] **Install Docker and Docker Compose**
- [ ] **Clone the Repository**
- [ ] **Set Up Environment Variables**
- [ ] **Build Docker Images**
- [ ] **Run the Containers**
- [ ] **Access the Application**
- [ ] **Verify Features**
- [ ] **Implement Security Best Practices**

---

## Step-by-Step Deployment Instructions

### 1. Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

If deploying to a remote server, ensure:
- SSH access is available.
- Required ports (e.g., `8212`) are open.

---

### 2. Clone the Repository

Clone the Neptune repository and navigate into the directory:

```bash
git clone https://github.com/your-org/neptune.git
cd neptune
```

---

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and configure the necessary environment variables. You can manually create this file or use an example (`.env.example`).

```env
PORT=8212
DATABASE_URL=<your-database-url>  # Connection string for the database
SECRET_KEY=<your-secret-key>      # Secret key for authentication and security
```

Replace placeholders with the appropriate values for your setup. **Do not share your `.env` file publicly** to protect sensitive information.

---

### 4. Build Docker Images

Run the following command to build the Docker images:

```bash
docker-compose build
```

This pulls necessary images and sets up all services defined in `docker-compose.yml`.

---

### 5. Run the Containers

Start all required services in detached mode:

```bash
docker-compose up -d
```

If issues arise, check logs with:

```bash
docker-compose logs
```

---

### 6. Access Neptune

Once the containers are running, open a web browser and navigate to:

```bash
http://<your-server-ip>:8212
```

Replace `<your-server-ip>` with your actual server's IP address or domain.

For a cloud provider, configure DNS settings for a subdomain (e.g., `neptune.yourdomain.com`).

To secure the connection, set up **SSL certificates** with [Certbot](https://certbot.eff.org/).

---

### 7. Verify Features

Ensure all features are working properly:

- **AI Chatbot** - Responds accurately to student queries.
- **Class List** - Allows students to select and view classes.
- **Chatroom** - Enables real-time communication.
- **Friends List** - Supports adding and managing friends.
- **Theme Customization** - Allows personalized themes.

---

## Notes for Developers

### Port Configuration

Neptune runs on **port 8212** (chosen by us). Ensure this port is open in your server's firewall.

### Error Handling

To diagnose errors, check container logs:

```bash
docker-compose logs
```

### Scaling

For higher traffic, consider scaling using **Docker Swarm** or **Kubernetes** for load balancing and high availability. 

To scale services manually:

```bash
docker-compose up --scale web=3 -d
```

---

## Troubleshooting

### Common Issues & Fixes

#### Containers Fail to Start
Run:
```bash
docker ps -a
```
Check logs for errors:
```bash
docker-compose logs
```

#### Database Connection Issues
- Verify `DATABASE_URL` is correctly set.
- Ensure the database container is running:
  ```bash
  docker-compose ps
  ```

#### Port Conflicts
- Run `netstat -tulnp | grep 8212` to check if another service is using the port.
- Modify the `PORT` variable in `.env` and update `docker-compose.yml` accordingly.

---

## System Architecture

Below is an overview of Neptune's architecture:

![System Architecture](/neptune_frontend/images/image.png)

Here is an image of the chatroom in depth, since it uses WebSocket.
![Chatroom](/neptune_frontend/images/chatroom.png)

---

Neptune is now deployed. Enjoy your journey among the stars.

# Security

## Authentication and Authorization:
- Implement user authentication and authorization mechanisms (e.g., JWT, OAuth) to control access to resources.
- Securely store user credentials and sensitive data.

## Data Encryption:
- Encrypt data in transit (e.g., using HTTPS) and at rest (e.g., encrypting database connections).

## Input Validation and Sanitization:
- Validate and sanitize user input to prevent vulnerabilities like SQL injection and cross-site scripting (XSS).

## Regular Security Audits and Updates:
- Regularly audit the application for security vulnerabilities.
- Keep the application and its dependencies up-to-date with security patches.

# Monitoring and Logging

## System Monitoring:
- Monitor key performance indicators (KPIs) such as CPU usage, memory consumption, and response times.
- Use monitoring tools (e.g., Prometheus, Grafana) to visualize and analyze system performance.

## Error Logging:
- Log errors and exceptions to help identify and troubleshoot issues.
- Use a centralized logging system (e.g., ELK stack) to collect and analyze logs.

## Alerting:
- Set up alerts for critical issues (e.g., system failures, security breaches).
- Use monitoring tools or alerting services (e.g., PagerDuty) to notify the appropriate personnel.

# Deployment Strategies

## Rolling Updates:
- Implement rolling updates to minimize downtime during deployments.
- Use strategies like blue/green deployments or canary releases to gradually roll out updates.

## Rollback Strategy:
- Have a plan for rolling back to a previous version in case of issues.
- Use version control and automated deployment tools to facilitate rollbacks.

## Scalability and High Availability:
- Load balance traffic across multiple instances to improve performance and reliability.
- Implement horizontal scaling to handle increased traffic.
- Plan for disaster recovery to ensure business continuity.

# Testing

## Unit Tests:
- Write unit tests to test individual components of the application.

## Integration Tests:
- Test the interaction between different components of the application.

## End-to-End Tests:
- Test the application from the user's perspective to ensure it meets user requirements.

# Maintenance

## Regular Maintenance:
- Perform routine maintenance tasks such as database backups and security audits.
- Regularly review and update the deployment and maintenance procedures.

## Performance Tuning:
- Monitor application performance and identify areas for improvement.
- Optimize database queries, cache frequently accessed data, and use efficient algorithms.


## Changing Code in VSCode

To keep deployment working, good practices in your coding process with verifications prior to pushing code to GitHub will save a lot of troubleshooting.

**1. Pull Changes:**

   - **Before making changes:** 
      - **`git pull`** in the VSCode terminal. 
      - This ensures you have the latest code from your team and prevents merge conflicts.

**2. Local Testing:**

   - **Open terminal in VSCode:** `cd` into your repository.
   - **Run:** `python3 main.py` 
   - This starts your Flask application locally.
   - **Open the local address in your browser:** View your changes live.
   - **Make changes:** Refer to your running site frequently to see changes in real-time.

**3. Commit Changes:**

   - **Commit your changes locally:** Use meaningful commit messages.
   - **Do not sync or push yet:** Committing allows you to pull team changes for further verification.

**4. Docker Desktop Testing:**

   - **Start Docker Desktop.**
   - **Run:** `docker-compose up` or `sudo docker-compose up` in the VSCode terminal.
   - **Access the application:** 
      - Open `http://localhost:8212` in your browser 
      - Replace `<port>` with your port number.
   - **Test thoroughly:** Review your changes and team members' changes.
   - **Debug errors:** If any errors occur, they will appear in the browser or VSCode terminal.
   - **Note:** Docker Desktop can consume resources. Close it after testing if you're unplugged.

**5. Push to GitHub:**

   - **If all tests pass:** 
      - **Sync changes** from the VSCode UI or **`git push`** from the terminal.
   - **If you encounter issues:** 
      - **`git status`** to review open files.
      - **Resolve conflicts:** Use `git restore` or `git commit`.
      - **`git pull`** again and repeat steps 2-4.

**6. Deploying to AWS EC2:**

   - **In your AWS EC2 terminal:**
      - **Navigate:** `cd ~/neptune_frontend`
      - **Stop the current deployment:** `docker-compose down`
      - **Verify downtime:** The server should be down (502 Bad Gateway).
      - **Pull changes:** `git pull`
      - **Rebuild:** `docker-compose up -d --build` 
      - **Test again:** The server should be updated and running.

**7. Optional Troubleshooting Checks (AWS EC2):**

   - **Check server status:** `curl localhost:8212`
   - **Verify container status:**
      - `docker-compose ps` 
      - `docker ps` 
