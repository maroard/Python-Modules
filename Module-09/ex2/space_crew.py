from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")
        if not any(
            crew_member.rank in (Rank.captain, Rank.commander)
            for crew_member in self.crew
        ):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced_crew_members = [crew_member
                                        for crew_member in self.crew
                                        if crew_member.years_experience >= 5]
            if len(experienced_crew_members) < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need "
                                 "50% experienced crew (5+ years)")
        if not all(crew_member.is_active for crew_member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def __str__(self) -> str:
        info = (
            f"Mission: {self.mission_name}\n"
            f"ID: {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration: {self.duration_days} days\n"
            f"Budget: ${self.budget_millions}M\n"
            f"Crew Size: {len(self.crew)}\n"
            "Crew members:"
        )
        for member in self.crew:
            info += (f"\n- {member.name} ({member.rank.value}) "
                     f"- {member.specialization}")

        return info


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    space_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-04-10T10:30:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="SC_001",
                name="Sarah Connor",
                rank="commander",
                age=37,
                specialization="Mission Command",
                years_experience=17,
            ),
            CrewMember(
                member_id="JS_001",
                name="John Smith",
                rank="lieutenant",
                age=31,
                specialization="Navigation",
                years_experience=11,
            ),
            CrewMember(
                member_id="AJ_001",
                name="Alice Johnson",
                rank="officer",
                age=26,
                specialization="Engineering",
                years_experience=3,
            ),
        ]
    )

    print("Valid mission created:")
    print(space_mission)

    print()
    print("=========================================")
    print("Expected validation error:")

    try:
        space_mission = SpaceMission(
            mission_id="M2025_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2025-04-10T10:30:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="SC_001",
                    name="Sarah Connor",
                    rank="lieutenant",
                    age=37,
                    specialization="Mission Command",
                    years_experience=17,
                ),
                CrewMember(
                    member_id="JS_001",
                    name="John Smith",
                    rank="officer",
                    age=31,
                    specialization="Navigation",
                    years_experience=11,
                ),
                CrewMember(
                    member_id="AJ_001",
                    name="Alice Johnson",
                    rank="cadet",
                    age=26,
                    specialization="Engineering",
                    years_experience=3,
                ),
            ]
        )
    except ValidationError as error:
        print(error.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
