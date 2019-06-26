from flask import Flask, render_template, redirect

app = Flask (__name__)

profile = {
    "Name": "Lại Thu Thảo",
    "Work": "Marketer",
    "School": "Banking Academy",
    "Picture": "https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/64990779_10157316337696597_8205319596333334528_o.jpg?_nc_cat=103&_nc_oc=AQnAISeN5mCHK8Oani8jPCRsF-JxmfF90z8vRsXl6uck915MgardmvifF1-W33pGVU8&_nc_ht=scontent.fhan3-2.fna&oh=b0a457eabe4cd68250eb1b3232d0582e&oe=5D8ACC3F"
    }


@app.route("/about-me")
def home():
    return render_template("about_me.html", PROFILE=profile)

@app.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)