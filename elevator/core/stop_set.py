from dataclasses import dataclass , field
import threading
import bisect

@dataclass(slots=True)
class StopSet:

    _stops : list[int] =field(default_factory=list)
    _lock : threading.Lock = field(default_factory=threading.Lock , repr= False)
    _is_empty : bool = field(default=False)

    @property
    def is_empty(self):
         return self._is_empty


    def add(self,floor:int):
        with self._lock :
           index = bisect.bisect_left(self._stops,floor) # it finds the leftmost position where a value can be inserted into an already sorted list without breaking the sorted order.
           if index >= len(self._stops) or self._stops[index] != floor:
             self._stops.insert(index,floor) 

    def remove(self,floor:int):
        with self._lock:
           index = bisect.bisect_left(self._stops,floor)
           if index < len(self._stops) and self._stops[index] == floor:
             self._stops.pop(index)


    def contains(self,floor:int)->bool:
        with self._lock : 
           index = bisect.bisect_left(self._stops,floor)
           return index < len(floor) and self._stops[index] == floor

    def floor(self,floor:int)->int|None:
       """Largest stop <= floor, or None."""
       with self._lock : 
          index = bisect.bisect_right(self._stops,floor)
          return self._stops[index-1] if index > 0 else None

    def ceiling(self,floor:int) : 
        """Smallest stop >= floor, or None."""
        with self._lock :
           index = bisect.bisect_left(self._stops,floor)
           return self._stops[index] if index < len(self._stops) else None

    def snapshot(self) -> list[int]:
        with self._lock:
            return list(self._stops)
    
          
 
    