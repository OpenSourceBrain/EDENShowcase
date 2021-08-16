import eden_simulator
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "LEMS_2007One.xml"
print(
    "Running a simulation of %s in EDEN v%s"
    % (
        filename,
        eden_simulator.__version__ if hasattr(eden_simulator, "__version__") else "???",
    )
)

results = eden_simulator.runEden(filename)
