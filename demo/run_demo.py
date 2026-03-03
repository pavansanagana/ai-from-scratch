import subprocess
import sys

subprocess.check_call([sys.executable, "scripts/train_numpy.py"])
subprocess.check_call([sys.executable, "scripts/train_torch.py"])

print("\nDemo complete.\n")
