import json
from kafka import KafkaProducer
from datetime import datetime
import random
import time

# Set up Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka server address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializer to send data as JSON
)

# Function to generate random stock data
def generate_stock_data(symbol):
    current_time = datetime.now()
    stock_data = {
        'symbol': symbol,
        'open': round(random.uniform(100, 500), 2),
        'high': round(random.uniform(100, 500), 2),
        'low': round(random.uniform(100, 500), 2),
        'close': round(random.uniform(100, 500), 2),
        'volume': random.randint(1000, 10000),
        'timestamp': current_time.strftime('%Y-%m-%d %H:%M:%S')
    }
    return stock_data

# Example usage
if __name__ == "__main__":
    symbol = 'AAPL'
    while True:
        stock_data = generate_stock_data(symbol)
        producer.send('stock-market-data', stock_data)
        print(f"Sent data: {stock_data}")
        time.sleep(30)  # Sleep for 30 seconds
