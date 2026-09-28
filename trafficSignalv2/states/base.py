


from abc import ABC , abstractmethod


class Base(ABC):

  @property
  @abstractmethod
  def color(self):
    pass
