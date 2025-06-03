from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
import json


app = Flask(__name__)

def all_problems():
    problems = []
    with open('sorted_problems.json', 'r') as f:
        problems = json.load(f)
    return problems

def fetch_solved_problems(username):    
    url = f"https://codebreaker.xyz/profile/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    problem_names = [a.text.strip() for a in soup.select('table.table-bordered td a[href^="/problem/"]') if a.text.strip()]
    return problem_names

@app.route('/', methods = ['GET', 'POST'])
def index():
    username = ""
    problems = all_problems()
    solved_problems = []
    if request.method == 'POST':
        username = request.form.get('username', username)
        solved_problems = fetch_solved_problems(username)
    return render_template('index.html', problems = problems, solved_problems = solved_problems, username = username);

if __name__ == "__main__":
    app.run(debug=True)