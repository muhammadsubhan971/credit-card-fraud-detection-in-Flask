# Credit Card Fraud Detection Web Application

This project is a web application for credit card fraud detection using machine learning techniques. It allows users to input transaction data or user IDs to check for potential fraudulent activities.

## Features

- User ID lookup: Retrieve transaction details for a specific user.
- Transaction validation: Input transaction data to check if it's potentially fraudulent.
- Machine Learning Model: Utilizes a K-Nearest Neighbors classifier for fraud detection.
- Web Interface: Simple and intuitive web interface for easy interaction.

## Prerequisites

- Python 3.7+
- MySQL Database

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Create a database named `credit_d`
   - Update the `DATABASE_URL` in `credit.py` with your MySQL credentials

4. Run the application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Enter a user ID (1-965) to retrieve transaction details.
2. Select option 'A' to input transaction data for fraud detection.
3. Enter comma-separated transaction data when prompted.

## File Structure

- `app.py`: Main Flask application file
- `credit.py`: Contains credit card fraud detection logic and database interactions
- `templates/index.html`: HTML template for the web interface
- `model.joblib`: Saved machine learning model (generated when running the application)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
