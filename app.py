from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

app = Flask(__name__)

def all_problems():
    problems = []
    with open('problems.txt', 'r') as f:
        problems = [line.strip() for line in f.readlines() if line.strip()]
    return problems

def fetch_solved_problems(username):    
    url = f"https://codebreaker.xyz/profile/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    problem_names = [a.text.strip() for a in soup.select('table.table-bordered td a[href^="/problem/"]') if a.text.strip()]
    return problem_names