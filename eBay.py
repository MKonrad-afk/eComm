from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


def fetch_etsy_products():
    url = "https://etsy-api2.p.rapidapi.com/shop/listings"
    querystring = {"shopId": "28297834"}
    headers = {
        "x-rapidapi-key": "d2bb2f2aa9msh77aa8db0d0b580fp18972djsn06599f709e01",
        "x-rapidapi-host": "etsy-api2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if not response.ok:
        return []

    items = response.json().get("data", [])
    return [{
        "title": item.get("title"),
        "image": item.get("image_url"),
        "price": item.get("price"),
        "link": item.get("url"),
        "marketplace": "Etsy"
    } for item in items[:6]]


def fetch_amazon_products():
    url = "https://real-time-amazon-data.p.rapidapi.com/influencer-profile"
    headers = {
        "x-rapidapi-key": "d2bb2f2aa9msh77aa8db0d0b580fp18972djsn06599f709e01",
        "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    }
    params = {"influencer_name": "tastemade", "country": "US"}

    response = requests.get(url, headers=headers, params=params)
    if not response.ok:
        return []

    items = response.json().get("data", {}).get("products", [])
    return [{
        "title": item.get("title"),
        "image": item.get("thumbnail"),
        "price": item.get("price"),
        "link": item.get("url"),
        "marketplace": "Amazon"
    } for item in items[:6]]


def fetch_ebay_product():
    url = "https://ebay32.p.rapidapi.com/product/195499451557"
    headers = {
        "x-rapidapi-key": "d2bb2f2aa9msh77aa8db0d0b580fp18972djsn06599f709e01",
        "x-rapidapi-host": "ebay32.p.rapidapi.com"
    }
    params = {"country": "germany", "country_code": "de"}

    response = requests.get(url, headers=headers, params=params)
    if not response.ok:
        return []

    item = response.json()
    return [{
        "title": item.get("title", "Unknown Title"),
        "image": item.get("image", ""),
        "price": item.get("price", {}).get("value", "N/A"),
        "link": item.get("url", "#"),
        "marketplace": "eBay"
    }]



@app.route("/")
def home():
    return render_template("main.html")

@app.route("/listings")
def listings():
    return render_template("listing.html")


@app.route("/api/products/all")
def get_all_products():
    etsy = fetch_etsy_products()
    amazon = fetch_amazon_products()
    ebay = fetch_ebay_product()
    return jsonify(etsy + amazon + ebay)

if __name__ == "__main__":
    app.run(debug=True)
