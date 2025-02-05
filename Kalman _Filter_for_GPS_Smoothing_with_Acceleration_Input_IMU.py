# Kalman Filter for GPS Smoothing with Acceleration Input (IMU)


import numpy as np
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter

# Time step
dt = 1.0  # 1 second (adjust as needed)

# Initialize Kalman Filter
kf = KalmanFilter(dim_x=4, dim_z=2)

# State Transition Matrix (A)
kf.F = np.array([[1, 0, dt, 0],  # x = x + vx*dt
                 [0, 1, 0, dt],  # y = y + vy*dt
                 [0, 0, 1, 0],   # vx = vx
                 [0, 0, 0, 1]])  # vy = vy

# Control Matrix (B) - For acceleration input
kf.B = np.array([[0.5 * dt**2, 0],
                 [0, 0.5 * dt**2],
                 [dt, 0],
                 [0, dt]])

# Measurement Matrix (H) - GPS provides only position (x, y)
kf.H = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0]])

# Process Noise Covariance (Q) - Represents model uncertainty
kf.Q = np.array([[0.1, 0, 0, 0],
                 [0, 0.1, 0, 0],
                 [0, 0, 0.1, 0],
                 [0, 0, 0, 0.1]])

# Measurement Noise Covariance (R) - GPS noise
kf.R = np.array([[5, 0],
                 [0, 5]])

# Initial State [x, y, vx, vy] - Assume starting at (0,0) with no velocity
kf.x = np.array([[0], [0], [0], [0]])

# Initial Covariance Matrix (P) - High uncertainty in velocity
kf.P = np.eye(4) * 500

# Simulated Noisy GPS Measurements
gps_measurements = np.array([[0, 0], [1, 2], [2, 3], [3, 5], [5, 8], [7, 11], [9, 14]])

# Simulated IMU Acceleration Data (assume some external force acting)
accel_inputs = np.array([[0.2, 0.1],  # Acceleration at each step (ax, ay)
                         [0.3, 0.1],
                         [0.1, 0.05],
                         [0.05, 0.02],
                         [0, -0.1],
                         [-0.1, -0.2],
                         [-0.2, -0.3]])

filtered_positions = []

# Run Kalman Filter with IMU input
for z, u in zip(gps_measurements, accel_inputs):
    kf.predict(u=np.array(u).reshape(2, 1))  # Predict with acceleration input
    kf.update(z)  # Update with GPS measurement
    filtered_positions.append(kf.x[:2].flatten())  # Store filtered position

# Convert results to NumPy array for plotting
filtered_positions = np.array(filtered_positions)

# Plot results
plt.plot(gps_measurements[:, 0], gps_measurements[:, 1], 'ro-', label='Noisy GPS')
plt.plot(filtered_positions[:, 0], filtered_positions[:, 1], 'bo-', label='KF Smoothed (IMU)')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.title('Kalman Filter GPS Smoothing with IMU Acceleration')
plt.grid()
plt.show()
