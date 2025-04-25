from flask import Flask, render_template
import pybaseball as pyb

app = Flask(__name__)

df_batting_2025 = pyb.batting_stats(2025)

def is_vlad_batting_above_310():
    return "HELLO WORLD"

@app.route('/')
def index():
    result = is_vlad_batting_above_310()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)