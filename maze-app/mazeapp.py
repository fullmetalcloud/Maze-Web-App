from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, make_response
from mazebuilder import Mazebuilder

app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"
 
@app.route("/maze/<int:size>/")
def buildMaze(size):
  if(size > 1000): 
    return "Cannot build a maze greater than size 100 'Currently'"

  myMaze = Mazebuilder(size)
  myMaze.createMaze()

  return make_response(jsonify(maze=myMaze.maze), 200)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')