
from states.base import Base
from models.signal_color import SignalColor

class GreenState(Base):

    @property
    def color(self):
        return SignalColor.GREEN