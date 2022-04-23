'''For trial plotting'''
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
import matplotlib.pyplot as plt
import matplotlib.animation as animation


i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])


# Parameters
x_len = 200        # Number of points to display
y_range = [-20, 20]  # Range of possible Y values to display

# Create figure for plotting
#fig = plt.figure(figsize=(20, 40), constrained_layout=True)
#spec = fig.add_gridspec(ncols=3, nrows=3)
#ax1 = fig.add_subplot(spec[0,0])
#ax2 = fig.add_subplot(spec[1,0])
#ax3 = fig.add_subplot(spec[-1,0])

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex='col', sharey='row', figsize=(20, 40))

xs = list(range(0, 200))
ys1 = [0] * x_len
ys2 = [0] * x_len
ys3 = [0] * x_len


ax1.set_ylim(y_range)
ax2.set_ylim(y_range)
ax3.set_ylim(y_range)


# Add labels
plt.suptitle('Seismic Acceleration')
fig.text(0.04, 0.5,'Amplitude(m/s$^2$)',  va='center', rotation='vertical')
#plt.title('Seismic Acceleration')
plt.xlabel('Time(s)')
ax1.set_ylabel('Acceleration_Z')
ax2.set_ylabel('Acceleration_Y')
ax3.set_ylabel('Acceleration_X')

# Create a blank line. We will update the line in animate
line1, = ax1.plot(xs, ys1, color='red', marker='o')
line2, = ax2.plot(xs, ys2, color='blue', marker='o')
line3, = ax3.plot(xs, ys3, color='orange', marker='o')

# This function is called periodically from FuncAnimation
def animate(i, ys1, ys2, ys3):

    # Add y to list the mean of all sensors
    ys1.append((accel_1.acceleration[2]+accel_2.acceleration[2]+accel_3.acceleration[2]+accel_4.acceleration[2])/4)
    ys2.append((accel_1.acceleration[1]+accel_2.acceleration[1]+accel_3.acceleration[1]+accel_4.acceleration[1])/4)
    ys3.append((accel_1.acceleration[0]+accel_2.acceleration[0]+accel_3.acceleration[0]+accel_4.acceleration[0])/4)

    # Limit y list to set number of items
    ys1 = ys1[-x_len:]
    ys2 = ys2[-x_len:]
    ys3 = ys3[-x_len:]

    # Update line with new Y values
    line1.set_ydata(ys1)
    line2.set_ydata(ys2)
    line3.set_ydata(ys3)

    return line1, line2, line3,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys1,ys2,ys3,),
    interval=50,
    blit=True)
plt.show()