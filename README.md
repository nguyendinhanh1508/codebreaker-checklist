# Codebreaker problems checklist
# Overview
This is a web-application that allows their user to track theirs and other people's solved problems on codebreaker.xyz.<br>
It allows the user to enter their username and the number of problems they have solved and their solved problems will be displayed.<br>
# Structure
1. ```app.py``` - main application file:
- Handles routing and server logic.
- Fetches user's solved problems from **https://codebreaker.xyz**.
- Renders the template with data.
2. ```fetch_problems.py``` - scrape all the available problems on **codebreaker.xyz**:
- Create ```sorted_problems.json``` containing all the problem names.
3. ```requirements.txt```:
- All the dependencies.
4. ```static/style.css``` & ```templates/index.html```:
- Provide the template for ```app.py```
# Explaining the code
***```app.py```***
1. ```app = Flask(__name__)```:
- Init the flask application.
- ```__name__``` tells flask where to find templates/static files.
2. ```all_problems()```:
- Loads all the problems from ```sorted_problems.json```.
- Flow: Open JSON -> Load list of problems -> Return the list.
3. ```fetch_solved_problems(username)```:
- Constructs the profile url.
- Fetches the HTML page using ```requests```.
- Parses the HTML using ```BeautifulSoup```.
- Extracts the problem names from the HTML with class ```table-bordered```.
- Returns the list of solved problems.
4. Main route:
- Initializes **username**, **problems**, and **solved_problems**.
- If the request is a 'POST' form submission then it gets the username from the form and fetches the user's problems using ```fetch_solved_problems()```.
- Renders ```index.html``` with **problems**, **solved_problems** and **username**.

***```fetch_problems.py```***
1. Core function ```fetch_all_problems()```:
- ```requests.get(url)``` retrieves the HTML of **https://codebreaker.xyz/problems**.
- Uses ```BeautifulSoup``` to convert raw HTML into a searchable object.
- Search the problem names to find all ```<a>``` tags inside a table with ```id = "myTable"``` where href starts with ```/problem/``` . 
- ```link.text.strip()``` extracts all the problem names.
- Names are added to ```problem_names``` list.
- Sort the list and then use ```json.dump(problem_names, f)``` to write the list to ```sorted_problems.json```.
- Return the list
2. Script execution:
- Calls ```fetch_all_problems()``` to perform the scraping.
- Prints a confirmation message when done.


# Features
Simply input your **codebreaker username**<br>
The website will tell you how many problems **the user has solved** over the **total number of problems**<br>
This website also displays all the **available problems** sorted in *lexicographical order* in a grid style<br>
All the solved problems will be displayed in <span style="color: green">green</span>, white if not.<br>
