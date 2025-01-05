class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        bcw = self.name
        acw = f"{{Name: {bcw}, Health: {self.health}, Hidden: {self.hidden}}}"
        return acw

    @staticmethod
    def print_alive() -> str:
        return str(Animal.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
