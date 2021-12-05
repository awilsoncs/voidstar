# Oh No! It's THE HORDE!

Oh No! It's THE HORDE is a classic fantasy roguelike with tower defense elements.

Protect your village by killing all of the hordelings.

## Build Notes

### Steps to Build On Windows 10

1. Install Python 9. The build is not compatible with subsequent versions (as of this writing).
2. Create a virtualenv in PowerShell


    & 'C:\Program Files\Python39\python.exe' -m venv horde-venv

3. Activate the venv.

    
    ./horde-venv/Scripts/Activate.ps1

4. Install the dependencies.


    pip install -r $GAME_TOP_DIR/requirements.txt

5. Run the build.


    make dist

6. Optionally, push the build.


    make push
