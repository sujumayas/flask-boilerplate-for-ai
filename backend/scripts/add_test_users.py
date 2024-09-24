from app import create_app, db
from app.models.user import User

def add_test_users():
    app = create_app()
    with app.app_context():
        # Clear existing users
        User.query.delete()
        
        # Add test users
        users = [
            User(username="alice", email="alice@example.com"),
            User(username="bob", email="bob@example.com"),
            User(username="charlie", email="charlie@example.com")
        ]
        
        db.session.add_all(users)
        db.session.commit()
        
        print("Test users added successfully!")

if __name__ == "__main__":
    add_test_users()