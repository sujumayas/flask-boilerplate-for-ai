# backend/app/services/user_service.py
from app.repositories.user_repository import UserRepository
from app.models.user import User
from flask import current_app
from sqlalchemy.exc import IntegrityError

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
    
    def create_user(self, user_data):
        try:
            current_app.logger.info(f"Creating user with data: {user_data}")
            user = User(username=user_data['username'], email=user_data['email'])
            created_user = self.user_repo.add_user(user)
            if created_user and created_user.id:
                current_app.logger.info(f"User created successfully: {created_user.id}")
                return created_user
            else:
                current_app.logger.error("User creation failed: User object is None or has no ID")
                raise ValueError("User creation failed")
        except IntegrityError:
            current_app.logger.warning(f"Attempted to create user with existing email: {user_data.get('email')}")
            raise
        except Exception as e:
            current_app.logger.error(f"Error in create_user service: {str(e)}", exc_info=True)
            raise
    
    def list_users(self):
        return self.user_repo.get_all_users()
    
    def find_user(self, user_id):
        return self.user_repo.get_user_by_id(user_id)
    
    def remove_user(self, user_id):
        self.user_repo.delete_user(user_id)
