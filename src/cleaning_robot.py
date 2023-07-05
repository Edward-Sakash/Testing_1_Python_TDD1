class CleaningRobot:
    def __init__(self, testing_mode=False):
        self.testing_mode = testing_mode

    def run_motor(self, command):
        # Simulate motor running based on the command
        return f"{command.capitalize()} executed.\n"

    def unlock_door(self):
        if not self.testing_mode:
            return self.run_motor("unlock_door")
        return "Unlock_door executed.\n"

    def lock_door(self):
        if not self.testing_mode:
            return self.run_motor("lock_door")
        return "Lock_door executed.\n"

    def enter_door(self):
        if not self.testing_mode:
            return self.run_motor("enter_door")
        return "Enter_door executed.\n"

    def turn_around(self):
        if not self.testing_mode:
            return self.run_motor("turn_around")
        return "Turn_around executed.\n"

    def when_encounter_inner_door(self):
        log = ""
        log += self.unlock_door()
        log += self.enter_door()
        return log

    def when_encounter_outer_door(self):
        log = ""
        log += self.turn_around()
        return log

    def when_encounter_prisoner(self):
        log = ""
        return log

    def when_encounter_guard(self):
        log = ""
        log += self.turn_around()
        return log
