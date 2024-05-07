# API Gateway

Welcome to the API Gateway of our application! The API Gateway serves as the entry point for all incoming requests from clients and efficiently routes them to the appropriate microservices within our system. By centralizing request handling, authentication, and load balancing, the API Gateway ensures seamless communication between clients and microservices while maintaining security and scalability.

## Features

### 1. Centralized Endpoint

- **Single Entry Point**: Clients interact with the API Gateway to access various functionalities provided by the microservices.

### 2. Request Routing

- **Dynamic Routing**: Incoming requests are dynamically routed to the corresponding microservices based on predefined rules or configurations.

### 3. Load Balancing

- **Traffic Distribution**: The API Gateway distributes incoming traffic evenly across multiple instances of microservices to optimize performance and scalability.

### 4. Authentication and Authorization

- **Authentication**: Handles user authentication and verifies access tokens or API keys before forwarding requests to microservices.
- **Authorization**: Enforces access control policies to ensure that only authorized users can access protected resources.

### 5. Request Filtering and Transformation

- **Request Filtering**: Filters and sanitizes incoming requests to prevent malicious attacks or unauthorized access.
- **Request Transformation**: Transforms request payloads or headers to match the format expected by downstream microservices.

### 6. Rate Limiting

- **Throttling**: Enforces rate limits on incoming requests to prevent abuse or overload of microservices.

### 7. Logging and Monitoring

- **Request Logging**: Logs incoming requests and responses for auditing and troubleshooting purposes.
- **Metrics Collection**: Collects metrics and performance data to monitor the health and performance of microservices.

## Setting Up Docker Container

1. **Clone the Repository**: Clone the repository to your local machine.

    ```bash
    git clone https://github.com/ankushsinghgandhi/super_trader_flask.git
    ```

2. **Navigate to the API Gateway Directory**: Change into the directory containing the API Gateway microservice.

    ```bash
    cd super_trader_flask/app/api_gateway
    ```

3. **Build Docker Image**: Build a Docker image for the API Gateway microservice using its Dockerfile.

    ```bash
    docker build -t api_gateway .
    ```

4. **Run Docker Container for the API Gateway**: Once the Docker image is built, run a Docker container for the API Gateway microservice.

    ```bash
    docker run -d -p 8080:8080 api_gateway
    ```

5. **Verify Container Status**: You can verify that the Docker container is running by checking its status.

    ```bash
    docker ps
    ```

   This command will display a list of running Docker containers. You should see a container for the API Gateway microservice in the list.

6. **Access the API Gateway**: Once the container is up and running, you can access the API Gateway through your web browser or using API clients. The API Gateway will be available at port 8080 (e.g., `http://localhost:8080`).

That's it! You've successfully set up a Docker container for the API Gateway microservice. You can now use Docker to deploy the microservice independently.

If you encounter any issues during the setup process, please refer to the Docker documentation or reach out to the support team for assistance.
