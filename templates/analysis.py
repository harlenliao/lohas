from flask import Flask, render_template, request
from analysis import plot_lh5

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    stock_code = request.form['stock_code']
    plot_lh5(stock_code)
    return render_template('result.html', stock_code=stock_code)

if __name__ == '__main__':
    app.run(debug=True)
