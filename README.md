## PriceOyee 🎉

**PriceOyee** is a price comparison and tracking tool, enabling users to make informed purchasing decisions by providing real-time product pricing and discount data from multiple online stores. With an intuitive interface and powerful tracking features, PriceOyee is designed to help users save money and shop smartly.

### Key Features

- **Real-Time Price Comparison**: Instantly compare product prices across various e-commerce platforms, ensuring users get the best available deals.
- **Price Tracking & Alerts**: Monitor historical price changes and receive alerts on price drops to make purchases at the right time.
- **Wishlist Management**: Keep track of your favorite items and get notifications on any price changes.
- **Simple, Clean Interface**: An intuitive, user-friendly interface built for ease of use.

### Tech Stack

- **Frontend**: HTML, CSS, and JavaScript for a lightweight and responsive user experience.
- **Backend**: Python with Django, providing robust server-side functionality.
- **Database**: SQLite for efficient data storage and retrieval of product and price data.
- **Deployment**: Docker containerization for easy deployment and scalability across different environments.

### Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/irtaza001/PriceOyee.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd PriceOyee
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Project**:
   ```bash
   python manage.py runserver
   ```
5. **Visit** `http://localhost:8000` to view the app locally.

### Docker Deployment

1. **Build the Docker Image**:
   ```bash
   docker build -t priceoyee .
   ```
2. **Run the Docker Container**:
   ```bash
   docker run -p 8000:8000 priceoyee
   ```

### Contributing

We welcome contributions! Please submit a pull request for any improvements or bug fixes.

**PriceOyee** – Your companion for smart shopping and best deals, powered by real-time data!
