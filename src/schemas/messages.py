from typing import Union

from pydantic import field_validator
from pywa_async.types import User

from src.core import BaseSchema


class UserResponse(BaseSchema):
    """
    Represents the response structure for a user.

    Attributes:
        id (str): The unique identifier of the user.
        name (str): The name of the user.
        phone_number (str): The phone number of the user.
    """

    wa_id: str
    name: str | None
    input: str


class MessageResponse(BaseSchema):
    """
    Represents the response structure for a message.

    Attributes:
        id (str): The unique identifier of the message.
        to_user (str): The recipient's phone number.
        from_phone_id (str): The phone number from which the message was sent.
    """

    id: str
    to_user: UserResponse
    from_phone_id: str

    @field_validator("to_user", mode="before")
    def validate_to_user(cls, value: Union[User, UserResponse]) -> UserResponse:
        """
        Validate the to_user field to ensure it is a valid UserResponse.

        Args:
            value (UserResponse): The user response to validate.

        Returns:
            UserResponse: The validated user response.
        """
        if isinstance(value, User):
            return UserResponse.model_validate(value, from_attributes=True)
        return value
