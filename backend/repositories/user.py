from uuid import UUID

from sqlalchemy import select

from models.user import User, UserModel
from db import Session


def get_user(id: UUID) -> UserModel:
    with Session() as session:
        # Query to select the user by ID
        stmt = select(User).filter(User.id == id)
        result = session.execute(stmt).scalar_one_or_none()

        if result:
            # Return the result as a UserModel
            return UserModel.model_validate(result)
        else:
            # Handle case where user is not found (optional)
            raise ValueError(f"User with ID {id} not found")
