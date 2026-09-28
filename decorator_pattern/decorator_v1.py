from dataclasses import dataclass
from pizza import Pizza

@dataclass(slots=True)
class Decorator(Pizza):

    inner : Pizza