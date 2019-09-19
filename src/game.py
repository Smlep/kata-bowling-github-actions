class Game:
    def __init__(self):
        self.rolls = []

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        res = 0
        frame_index = 0
        for i in range(10):
            if self.is_strike(frame_index):
                res += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                res += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                res += self.sum_of_balls_in_frame(frame_index)
                frame_index += 2
        return res
