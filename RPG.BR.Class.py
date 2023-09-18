
class DiceRoller:
    def __init__(self, tod: int, nod: int, mod: str):
    # tod = type of die
    # nod = number of die
    # mod = modifier -> move to own method?
        self.tod = tod
        self.nod = nod
        self.mod = mod
        self.rolls = []
    
    