class Katze:
    def __init__(self, name):
        self.name = name
    
    def miauen(self):
        return "Miau!"
    
    def begruessen(self):
        return f"{self.name} sagt: {self.miauen()}"

# Hauptprogramm
if __name__ == "__main__":
    katze = Katze("Miming")
    print(katze.begruessen())