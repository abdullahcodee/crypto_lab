from app import db
from app import User

# Retrieve all users from the User table
all_users = User.query.all()

# Print the details of each user
for user in all_users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
