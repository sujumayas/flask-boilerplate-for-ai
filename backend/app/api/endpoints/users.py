# backend/app/api/endpoints/users.py
from flask import jsonify, request, current_app
from app.api import api_bp
from app.services.user_service import UserService
from sqlalchemy.exc import IntegrityError

user_service = UserService()

@api_bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.list_users()
    return jsonify([user.to_dict() for user in users]), 200

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.find_user(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@api_bp.route('/users', methods=['POST'])
def create_user():
    try:
        current_app.logger.info("Received POST request to create user")
        data = request.get_json()
        current_app.logger.debug(f"Received user data: {data}")
        
        if not data:
            current_app.logger.warning("No JSON data received in request")
            return jsonify({'error': 'No input data provided'}), 400
        
        # Validate required fields
        required_fields = ['username', 'email']
        for field in required_fields:
            if field not in data:
                current_app.logger.warning(f"Missing required field: {field}")
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        user = user_service.create_user(data)
        current_app.logger.info(f"User created successfully with id: {user.id}")
        return jsonify(user.to_dict()), 201
    except IntegrityError as e:
        current_app.logger.warning(f"Attempted to create user with existing email: {data.get('email')}")
        return jsonify({'error': 'A user with this email already exists'}), 409
    except Exception as e:
        current_app.logger.error(f"Error creating user: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500

@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.remove_user(user_id)
    return jsonify({'message': 'User deleted'}), 200
