import cv
import ephem
from datetime import date, datetime

CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4

observer = ephem.Observer()
observer.lon = "-85:24"
observer.lat = "42:24"
sun = ephem.Sun()
sun.compute(observer)

today = ephem.localtime(ephem.now()).date()
rising = ephem.localtime(observer.previous_rising(sun)).date()
setting = ephem.localtime(observer.next_setting(sun)).date()

print today
print  rising
print setting

if (today == rising) & (today == setting):
  print "daylight"
  capture = cv.CaptureFromCAM(0)
  cv.SetCaptureProperty(capture,CV_CAP_PROP_FRAME_HEIGHT,960)
  cv.SetCaptureProperty(capture,CV_CAP_PROP_FRAME_WIDTH,1280)

  frame = cv.QueryFrame(capture)
  filename = 'images/'
  filename += str(datetime.now().isoformat())
  filename += '.png'
  cv.SaveImage(filename,frame)


