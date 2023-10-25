import pyautogui
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import keyboard

GAME_REGION = (654, 170, 1246-654, 673-170)
LEVEL_REGION = (654, 140, 1246-654, 170-140)

patterns = []

def capture_screen(region):
    return pyautogui.screenshot(region=region)
