from typing import Any

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Base schema for all request and response models.
    """

    model_config = ConfigDict(
        extra="ignore",  # Disallow extra fields
        str_strip_whitespace=True,  # Strip whitespace from strings
        use_enum_values=True,  # Use enum values instead of names
        from_attributes=True,  # Allow model creation from attributes
    )

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the model to a dictionary.

        Returns:
            dict: The model as a dictionary.
        """
        return self.model_dump(mode="json")
