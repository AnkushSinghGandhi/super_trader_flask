# User Microservice

Welcome to the User Microservice of our application! This microservice is responsible for handling user authentication, user registration, user management, and related functionalities within our application. By providing endpoints for user authentication, registration, buying and selling stocks, managing user profiles, and administrative tasks, this microservice ensures a seamless user experience and robust security measures.

## Features

### 1. Authentication and Registration

- **POST /login**: Authenticates a user.
- **POST /register**: Registers a new user.

### 2. Trading

- **POST /buy**: Allows users to buy stocks.
- **POST /sell**: Allows users to sell stocks.

### 3. User Management

- **GET /users/{user_id}/purchase_history**: Retrieves the purchase history of a user.
- **GET /users/{user_id}/sell_history**: Retrieves the sale history of a user.
- **POST /users/{user_id}/watchlist**: Adds watchlist items for a user.
- **GET /users/{user_id}/watchlist**: Retrieves the watchlist of a user.
- **POST /users/{user_id}/delete_watchlist_items**: Deletes watchlist items for a user.

### 4. Admin Tasks

- **POST /create_admin**: Creates an admin account.
- **POST /create_user**: Creates a user account.
- **POST /pause_user**: Pauses a user account.
- **POST /ban_user**: Bans a user account.
- **GET /get_user_history/{user_id}**: Retrieves the purchase history of a user.

## Setting Up Docker Container

1. **Clone the Repository**: Clone the repository to your local machine.

    ```bash
    git clone https://github.com/ankushsinghgandhi/super_trader_flask.git
    ```

2. **Navigate to the Microservices Directory**: Change into the directory containing the microservices.

    ```bash
    cd super_trader_flask/app
    ```

3. **Build Docker Images**: Each microservice has its own Dockerfile. Build Docker images for the user microservice using its Dockerfile.

    ```bash
    cd user_microservice
    docker build -t user_service .
    ```

4. **Run Docker Container for the User Microservice**: Once the Docker image is built, run a Docker container for the user microservice.

    ```bash
    docker run -d -p 5000:5000 user_service
    ```

5. **Verify Container Status**: You can verify that the Docker container is running by checking its status.

    ```bash
    docker ps
    ```

   This command will display a list of running Docker containers. You should see a container for the user microservice in the list.

6. **Access the User Microservice**: Once the container is up and running, you can access the user microservice through your web browser or using API clients. The microservice will be available at port 5000 (e.g., `http://localhost:5000`).

That's it! You've successfully set up a Docker container for the user microservice. You can now use Docker to deploy the microservice independently.

If you encounter any issues during the setup process, please refer to the Docker documentation or reach out to the support team for assistance.

## API Documentation

Swagger API documentation is available at `/api/swagger.json` endpoint. You can use Swagger UI or any API client to explore and interact with the API endpoints.
