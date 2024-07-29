from flask import Blueprint, request, jsonify
from models import db, User, Recipe
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

main_routes = Blueprint('main', __name__)

@main_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@main_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@main_routes.route('/recipes', methods=['GET', 'POST'])
@jwt_required()
def recipes():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        title = data['title']
        description = data['description']
        recipe = Recipe(title=title, description=description, user_id=user_id)
        db.session.add(recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe created successfully'}), 201
    elif request.method == 'GET':
        recipes = Recipe.query.filter_by(user_id=user_id).all()
        return jsonify([{'id': r.id, 'title': r.title, 'description': r.description} for r in recipes])

@main_routes.route('/recipes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def recipe_detail(id):
    user_id = get_jwt_identity()
    recipe = Recipe.query.get_or_404(id)
    if recipe.user_id != user_id:
        return jsonify({'message': 'Unauthorized'}), 403
    if request.method == 'GET':
        return jsonify({'id': recipe.id, 'title': recipe.title, 'description': recipe.description})
    elif request.method == 'PUT':
        data = request.get_json()
        recipe.title = data['title']
        recipe.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Recipe updated successfully'})
    elif request.method == 'DELETE':
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe deleted successfully'})
