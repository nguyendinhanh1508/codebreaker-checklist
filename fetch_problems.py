from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

def fetch_all_problems():
    url = "https://codebreaker.xyz/problems"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    problem_names = []
    for link in soup.select('table#myTable a[href^="/problem/"]'):
        problem_name = link.text.strip()
        if problem_name:
            problem_names.append(problem_name)
    with open('problems.txt', 'w') as f:
        for problem in problem_names:
            f.write(f"{problem}\n")
    return problem_names

fetch_all_problems()
print("Scraping finished.")