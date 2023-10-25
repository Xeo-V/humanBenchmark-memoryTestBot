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

def get_level(region):
    screenshot = capture_screen(region)
    screenshot_np = np.array(screenshot)
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray_screenshot, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)
