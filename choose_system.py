from single_pendulum import SinglePendulum
from double_pendulum import DoublePendulum

def chooseSystem(sys, input):
    if sys == "SP":
        return SinglePendulum(input)
    elif sys == "DP":
        return DoublePendulum(input)
    else:
        print("Please choose a valid system (SP or DP).")