from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/products/ebay")
def get_mock_products():
    return jsonify([
        {
            "title": "Wireless Earbuds Bluetooth 5.3",
            "image": "https://i.ebayimg.com/images/g/123456/s-l1600.jpg",
            "price": "29.99",
            "link": "https://www.ebay.com/itm/1234567890",
            "marketplace": "eBay"
        },
        {
            "title": "Smart Watch for Android iOS",
            "image": "https://i.ebayimg.com/images/g/abcdef/s-l1600.jpg",
            "price": "45.00",
            "link": "https://www.ebay.com/itm/9876543210",
            "marketplace": "eBay"
        },
        {
            "title": "4K Action Camera Waterproof",
            "image": "https://i.ebayimg.com/images/g/xyz123/s-l1600.jpg",
            "price": "55.99",
            "link": "https://www.ebay.com/itm/1928374650",
            "marketplace": "eBay"
        }
    ])

if __name__ == "__main__":
    app.run(debug=True)
