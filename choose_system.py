from single_pendulum import SinglePendulum
from double_pendulum import DoublePendulum

def chooseSystem(sys, input):
    if sys == "SP" or sys == "TEST_SP":
        return SinglePendulum(input)
    elif sys == "DP" or sys == "TEST_DP":
        return DoublePendulum(input)
    else:
        print("Please choose a valid system (SP or DP).")