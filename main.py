import subprocess
import sys
import multiprocessing

multiprocessing.freeze_support()

def run():
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    # To prevent infinite spawning problem
    run()
