import requests
from flask import Flask, render_template, request, url_for

class Universiter():
    def __init__(self, country):
        self.alpha_parameters = {"country": country}
        self.output_data = None
        self.get_data()

    def get_data(self):
        self.alpha_response = requests.get(url = "http://universities.hipolabs.com/search", params = self.alpha_parameters)
        self.alpha_response.raise_for_status()
        data = self.alpha_response.json()
        self.output_data = [{"Name:": x["name"], "Page": x["web_pages"][0]} for x in data]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def enter_country():
    if request.method == 'POST':
        country = request.values["country"].title()

        if country == '':
            return render_template("oops.html")
 #           return redirect(request.url)
        if country:
            univs = Universiter(country).output_data
            if len(univs) > 0:
                return render_template('output.html', universities = univs, country = country)
            else:
                return render_template("oops.html", no_univs = True)
#                return redirect(request.url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
