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
