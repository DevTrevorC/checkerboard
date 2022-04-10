from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", rows = 8, columns = 8, color1 = 'red', color2 = 'black')

@app.route('/<int:rows>/')
def rows(rows):
    return render_template("index.html", rows = rows, columns = 8, color1 = 'red', color2 = 'black')

@app.route('/<int:rows>/<int:columns>/')
def rows_and_columns(rows, columns):
    return render_template("index.html", rows = rows, columns = columns, color1 = 'red', color2 = 'black')

@app.route('/<int:rows>/<int:columns>/<color1>/')
def rows_cols_color(rows, columns, color1):
    return render_template("index.html", rows = rows, columns = columns, color1 = color1, color2 = 'black')

@app.route('/<int:rows>/<int:columns>/<color1>/<color2>/')
def rows_cols_both_colors(rows, columns, color1, color2):
    return render_template("index.html", rows = rows, columns = columns, color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug = True)