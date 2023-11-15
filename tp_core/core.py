from src.controller.controller import save
from src.tp_core.sub_core import return_meaning_of_life

def add(x, y):
    save(x)
    save(y)
    return x + y
