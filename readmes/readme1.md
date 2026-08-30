## Type Hints, Forward References & `"Elevator" | None`

### 1. Circular imports with type hints

If `elevator.py` imports `ElevatorState`, and `elevator_state.py` imports `Elevator`, we get a circular import:

```text
elevator.py
    ↓
ElevatorState
    ↓
Elevator
    ↓
❌ Circular import
```

If `Elevator` is only needed for a type hint, use `TYPE_CHECKING`:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.elevator import Elevator
```

Then use a forward reference:

```python
def step(self, car: "Elevator") -> None:
    ...
```

---

### 2. Why `"Elevator" | None` causes an error

This is **wrong**:

```python
def pick_car(self) -> "Elevator" | None:
```

Because `"Elevator"` is a **string value**, not the `Elevator` class.

Python effectively tries to evaluate:

```python
"Elevator" | None
```

So it is trying to apply `|` to a string and `None`, which causes:

```text
TypeError: unsupported operand type(s) for |: 'str' and 'NoneType'
```

```text
"Elevator" is a tring value not a type and because of which it throws an error
```

---

### 3. Correct ways

#### Option 1: Quote the entire annotation

```python
def pick_car(self) -> "Elevator | None":
    ...
```

The entire expression is treated as a forward-reference string.

#### Option 2: Recommended — use postponed annotations

```python
from __future__ import annotations
```

Then:

```python
def pick_car(self) -> Elevator | None:
    ...
```

Python postpones evaluation of the annotation, so `Elevator` does not need to be imported at runtime.

---

### 4. Important distinction

```python
Elevator       # actual class/type
"Elevator"     # string containing the word "Elevator"
```

Similarly:

```python
"Elevator" | None
```

does **not** mean:

> Elevator OR None

It means Python is trying to apply `|` to a string and `None`.

With postponed annotations:

```python
Elevator | None
```

means:

> The value can be an `Elevator` or `None`.

---

### 5. Recommended pattern for this LLD

For classes that refer to each other only through type hints:

```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.elevator import Elevator
```

Then freely write:

```python
def step(self, car: Elevator) -> None:
    ...

def pick_car(self, cars: list[Elevator]) -> Elevator | None:
    ...
```

This avoids circular imports while keeping the type hints clear.
