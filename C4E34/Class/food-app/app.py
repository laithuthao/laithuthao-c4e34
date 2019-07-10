from flask import Flask, render_template, redirect, request
from food_database import Foods
from bson.objectid import ObjectId

app = Flask (__name__)

@app.route("/foods")
def home():
    all_foods = Foods.find()
    return render_template("all_food.html", ALL_FOODS=all_foods)

@app.route("/foods/<id>")
def food_detail(id):
    food = Foods.find_one({"_id": ObjectId(id)})
    return render_template("food_detail.html", FOOD=food)

@app.route("/foods/delete/<id>")
def delete_food(id):
    delete_food = Foods.find_one({"_id": ObjectId(id)})
    if delete_food is not None:
        Foods.delete_one(delete_food)
    else:
        return "Not found"
    return redirect("/foods")

@app.route("/foods/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("add_food.html")
    elif request.method =="POST":
        form = request.form
        new_foods={
            "title": form["title"],
            "description": form["desc"],
            "link": form ["img_link"],
            "type": form ["food_type"]
        }
        Foods.insert_one(new_foods)
        return redirect("/foods")


@app.route("/foods/edit/<id>", methods=["GET", "POST"])
def edit_food(id):
    edit_food = Foods.find_one({"_id": ObjectId(id)})
    if request.method == "GET":
        return render_template("edit_food.html", EDIT_FOOD=edit_food)
    elif request.method == "POST":
        form = request.form
        new_food_info = {
            "title": form["title"],
            "description": form["desc"],
            "link": form["img_link"],
            "type": form["food_type"],
        }
        new_value = {"$set": new_food_info}
        Foods.update_one(edit_food, new_value)
        return redirect('/foods')
        
if __name__ == "__main__":
    app.run(debug=True)
