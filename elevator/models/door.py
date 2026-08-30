from dataclasses import dataclass , field

@dataclass(slots=True) # slots=True basically means this object can only have the attributes I explicitly define
class Door:

    _is_open : bool = field(default=False,repr = False) # repr = False means don't include this attribute when Python automatically creates the object's repr()
    _obstructed : bool = field(default=False,repr=False)

    @property
    def is_open(self)->bool:
        return self._is_open

    @property
    def obstructed(self)->bool:
        return self._obstructed

    @obstructed.setter
    def obstructed(self,value):
        self._obstructed = value

    def open(self):
        self.open = True

    def close(self)->bool:
        if self._obstructed == True:
            return False

        self._is_open = False

        return True

