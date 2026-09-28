
from beverages.base import Base
from dataclasses import dataclass


@dataclass(slots=True)
class BeverageDecorator(Base):
    inner : Base