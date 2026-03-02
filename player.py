from dataclasses import dataclass, field

@dataclass
class Player:
    name: str
    color: str
    armies_available: int = 0
    territories: set = field(default_factory=set)
    cards: list = field(default_factory=list)
    eliminated: bool = False