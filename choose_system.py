from single_pendulum import SinglePendulum
from double_pendulum import DoublePendulum

def chooseSystem(sys, spInput, dpInput):
    if sys == "sp":
        #Create an instance of a SinglePendulum
        return SinglePendulum(spInput)
    elif sys == "dp":
        return DoublePendulum(dpInput)
    else:
        print("Please choose a valid system (sp or dp).")