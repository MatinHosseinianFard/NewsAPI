# NewsAPI

## Overview

This project is a web application developed using Django and Django REST Framework. It includes a web scraper built with Scrapy to crawl and store news articles from Zoomit.

## Technologies Used

This project utilizes the following technologies:

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs in Django.
- **PostgreSQL**: A powerful, open-source relational database system.
- **Scrapy**: An open-source and collaborative web crawling framework for Python.
- **RabbitMQ**: A message broker that your applications can use to send and receive messages.
- **Celery**: An asynchronous task queue/job queue based on distributed message passing, used with RabbitMQ.
- **Nginx**: A high-performance web server and reverse proxy.
- **Docker**: A platform for developing, shipping, and running applications in isolated containers.

## Getting Started


### Prerequisites

Before you begin, ensure you have met the following requirements:
- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.
- Basic knowledge of Docker and Docker Compose.


### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/MatinHosseinianFard/NewsAPI.git
cd NewsAPI/
```

### 2. Build and Start the Containers
Build the Docker images and start the containers with Docker Compose:

```bash
docker-compose up -d --build
```

This command will:

Build the Docker images as specified in the `Dockerfile`.

Start the containers as defined in the `docker-compose.yml` file.


#### Create a superuser (optional, for accessing Django admin):
```bash
docker-compose exec -it app
```
Then:
```bash
python manage.py createsuperuser
```

### 3. Access the Application
The application will be available at http://localhost:8000.

The Django admin interface can be accessed at http://localhost:8000/admin.

### Urls

http://194.33.105.207/

http://194.33.105.207/admin

http://194.33.105.207/api/news

http://194.33.105.207/api/news?tags__name=

http://194.33.105.207:5556



### Celery Flower
Celery Flower, a real-time monitoring tool for Celery, is available at:
```bash
http://localhost:5556
```

### Project Structure
Below is a visual representation of the project structure:
[![Structure](https://github.com/MatinHosseinianFard/NewsAPI/blob/main/structure.png)](https://coggle.it/)

### 4. Stop the Containers
To stop and remove the containers, run:

```bash
docker-compose down
```

### Troubleshooting
**Port Conflicts**: Ensure that the ports specified in docker-compose.yml are not already in use by other applications.

**Logs**: To view logs for debugging, use:

```bash
docker-compose logs [service-name]
```

**Environment Issues**: Make sure all required environment variables are correctly set in the .env file.

### License
This project is licensed under the [MIT License](https://github.com/MatinHosseinianFard/NewsAPI/blob/main/LICENSE).

### Contact
For any questions or support, please reach out to matinhosseini795@gmail.com.

