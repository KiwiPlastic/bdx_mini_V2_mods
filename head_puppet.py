"""
Sets up the robot in init position, you control the head with the xbox controller
"""

import time
import numpy as np
from mini_bdx_runtime.rustypot_position_hwi import HWI
from mini_bdx_runtime.duck_config import DuckConfig
from mini_bdx_runtime.xbox_controller import XBoxController


from mini_bdx_runtime.eyes import Eyes
from mini_bdx_runtime.sounds import Sounds
from mini_bdx_runtime.antennas import Antennas
from mini_bdx_runtime.projector import Projector

duck_config = DuckConfig()

xbox_controller = XBoxController(50, only_head_control=True)

if duck_config.speaker:
    sounds = Sounds(volume=1.0, sound_directory="../mini_bdx_runtime/assets/")
if duck_config.antennas:
    antennas = Antennas()
if duck_config.eyes:
    eyes = Eyes()
if duck_config.projector:
    projector = Projector()

lcd_eyes_command = 0               #index value to connect to buttons
lcd_eyes_mode = 0
eyes.run(lcd_eyes_command)         # set 5-bit Bus to zero

last_head_yaw_pos_rad = 0
last_head_roll_pos_rad = 0
last_head_pitch_pos_rad= 0

hwi = HWI(duck_config)

kps = [8] * 14
kds = [0] * 14

hwi.set_kps(kps)
hwi.set_kds(kds)
hwi.turn_on()

limits = {
    "neck_pitch": [-20, 60],
    "head_pitch": [-60, 45],
    "head_yaw": [-60, 60],
    "head_roll": [-20, 20],
}

try:
    while True:

        last_commands, buttons, left_trigger, right_trigger = (
            xbox_controller.get_last_command()
        )

        l_x = last_commands[5]
        l_y = last_commands[4]
        r_x = last_commands[6]
        # r_y = last_commands[3]

        head_yaw_deg = (
            l_x * (limits["head_yaw"][1] - limits["head_yaw"][0]) / 2
            + (limits["head_yaw"][1] + limits["head_yaw"][0]) / 2
        )
        head_yaw_pos_rad = np.deg2rad(head_yaw_deg)

        head_roll_deg = (
            r_x * (limits["head_roll"][1] - limits["head_roll"][0]) / 2
            + (limits["head_roll"][1] + limits["head_roll"][0]) / 2
        )
        head_roll_pos_rad = np.deg2rad(head_roll_deg)

        head_pitch_deg = (
            l_y * (limits["head_pitch"][1] - limits["head_pitch"][0]) / 2
            + (limits["head_pitch"][1] + limits["head_pitch"][0]) / 2
        )
        head_pitch_pos_rad = np.deg2rad(head_pitch_deg)

        # neck_pitch_deg = (
        #     -r_y * (limits["neck_pitch"][1] - limits["neck_pitch"][0]) / 2
        #     + (limits["neck_pitch"][1] + limits["neck_pitch"][0]) / 2
        # )
        # neck_pitch_pos_rad = np.deg2rad(neck_pitch_deg)

        hwi.set_position("head_yaw", head_yaw_pos_rad)
        hwi.set_position("head_roll", head_roll_pos_rad)
        hwi.set_position("head_pitch", head_pitch_pos_rad)
        # hwi.set_position("neck_pitch", neck_pitch_pos_rad)

        if duck_config.eyes:                                # LCD EYES 
            if buttons.A.triggered:                         # A  Expression 1 - 4
                lcd_eyes_mode += 1
                if lcd_eyes_mode > 4:
                    lcd_eyes_mode = 1
                lcd_eyes_command = lcd_eyes_mode
                eyes.run(lcd_eyes_command)
            #if buttons.back.triggered:                      # back Hoz Flicker
            if xbox_controller.back_pressed:
                lcd_eyes_command = 5
                eyes.run(lcd_eyes_command)
            if buttons.start.triggered:                     # start Vert Flicker
                lcd_eyes_command = 6
                eyes.run(lcd_eyes_command)
            if buttons.guide.triggered:                     # guide Invert display
                lcd_eyes_command = 7
                eyes.run(lcd_eyes_command)
            if buttons.LB.triggered:                        # LB Wink
                lcd_eyes_command = 8
                eyes.run(lcd_eyes_command)
            if buttons.RB.triggered:                        # RB Blink
                lcd_eyes_command = 9
                eyes.run(lcd_eyes_command)
            if buttons.LSB.triggered:                       # LSB Animation laugh
                lcd_eyes_command = 10
                eyes.run(lcd_eyes_command)
            if buttons.RSB.triggered:                       # RSB Animation Confused
                lcd_eyes_command = 11
                eyes.run(lcd_eyes_command)
            # curiosity toggle  = 12
            # Position center = 13                
            if xbox_controller.dpad_up_pressed:             # dpad Position North
                lcd_eyes_command = 14
                eyes.run(lcd_eyes_command)
                xbox_controller.dpad_up_pressed = False
            if xbox_controller.dpad_up_right_pressed:       # dpad Position North East
                lcd_eyes_command = 15
                eyes.run(lcd_eyes_command)
                xbox_controller.dpad_up_right_pressed = False
            if xbox_controller.dpad_right_pressed:          # dpad Position East
                lcd_eyes_command = 16
                eyes.run(lcd_eyes_command)
                xbox_controller.dpad_right_pressed = False
            if xbox_controller.dpad_down_right_pressed:     # dpad Position SE
                lcd_eyes_command = 17
                eyes.run(lcd_eyes_command)
                xbox_controller.dpad_down_right_pressed = False 
            if xbox_controller.dpad_down_pressed:           # dpad Position S
                lcd_eyes_command = 18
                eyes.run(lcd_eyes_command)
                xbox_controller.dpad_down_pressed = False
            if xbox_controller.dpad_down_left_pressed:      # dpad Position SW
                lcd_eyes_command = 19
                eyes.run(lcd_eyes_command)
                xbox_controller.dpad_down_left_pressed = False 
            if xbox_controller.dpad_left_pressed:           # dpad Position W
                lcd_eyes_command = 20
                eyes.run(lcd_eyes_command)
                xbox_controller.dpad_left_pressed = False
            if xbox_controller.dpad_up_left_pressed:        # dpad Position NW
                lcd_eyes_command = 21
                eyes.run(lcd_eyes_command)
                xbox_controller.dpad_up_left_pressed = False
            if xbox_controller.lcd_bus_clear:               # Flag to write 0 on bus
                lcd_eyes_command = 0
                eyes.run(lcd_eyes_command)
                xbox_controller.lcd_bus_clear = False
            if (head_yaw_pos_rad != last_head_yaw_pos_rad) or (head_roll_pos_rad != last_head_roll_pos_rad) or (head_pitch_pos_rad != last_head_pitch_pos_rad):
                #neck_pitch_pos_rad   
                lcd_eyes_command = 31
                eyes.run(lcd_eyes_command)
                last_head_yaw_pos_rad = head_yaw_pos_rad
                last_head_roll_pos_rad = head_roll_pos_rad
                last_head_pitch_pos_rad= head_pitch_pos_rad
                #last_neck_pitch_pos_rad = neck_pitch_pos_rad
            if (lcd_eyes_command == 31):                    # Head moving
                if (head_yaw_pos_rad == last_head_yaw_pos_rad) and (head_roll_pos_rad == last_head_roll_pos_rad) and (head_pitch_pos_rad == last_head_pitch_pos_rad):
                    xbox_controller.lcd_bus_clear = True

        if duck_config.antennas:                            #left/Right Trigger - Antennas
            antennas.set_position_left(right_trigger)
            antennas.set_position_right(left_trigger)

        if buttons.B.triggered:                             # B Button - Speaker random sound
            if duck_config.speaker:
                sounds.play_random_sound()

        if buttons.X.triggered:                             # X button - Projector ON/OFF
            if duck_config.projector:
                projector.switch()

        # pygame.event.pump()  # process event queue
        time.sleep(1 / 60)
except KeyboardInterrupt:
    if duck_config.antennas:
        antennas.stop()
