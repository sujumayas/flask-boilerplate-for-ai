# backend/app/repositories/user_repository.py
from app import db
from app.models.user import User

class UserRepository:
    def add_user(self, user):
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)  # This ensures the user object has the latest data from the database
        return user

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def get_all_users(self):
        return User.query.all()

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()