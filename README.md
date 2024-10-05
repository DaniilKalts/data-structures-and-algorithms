# 🧑‍🎓 Data Structures and Algorithms

This repository is made for educational purposes.

You can view and run each algorithm on your local machine using Docker (if Python and pytest-tui are not installed).

---

## 🐳 Getting Started with Docker

### ❗ Prerequisites:

1. **Docker Desktop** (macOS and Windows):  
   [Download Docker Desktop](https://www.docker.com/products/docker-desktop)

2. **Arch Linux users**: Install Docker:

   ```bash
   sudo pacman -S docker
   ```

3. Ensure Docker is installed and running properly.

---

### 🚀 Running the Project:

1. **Build the Docker container:**

   ```bash
   docker build -t container_name .
   ```

2. **Run the container:**
   ```bash
   docker run -it container_name
   ```

---

### 🛑 Stopping and Cleaning Up (Optional):

1. **Stop all running containers:**

   ```bash
   docker stop $(docker ps -q)
   ```

2. **Remove all containters:**

   ```bash
   docker rm $(docker ps -a -q)
   ```

3. **Remove all unused images, container (optional)**

   ```bash
   docker system prune -a
   ```
