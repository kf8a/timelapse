import cv
import os
import time
import ephem
from datetime import date, datetime

CV_CAP_PROP_POS_FRAMES    = 1
CV_CAP_PROP_FRAME_WIDTH   = 3
CV_CAP_PROP_FRAME_HEIGHT  = 4
CV_CAP_PROP_BRIGHTNESS    = 10
CV_CAP_PROP_EXPOSURE      = 15

observer = ephem.Observer()
observer.lon = "-85:24"
observer.lat = "42:24"
sun = ephem.Sun()
sun.compute(observer)

today = ephem.localtime(ephem.now()).date()
rising = ephem.localtime(observer.previous_rising(sun)).date()
setting = ephem.localtime(observer.next_setting(sun)).date()

if (today == rising) & (today == setting):
  capture = cv.CaptureFromCAM(0)
  cv.SetCaptureProperty(capture,CV_CAP_PROP_FRAME_HEIGHT,720)
  cv.SetCaptureProperty(capture,CV_CAP_PROP_FRAME_WIDTH,1280)

  frame = cv.QueryFrame(capture)
  time.sleep(1)
  frame = cv.QueryFrame(capture)
  time.sleep(1)
  frame = cv.QueryFrame(capture)
  filename = '/home/pi/images/'
  filename += str(datetime.now().isoformat())
  filename += '.png'
  cv.SaveImage(filename,frame)
  os.unlink("/home/pi/images/current.png")
  os.symlink(filename, "/home/pi/images/current.png")
