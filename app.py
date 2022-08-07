from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route("/")
def home():
  """Show form to request words."""

  prompts = story.prompts

  return render_template("home.html", prompts=prompts)

@app.route("/story")
def show_story():
  """Display the story result."""

  text = story.generate(request.args)
  return render_template("story.html", text=text)
