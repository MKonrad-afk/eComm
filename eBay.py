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
def get_mock():
    return jsonify(
        [
            {
                "title": "Personalized Leather Keychain",
                "image": "https://i.etsystatic.com/29115127/r/il/20e281/3217173421/il_794xN.3217173421_c6ng.jpg",
                "price": "12.99",
                "link": "https://www.etsy.com/listing/1043130124/personalized-leather-keychain",
                "marketplace": "Etsy"
            },
            {
                "title": "Boho Rainbow Wall Art Print",
                "image": "https://i.etsystatic.com/28243037/r/il/66f5c4/3055123972/il_794xN.3055123972_hh7y.jpg",
                "price": "6.85",
                "link": "https://www.etsy.com/listing/962342892/boho-rainbow-wall-art-print",
                "marketplace": "Etsy"
            },
            {
                "title": "Echo Dot (5th Gen, 2022 release) with clock",
                "image": "https://m.media-amazon.com/images/I/71jiGaztijL._AC_SL1500_.jpg",
                "price": "59.99",
                "link": "https://www.amazon.com/dp/B09B9NQ4JZ",
                "marketplace": "Amazon"
            },
            {
                "title": "Apple AirPods Pro (2nd Generation)",
                "image": "https://m.media-amazon.com/images/I/61f1YfTkTDL._AC_SL1500_.jpg",
                "price": "249.00",
                "link": "https://www.amazon.com/dp/B0BDHWDR12",
                "marketplace": "Amazon"
            },
            {
                "title": "Apple iPhone 13 Pro Max 128GB Graphite (Unlocked)",
                "image": "https://i.ebayimg.com/images/g/nq4AAOSwFv5jvFwo/s-l1600.jpg",
                "price": "849.99",
                "link": "https://www.ebay.com/itm/175930388348",
                "marketplace": "eBay"
            },
            {
                "title": "PlayStation 5 Console Disc Edition - Brand New",
                "image": "https://i.ebayimg.com/images/g/7akAAOSwuq5km5Nn/s-l1600.jpg",
                "price": "599.00",
                "link": "https://www.ebay.com/itm/256346161882",
                "marketplace": "eBay"
            }
        ]
    )



@app.route("/")
def home():
    return render_template("main.html")

@app.route("/listings")
def listings():
    return render_template("listing.html")

@app.route("/api/products/all")
def get_all_products():
    # etsy = fetch_etsy_products()
    # amazon = fetch_amazon_products()
    # ebay = fetch_ebay_product()
    # return jsonify(etsy + amazon + ebay)
    return get_mock()

if __name__ == "__main__":
    app.run(debug=True)
