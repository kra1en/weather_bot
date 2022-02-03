from dataclasses import dataclass

@dataclass
class Settlement:
    id: int
    name: str
    region: str

@dataclass
class Coordinates:
    lat: float
    lon: float