class tv:
    def __init__(self):
        self.channel = 1
        self.volume = 5

    def volume_up(self):
        if self.volume < 10:
            self.volume += 1
            print(f"volume: {self.volume:.0f}")
        else:
            print("max volume")

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"volume: {self.volume:.0f}")
        else:
            print("minimum volume")

    def change_channel(self, newChennel):
        if newChennel > 0 and newChennel < 100:
            self.channel = newChennel
            print(f"current channel: {self.channel}")
        else:
            print("chennel not found")
