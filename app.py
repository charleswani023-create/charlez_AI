from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# -----------------------------
# Knowledge base for IT questions
# -----------------------------
responses = {
    # HTML
    "html": "HTML (HyperText Markup Language) structures web pages. Example: <h1>Hello World</h1>",
    "div": "A <div> is a block-level container used to group content.",
    "span": "A <span> is an inline container for text or inline elements.",
    "form": "Forms collect user input. Example: <form><input type='text'></form>",
    "link": "Use <a href='url'>Link text</a> for hyperlinks.",
    "image": "Use <img src='image.jpg' alt='description'> for images.",
    "table": "Use <table>, <tr>, <td> to create tables.",

    # CSS
    "css": "CSS styles HTML. Example: h1 { color: red; font-size: 20px; }",
    "flexbox": "Flexbox is for layout. Example: display: flex; justify-content: center;",
    "grid": "Grid is for 2D layout. Example: display: grid; grid-template-columns: 1fr 1fr;",
    "animation": "CSS animations move elements. Example: @keyframes fade { from {opacity:0;} to {opacity:1;} }",
    "selector": "CSS selectors target HTML elements. Example: p { color: blue; }",
    "class": "Use .classname in CSS to style elements with class='classname'.",

    # JavaScript
    "javascript": "JavaScript adds interactivity. Example: alert('Hello World');",
    "variable": "Use let, const, or var. Example: let x = 5;",
    "function": "Functions perform tasks. Example: function greet() { alert('Hi'); }",
    "loop": "Loops repeat code. Example: for(let i=0;i<5;i++){ console.log(i); }",
    "event": "Events respond to actions. Example: button.onclick = function() { alert('Clicked'); }",
    "dom": "DOM lets JavaScript manipulate HTML. Example: document.getElementById('id').innerText = 'Hello';",
    "array": "Arrays store multiple values. Example: let arr = [1,2,3];",

    # Programming basics
    "programming": "Programming is giving instructions to a computer to perform tasks.",
    "algorithm": "An algorithm is a step-by-step method to solve a problem.",
    "variable": "Variables store data. Example: let name = 'Alice';",
    "loop": "Loops repeat tasks multiple times. Example: for, while loops.",
    "condition": "Conditions check logic. Example: if(x>5){...} else {...}",
    "varriables": "A varriable is a keyword which can be declared to a function. examples of varriables are let, var, and const . They are usually declared using keywords",
    "charles":"charles is a programmer who wrote python 3 in 2019 after completing his masters in computer science. He is now popular in AI programming and working as a project manager in South Sudan embassy tech company.",
    "django":"django is a framework used to create web apps using python and other technologies",
    "steps for creating a django app":"there are some steps for you to create a simple django app lets break it down step by step.1.create a virtual environment using: python -m venv env. 2.activate your virtual environment using: env\scripts\activate. 3.install django package using: pip install django. 4.create a requirements file using: pip freeze > requirements.txt. 5. create your project folder using: django-admin startproject core . 6. run your app using python manage.py runserver. this will display the default django dashboard.let me know if you want me to take you through some advance django",
    "Alfa elite": "this is a discussion group created by some united IT students at muni university led by Freaky. Do you want me to mention the names of the group members of alfa elite? just say yes i will do that for you right here",
    

    # IT concepts
    "computer": "computer is a device that processes data and executes programs.",
    "network": "A network connects computers to share data and resources.",
    "server": "A server provides services or data to other computers over a network.",
    "database": "Databases store structured data. Example: MySQL, PostgreSQL.",
    "html5": "HTML5 is the latest HTML standard with new elements like <section>, <article>.",
    "css3": "CSS3 is the latest CSS standard with animations, transitions, and flex/grid layouts.",
    "debug": "Debugging is finding and fixing errors in code.",
    "git": "Git is a version control system to track code changes.",
    "github": "GitHub is an online platform to host Git repositories.",
    "api": "API (Application Programming Interface) lets programs communicate with each other.",
    "responsive": "Responsive design makes web pages look good on all devices using CSS media queries.",
}

# -----------------------------
# Fallback for unknown questions
# -----------------------------
def unknown():
    return "Sorry, I don't have an answer for that yet. Try asking about HTML, CSS, JavaScript, programming, or IT concepts."

# -----------------------------
# Process user input
# -----------------------------
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return unknown()

# -----------------------------
# Flask routes
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]
    answer = get_response(user_input)
    return jsonify({"answer": answer})
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Replit provides the PORT
    app.run(host="0.0.0.0", port=port, debug=True)


#if __name__ == "__main__":
    #app.run(debug=True)
