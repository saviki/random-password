from flask import Flask,render_template,request
from script import generator


app = Flask(__name__)
app.secret_key = "UoJ&78u*0!ac5b1P^4dwERF%$Z"


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/genarated', methods=['POST'])
def genarated():
    password = ""

    # call to password generator()
    if request.method == 'POST':
        have_upper = True if request.form.get("upper") == "on" else False
        have_lower = True if request.form.get("lower") == "on" else False
        have_numbers = True if request.form.get("num") == "on" else False
        have_symbols = True if request.form.get("symbols") == "on" else False
        length = int(request.form.get("length") )

        password += generator(length, have_upper, have_lower, have_numbers, have_symbols)


    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug = False)