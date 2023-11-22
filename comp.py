from flask import Flask, render_template, request, redirect, url_for
from joblib import load
import sqlite3




# load the pipeline object
def my_ans(com):
    temp = list()
    temp.append(com)
    pipeline = load("new.joblib")
    ans = pipeline.predict(temp)
    return(ans)

app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', comp=user))

# get the data for the requested query
@app.route('/success/<comp>')
def success(comp):
    ans = my_ans(comp)
    data = (comp,ans[0])
    conn = sqlite3.connect('best_complaints.db')
    c= conn.cursor()
    query = """INSERT INTO COMP(user_comp,category) VALUES(?,?);"""
    c.execute(query,data)
    conn.commit()
    return str(ans)

app.run(debug=True)
