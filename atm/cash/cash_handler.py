
# Note handler
class NoteHandler:
    def __init__(self,note_value:int,count:int):
        self.note_value = note_value
        self.count = count
        self.out : dict[int,int] = {}
        self.next : "NoteHandler|None"  = None # The double quotes are used because NoteHandler is referring to the class itself

    def link_next(self,next_handler:"NoteHandler") -> "NoteHandler" :
        self.next = next_handler
        return next_handler

    def refill(self,more:int):
        self.count+=more

    def plan(self, amount:int)->bool:
       use = min(amount // self.note_value , self.count)

       if use > 0 :
           self.out[self.note_value] = use

       remaining = amount - use * self.note_value

       if remaining == 0:
           return True
       elif self.next:
           return self.next.plan(remaining)
       return False

    def commit(self, plan=None):
        if plan is None:
         plan = {}

        if self.out:
         notes_used = self.out.get(self.note_value, 0)
         self.count -= notes_used
         plan.update(self.out)

        if self.next:
         return self.next.commit(plan)

        return plan
        

class Note2000Handler(NoteHandler):
    def __init__(self, count):
        super().__init__(2000, count)

class Note500Handler(NoteHandler):
    def __init__(self, count):
        super().__init__(500, count)

class Note100Handler(NoteHandler):
    def __init__(self, count):
        super().__init__(100, count)