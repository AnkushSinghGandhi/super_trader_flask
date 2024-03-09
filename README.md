<a href="https://warriorwhocodes.com"><img src="repo_images/header.jpeg"></a>

<p align="center">
  <a href="https://ankushsinghgandhi.github.io">
    <img src="https://img.shields.io/badge/Website-3b5998?style=flat-square&logo=google-chrome&logoColor=white" />
  </a>
  <a href="http://twitter.com/ankushsgandhi">
    <img src="https://img.shields.io/badge/-Twitter-blue?style=flat-square&logo=twitter&logoColor=white" />
  </a>
   <a href="https://www.linkedin.com/in/ankush-singh-gandhi-2487771aa/">
    <img src="https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white" />
  </a>
  <a href="https://dev.to/@ankushsinghgandhi">
    <img src="https://img.shields.io/badge/-Dev.to-grey?style=flat-square&logo=dev.to&logoColor=white"/>
  </a>
  <a href="https://stackoverflow.com/users/13790266/ankush-singh">
    <img src="https://img.shields.io/badge/-Stackoverflow-orange?style=flat-square&logo=stackoverflow&logoColor=white"/>
  </a>
  <a href="https://leetcode.com/ankushsinghgandhi/">
    <img src="https://img.shields.io/badge/-Leetcode-yellow?style=flat-square&logo=Leetcode&logoColor=white"/>
  </a>
    <a href="https://www.hackerrank.com/ankushsgandhi">
    <img src="https://img.shields.io/badge/-HackerRank-green?style=flat-square&logo=Hackerrank&logoColor=white"/>
  </a>
    <a href="https://www.hackerearth.com/@bhanusinghank">
    <img src="https://img.shields.io/badge/-Hackerearth-purple?style=flat-square&logo=Hackerearth&logoColor=white"/>
  </a>
</p>

# Super Trader Flask
Super Trader is a Flask-based application designed for learning to trade stocks using live data. It allows users to view real-time & historic stock prices, make purchases, and track their favorite stocks & transaction history. Additionally, the admin panel provides features for managing user accounts, monitoring transactions, and more.

## Features

- **User Authentication:** Users can register, login, and manage their accounts securely.
- **Stock Trading:** Buy and sell stocks with real-time market data.
- **Portfolio Management:** Track the stocks you own, view purchase history and analyze performance.
- **Favorite Stocks:** Add and remove favorite stocks for quick access.
- **Admin Panel:** Manage user accounts, view transaction history, and monitor system activity.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/AnkushSinghGandhi/super_trader_flask.git
   ```

2. **Navigate to the project directory:**
   ```
   cd super_trader_flask
   ```

3. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

6. **Set up the database:**
   - This project uses MongoDB as the database. Make sure you have MongoDB installed and running locally or update the database configuration in `app/config.py`.

7. **Start the Flask server:**
   ```
   python app.py
   ```

8. **Access the application in your web browser** at `http://127.0.0.1:5000`.

## Usage

- Register a new account or login with existing credentials.
- Explore the stock market and add your favorite stocks to track.
- Buy and sell stocks based on real-time market data.
- Monitor your portfolio performance and transaction history.
- Admins can manage user accounts, view transaction logs, and perform system maintenance tasks.

## Flutter App
Super Trader Flask works in conjunction with the Super Trader Flutter mobile app, which provides the user interface for trading stocks and managing portfolios. The Flutter app communicates with this backend server to fetch stock data, perform transactions, and manage user accounts.

### Repository
The Flutter app repository can be found at: https://github.com/AnkushSinghGandhi/super_trader_flutter

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Flask:** [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **MongoDB:** [https://www.mongodb.com/](https://www.mongodb.com/)

## Support

For any questions or assistance, feel free to contact the project maintainer at [ankushsinghgandhi@gmail.com](mailto:your-ankushsinghgandhi@gmail.com).

Thank you for using Super Trader Flask! Happy trading!

