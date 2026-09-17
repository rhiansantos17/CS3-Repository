class hero_one:
    def __init__(self, health_one):
        self.health = health_one - 10


class hero_two:
    def __init__(self, health_two):
        self.assigned = health_two


Arthur = hero_one(100)
Morgana = hero_two(100)

print(Arthur.health)
print(Morgana.assigned)

