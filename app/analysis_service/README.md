# Analysis Microservice

Welcome to the Analysis Microservice of our application! This microservice plays a pivotal role in extracting insights, generating reports, and providing valuable analysis based on the extensive data collected from the trading platform. By harnessing various analytical techniques and algorithms, this microservice empowers users with actionable information to make informed decisions in the dynamic world of trading.

## Features

### 1. Future Dashboard
Gain valuable insights into the futures market with comprehensive dashboards showcasing top gainers, top losers, open interest changes, turnover, and more. Our intuitive interface provides traders with a holistic view of the futures landscape, enabling them to identify emerging trends and opportunities.

### 2. Option Chain Analysis
Dive deep into the world of options trading with our live option chain analysis. Explore Greeks, implied volatility, and other critical metrics to make informed decisions when trading options. Our robust analysis tools empower traders to optimize their options strategies and maximize returns.

### 3. Heat Map Visualization
Visualize trading activities across different stock indices with our interactive heat map visualization. Quickly identify areas of high activity and market sentiment shifts to stay ahead of the curve. Our heat maps offer a bird's-eye view of the market, allowing traders to spot trends and anomalies with ease.

### 4. PCR (Put Call Ratio) Analysis
Harness the power of the put-call ratio, a key indicator of market sentiment, to gauge investor sentiment and market direction. Our PCR analysis provides traders with valuable insights into market sentiment, helping them make more informed trading decisions.

### 5. Implied Volatility Chart
Track changes in implied volatility for different instruments with our comprehensive charts. Implied volatility is a crucial factor in options pricing and risk management. Our charts help traders monitor volatility trends and adjust their strategies accordingly.

### 6. Routes for Fetching Stock Data
Access essential stock data with ease using our dedicated endpoints. Retrieve the last trade price, all instrument identifiers, and detailed quote information for stocks, enabling seamless integration with external systems and applications.

### 7. Option Dashboard
Retrieve data for the Option Dashboard effortlessly through our intuitive endpoints. Get access to critical data points and analytics tailored for options traders, empowering them to make data-driven decisions in real-time.

## Setting Up Docker Container

1. **Clone the Repository**: Clone the repository to your local machine.

    ```bash
    git clone https://github.com/ankushsinghgandhi/super_trader_flask.git
    ```

2. **Navigate to the Microservices Directory**: Change into the directory containing the microservices.

    ```bash
    cd super_trader_flask/app
    ```

3. **Build Docker Images**: Each microservice have its own Dockerfile. Build Docker images for microservice using their respective Dockerfile.

    ```bash
    cd analysis
    docker build -t analysis_service .
    ```

4. **Run Docker Containers for Each Microservice**: Once the Docker images are built, run Docker containers for each microservice.

    ```bash
    docker run -d -p 5004:5004 analysis_service
    ```

5. **Verify Container Status**: You can verify that the Docker containers are running by checking their status.

    ```bash
    docker ps
    ```

   This command will display a list of running Docker containers. You should see containers for each microservice in the list.

6. **Access Microservices**: Once the containers are up and running, you can access analysis microservice through your web browser or using API clients. Each microservice will be available at its respective port (e.g., `http://localhost:5004` for the Analysis Microservice).

That's it! You've successfully set up Docker container for analysis microservice. You can now use Docker to deploy each microservice independently.

If you encounter any issues during the setup process, please refer to the Docker documentation or reach out to the support team for assistance.

## API Endpoints

Explore our comprehensive API endpoints to access a wide range of analytical features and data sources:

- `/future_dashboard`: Access futures trading dashboard.
- `/live_option_chain`: Retrieve live option chain data.
- `/heat_map`: Generate heat map visualization.
- `/pcr`: Calculate and retrieve Put Call Ratio analysis.
- `/iv_chart`: Fetch implied volatility charts.
- `/get_ltp`: Get the last trade price of a stock by instrument identifier.
- `/get_all_instrument_identifiers`: Get all instrument identifiers of available stocks.
- `/get_quote_details`: Get the details of a stock by instrument identifier.
- `/option_dashboard`: Retrieve data for the Option Dashboard.
