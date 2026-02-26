class Engine:
    def start(self): print("[Engine] Engine started successfully")

class CarWithEngine:
    def __init__(self):
        self.engine = Engine() # Composition (Car owns the Engine)
        print("[Comp] Car built with internal Engine")

class Player:
    def __init__(self, name): self.name = name

class Team:
    def __init__(self, players):
        self.players = players # Aggregation (Team uses Players)
        print(f"[Aggr] Team formed with {len(self.players)} players")

# Execution
my_car = CarWithEngine()
my_car.engine.start()

p1, p2 = Player("Messi"), Player("Ronaldo")
my_team = Team([p1, p2])