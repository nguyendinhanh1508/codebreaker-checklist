from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import json

def fetch_all_problems():
    url = "https://codebreaker.xyz/problems"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    problem_names = []
    for link in soup.select('table#myTable a[href^="/problem/"]'):
        problem_name = link.text.strip()
        if problem_name:
            problem_names.append(problem_name)
    problem_names.sort()
    with open('sorted_problems.json', 'w') as f:
        json.dump(problem_names, f)
    return problem_names

fetch_all_problems()
print("Scraping finished.")