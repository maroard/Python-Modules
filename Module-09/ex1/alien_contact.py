from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\" "
                             "(Alien Contact)")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self

    def __str__(self) -> str:
        return (
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type.value}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: {self.message_received}"
        )


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    alien_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-04-10T10:30:00",
        contact_type="radio",
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )

    print("Valid contact report:")
    print(alien_contact)

    print()
    print("======================================")
    print("Expected validation error:")

    try:
        alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-04-10T10:30:00",
            contact_type="telepathic",
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as error:
        print(error.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
