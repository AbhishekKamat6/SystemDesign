
from states.base import Base
from models.signal_color import SignalColor

class RedState(Base):

    @property
    def color(self):
        return SignalColor.RED