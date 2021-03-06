import sys, getopt

sys.path.append('.')
import RTIMU
import os.path, time, math, numpy
from threading import Thread


SETTINGS_FILE = "RTIMULib"
threshold = 10
samples = 20


print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
	print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
	print("IMU init failed")
	sys.exit(1)
else:
	print("IMU init succeeded")

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended poll interval: %dmS, attempting to connect\n" % poll_interval)

# while not imu.IMURead():
# 	# waiting...
# 	print "."


#pastReadings = []

def getReading():
	data = imu.getIMUData()
	print 'data %s' % data
	return data["fusionPose"][2]



# def readData():
# 	global pastReadings
# 	while True:
# 		# x, y, z = imu.getFusionData()
# 		# print("%f %f %f" % (x,y,z))
# 		pastReadings.append(getReading())
# 		if len(pastReadings) > samples:
# 			pastReadings = pastReadings[-samples:]
# 		time.sleep(poll_interval*1.0/1000.0)


# monitor = Thread(target = readData())
# monitor.start()
# 
# 
# def unusual():
# 	global pastReadings
# 	median = numpy.median(numpy.array(pastReadings))
# 	yaw = getReading()
# 	return yaw > median + threshold or yaw < median - threshold



