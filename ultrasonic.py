import serial
import time
# Assigned Pins:
	# S1: Blue(TX) to GPIO14, Green(RX) to GPIO15
	# S2: TX to GPIO4, RX to GPIO5
	# S3: TX to GPIO8, RX to GPIO9
	# S4: TX to GPIO12, RX to GPIO13
# Setting serial ports for each sensors, skip AMA1
ports=[
	serial.Serial("/dev/ttyAMA0",9600,timeout=0.1),
	serial.Serial("/dev/ttyAMA3",9600,timeout=0.1),
	serial.Serial("/dev/ttyAMA4",9600,timeout=0.1),
	serial.Serial("/dev/ttyAMA5",9600,timeout=0.1)
]
# Flushing ports and waiting for sensors to stabilize
for ser in ports:
	ser.reset_input_buffer()
time.sleep(1.0)

def read_dist(ser):
	data=ser.read(4)
	distance = (data[1] * 256 + data[2])
	return distance

def cpu_speed():
	with open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq") as cpu:
		return int(cpu.read().strip()) / 1000 # Convert to mHz

# Function version with just distances
def distance_read(ports):
	distances = [] 
	for ser in ports: # Add each distance reading
		dist = read_dist(ser)
		distances.append(dist)
	return distances

while True:
	distances = [] 
	for i, ser in enumerate(ports): # Add each distance reading
		dist = read_dist(ser)
		distances.append(dist)
	speed = cpu_speed()
	distances.append(f"CPU Speed: {speed}")
	print(" ".join(distances))
	time.sleep(0.05)

