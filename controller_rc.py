import ctypes
import time
import sys

try:
    import keyboard
except ImportError:
    print("Run: pip install keyboard")
    sys.exit(1)

# ── Change these if needed ──────────────────────────
CONTROLLER = 0       # 0, 1, 2, or 3
MOTOR_POWER = 1.0    # 0.0 to 1.0
# ────────────────────────────────────────────────────

MOVE_MAP = {
    "w": (1.0, 1.0),
    "a": (0.0, 1.0),
    "d": (1.0, 0.0),
}

class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort),
                ("wRightMotorSpeed", ctypes.c_ushort)]

def load_xinput():
    for dll in ("xinput1_4", "xinput1_3", "xinput9_1_0", "xinput1_2", "xinput1_1"):
        try:
            return ctypes.windll.LoadLibrary(dll)
        except OSError:
            continue
    print("XInput not found. Make sure you're on Windows with a controller connected.")
    sys.exit(1)

xinput = load_xinput()

def set_vibration(left, right):
    l = int(max(0.0, min(1.0, left * MOTOR_POWER)) * 65535)
    r = int(max(0.0, min(1.0, right * MOTOR_POWER)) * 65535)
    xinput.XInputSetState(CONTROLLER, ctypes.byref(XINPUT_VIBRATION(l, r)))

def main():
    print("Controller RC Car | W=Forward  A=Left  D=Right  ESC=Quit")
    print("Place controller face-down on a smooth hard surface.\n")

    try:
        while True:
            if keyboard.is_pressed("esc"):
                break

            active = [k for k in MOVE_MAP if keyboard.is_pressed(k)]

            if not active:
                set_vibration(0, 0)
                time.sleep(0.01)
                continue

            left = max(MOVE_MAP[k][0] for k in active)
            right = max(MOVE_MAP[k][1] for k in active)
            set_vibration(left, right)
            time.sleep(0.01)

    except KeyboardInterrupt:
        pass
    finally:
        set_vibration(0, 0)
        print("Stopped.")

if __name__ == "__main__":
    main()