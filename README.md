# Data Visualization Dashboard

## Project Overview
This project is an interactive data visualization dashboard built using React (TypeScript) and D3.js. It allows users to visualize metrics such as intensity, likelihood, and relevance across various datasets. The dashboard is equipped with several filters (end year, topics, sector, region, country) to allow dynamic exploration of data.

A Django REST Framework API has been developed to provide data through GET requests, and the data is stored in an SQLite database for efficient querying and retrieval.

## Features
- **Interactive Visualizations**: Various visualizations powered by D3.js allow users to analyze the data effectively, with a common layout style of 100% width and 80% height for charts.
- **Multiple Filters**: Filters include end year, topics, sector, region, PEST, SWOT, and country, giving users the ability to customize the displayed data.
- **Dynamic Data Rendering**: As users interact with the dashboard, the visualizations are dynamically updated based on selected filters.

## Tech Stack

### Frontend:
- React (with TypeScript)
- D3.js for data visualizations
- Bootstrap for styling

### Backend:
- Django (Django REST Framework)
- SQLite database for data storage

### Other:
- TypeScript for type safety in React

## Prerequisites

Before you begin, ensure that you have the following installed on your local machine:

- [Docker](https://www.docker.com/products/docker-desktop) (including Docker Compose)
- Git (for cloning the repository)

## Installation Steps

### 1. Clone the Repository
First, clone the repository to your local machine:

    ```bash
    git clone https://github.com/Anusha-guptha/dashboard-visualization.git
    cd dashboard-visualization
    ```

### 2. Navigate into the project directory
    ```bash
    cd your-repository
    ```

### 3. Ensure Docker and Docker Compose are installed
    - [Docker installation guide](https://docs.docker.com/get-docker/)
    - [Docker Compose installation guide](https://docs.docker.com/compose/install/)

### 4. Build the Docker images
    ```bash
    docker-compose build
    ```

    This will download the required images and set up Python, Node.js, and other dependencies.

### 5. Start the application

    Once the images are built, you can start the application with the following command:

    ```bash
    docker-compose up
    ```

   This will start the services defined in the `docker-compose.yml` file, including:

    - **Frontend (React)**: Accessible at `http://localhost:3000`
    - **Backend (Django)**: Accessible at `http://localhost:8000`
    - **Database**: Django's built-in SQLite database (configured within the Django project)

### 6. Accessing the application:

    - **Frontend (React)**: [http://localhost:3000](http://localhost:3000)
    - **Backend (Django)**: [http://localhost:8000](http://localhost:8000)

### 5. Stop the Docker containers:

    To stop the running containers, you can run:

    ```bash
    docker-compose down
    ```

## Configuration

The project includes the following configurations:

- **Frontend**: React application with Node.js running inside the container.
- **Backend**: Django application with Python running inside the container.
- **Database**: The built-in SQLite database that comes with Django.

You can modify the environment variables and configurations in the respective `.env` files for the frontend and backend if needed.

## Troubleshooting

- **Docker version**: Ensure you're using a compatible version of Docker.
  
- **Ports already in use**: If ports 3000 (React) or 8000 (Django) are already in use on your system, you can modify the `docker-compose.yml` file to use different ports.

- **Build issues**: If there are issues with building the containers, try running the following to ensure everything is clean:

    ```bash
    docker-compose down --volumes --remove-orphans
    docker-compose build
    docker-compose up
    ```
## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. Please ensure your changes do not break the existing functionality and are well-documented.



