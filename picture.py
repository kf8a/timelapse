import cv
import ephem
import datetime

CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4

observer = ephem.Observer()
observer.lon = "-85:24"
observer.lat = "42:24"
sun = ephem.Sun()
sun.compute(observer)

if (ephem.now() > observer.previous_rising(sun)) & (ephem.now() < observer.next_setting(sun)):
  print "daylight"
  capture = cv.CaptureFromCAM(0)
  cv.SetCaptureProperty(capture,CV_CAP_PROP_FRAME_HEIGHT,960)
  cv.SetCaptureProperty(capture,CV_CAP_PROP_FRAME_WIDTH,1280)

  frame = cv.QueryFrame(capture)
  filename = 'images/'
  filename += str(datetime.datetime.now().isoformat())
  filename += '.png'
  cv.SaveImage(filename,frame)


