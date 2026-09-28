
from states.base import Base
from models.signal_color import SignalColor

class YellowState(Base):

    @property
    def color(self):
        return SignalColor.YELLOW