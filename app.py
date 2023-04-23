from flask import Flask, render_template,  jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Edinburgh,UK',
        'salary': '40000'
    },
    {
        'id':2,
        'title': 'Data Science',
        'location': 'London,UK',
        'salary': '50000'
    },
        {
        'id':3,
        'title': 'Mobile Developer',
        'location': 'Wales,UK',
        'salary': '20000'
    },
        {
        'id':4,
        'title': 'Wordpress Developer',
        'location': 'Delhi ,India',
        'salary': '20000'
    },
        {
        'id':5,
        'title': 'DevOps',
        'location': 'Goa ,India',
        'salary': '60000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS, company_name='Robin')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)