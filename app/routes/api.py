from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db
import email 
import json
import sys

from app.models.ToDo import ToDo



bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()

  try:
    # attempt creating a new user
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )

    db.add(newUser)
    db.commit()
  except:
    # insert failed, so send error to front end
    print(sys.exc_info()[0])
    db.rollback()
    return jsonify(message = 'Signup failed'), 500

  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  return jsonify(id = newUser.id)


@bp.route('/users/logout', methods=['POST'])
def logout():
    # below removes session varaibles
    session.clear()
    return '', 204

# Post route for user logins

@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()
  
  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
   print(sys.exc_info()[0])
 
  if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect credentials'), 400
      
  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)



# below contains route for users to create a Task

@bp.route('/todos', methods=['POST'])
def create():
  data = request.get_json()
  db = get_db()

  try:
    # create a new task
    newToDo = ToDo(
      title = data['title'],
      descr = data['descr'],
      user_id = session.get('user_id')
    )

    db.add(newToDo)
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Task failed'), 500

  return jsonify(id = newToDo.id)

# below contains the route to update a Task
@bp.route('/todos/<id>', methods=['PUT'])
def update(id):
  data = request.get_json()
  db = get_db()

  try:
    # retrieve post and update title property
    todos = db.query(ToDo).filter(ToDo.id == id).one()
    todos.title = data['title']
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Post not found'), 404

  return '', 204

# below contains route to delete posts

@bp.route('/todos/<id>', methods=['DELETE'])
def delete(id):
  db = get_db()

  try:
    # delete post from db
    db.delete(db.query(ToDo).filter(ToDo.id == id).one())
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Post not found'), 404

  return '', 204    
