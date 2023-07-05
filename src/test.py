from cleaning_robot import CleaningRobot


def test_inner_door_encounter():
    robot = CleaningRobot(testing_mode=True)
    log = robot.when_encounter_inner_door()

    # Test unlocking the door
    assert "Unlock_door" in log

    # Test entering the door
    assert "Enter_door" in log


def test_outer_door_encounter():
    robot = CleaningRobot(testing_mode=True)
    log = robot.when_encounter_outer_door()

    # Test turning around
    assert "Turn_around" in log

    # Test not unlocking the door
    assert "Unlock_door" not in log

    # Test not entering the door
    assert "Enter_door" not in log

    # Test not locking the door
    assert "Lock_door" not in log


def test_prisoner_encounter():
    robot = CleaningRobot(testing_mode=True)
    log = robot.when_encounter_prisoner()

    # Test that log is empty
    assert log == ""


def test_guard_encounter():
    robot = CleaningRobot(testing_mode=True)
    log = robot.when_encounter_guard()

    # Test turning around
    assert "Turn_around" in log

    # Test that log is not empty
    assert log != ""


# Run the tests
test_inner_door_encounter()
test_outer_door_encounter()
test_prisoner_encounter()
test_guard_encounter()

print("All tests ran successfully.")
