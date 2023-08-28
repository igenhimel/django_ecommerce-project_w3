# PrimePicks E-commerce Website

PrimePicks is an e-commerce platform built using Django, allowing users to browse, search, and purchase products. This repository provides the necessary code and configuration to set up the project.

## Table of Contents
1. [Django Run Process](#django-run-process)
2. [Docker Setup](#docker-setup)
3. [Project Features and Details](#Using-PrimePicks-E-commerce-Website)
4. [Using Django Admin](#using-django-admin)
5. [Creating Superuser and Running Migrations](#creating-superuser-and-running-migrations)

## Django Run Process

To run the PrimePicks project locally:

1. Clone this repository to your local machine.
```bash
git clone https://github.com/igenhimel/django_ecommerce-project_w3.git
```
2. Navigate to the project directory using the command line.
```bash
cd django_ecommerce-project_w3
```
3. Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

# Setting Up PostgreSQL Database with Docker

This section will guide you through setting up a PostgreSQL database using Docker for the PrimePicks E-commerce project.

## Prerequisites

Before you proceed, make sure you have Docker and Docker Compose installed on your system. If not, you can download and install them from the official Docker website.

## Creating a PostgreSQL Database

To set up the PostgreSQL database for PrimePicks using Docker, follow these steps:

1. **Create a `docker` folder:** In your PrimePicks project directory, create a folder named `docker`.

2. **Inside the `docker` folder, create a `docker-compose.yaml` file:** Copy the following content into the `docker-compose.yaml` file:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: adminpassword
    ports:
      - "8080:80"
    depends_on:
      - postgres
    volumes:
      - pgadmin_data:/var/lib/pgadmin

volumes:
  postgres_data:
  pgadmin_data:
```

3. **Navigate to the `docker` folder:** Open a terminal and navigate to the `docker` folder within your PrimePicks project directory.

4. **Start the Docker containers:** Run the following command to start the PostgreSQL and pgAdmin containers:

```bash
docker-compose up -d
```

5. Once the containers are up and running, you can navigate back to the parent directory using the cd .. command:

```bash
cd ..
```
6. **Accessing PostgreSQL and pgAdmin:**

   - PostgreSQL: The PostgreSQL container will run on port `5432`. You can access it using the connection details specified in the `docker-compose.yaml` file.

   - pgAdmin: The pgAdmin web interface will be available at `http://localhost:8080`. Use the email and password specified in the `docker-compose.yaml` file to log in.

7. **Creating a Database:**

   - Open pgAdmin in your web browser.
   - Log in using the provided credentials.
   - In pgAdmin, create a new server connection using the PostgreSQL container's information (host: `postgres`, port: `5432`, username: `your_db_user`, password: `your_db_password`).
   - Once connected, you can create a new database

8. **Configuring the `.env` file:** Update the `.env` file in your PrimePicks project root directory with the database connection details:

```dotenv
DATABASE_NAME=your_database_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=your_host
DATABASE_PORT=your_db_port
```


# Creating Superuser and Running Migrations

To access the Django admin interface and manage the PrimePicks platform:

1. Apply migrations if not done previously:

```bash
python manage.py makemigrations
python manage.py migrate
```


2. Create a superuser account:

```bash
python manage.py createsuperuser
```

3. Enter your desired username, email, and password.


# Using Django Admin

The Django admin interface provides a way to manage PrimePicks' data:

1. Start the development server:

```bash
python manage.py runserver
```

2. Access the Django admin panel at `http://127.0.0.1:8000/admin/`.

3. Log in with the superuser credentials created earlier.

4. You can manage products, reviews, and other data using the admin interface.


# Using PrimePicks E-commerce Website

PrimePicks is an intuitive e-commerce platform designed to provide a seamless shopping experience. Here's how you can use and access the website:

## Accessing the Website

1. Ensure that you have followed the instructions in the [Django Run Process](#django-run-process) section of the README to set up and run the PrimePicks project locally.

2. Open your web browser and navigate to `http://localhost:8000`.

## Browsing and Searching Products

1. **Home Page:** When you access the website, you will land on the home page showcasing a variety of products.

2. **Product Categories:** Use the navigation menu to explore products categorized under "Electronics," "Fashion," "Groceries," and "Home & Lifestyle."

3. **Search Bar:** To find specific products, use the search bar located at the top. Enter at least three characters and click the search button.

## Viewing Product Details

1. **Product List:** Click on any product's name or image to view its detailed information.

2. **Product Details:** On the product details page, you will find information such as product name, type, details, price, and any available discounts.


## Submitting Reviews

1. **Product Details Page:** Scroll down on the product details page to find the review section.

2. **Submit Review:** If you want to leave a review for the product, type your review in the provided text box and click the "Submit Review" button.

3. **Review Display:** Reviews submitted by other users will be displayed along with their creation date.

