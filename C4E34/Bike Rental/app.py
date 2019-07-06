from flask import Flask, render_template, redirect, request

app = Flask (__name__)

all_bikes = {
    "model": "Lead",
    "fee": "120000",
    "link": "https://cdn.24h.com.vn/upload/3-2019/images/2019-07-05/1562295693-443-nong-honda-lead-ra-ban-moi-nhin-sang-chanh-gia-tu-383-trieu-dong-lead1-1562286399-width660height630.jpg",
    "year": "2015"
    }


@app.route("/bikes")
def home():
    return render_template("all_bike.html")

@app.route("/new_bike", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("add_bike.html")
    elif request.method =="POST":
        form = request.form
        model =form["Model"]
        fee=form["Daily_fee"]
        link = form ["Image"]
        year = form ["Year"]
        new_bikes={
            "model": Model,
            "fee": Daily_fee,
            "link": Image,
            "year": Year
        }
        all_bikes.append(new_bikes)
        return render_template("add_bike.html")