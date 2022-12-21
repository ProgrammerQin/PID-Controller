import matplotlib.pyplot as plt
from numpy import diff
import scipy.integrate as integrate


class Input:
  def __init__(self, process_variable):
    self.measured_process_variable = process_variable


class PID_Controller:
  def __init__(self, measured_process_variable, set_point, Kp, Ki, Kd):
    self.measured_process_variable = measured_process_variable
    self.C = 1
    self.set_point = set_point
    self.difference = measured_process_variable - set_point
    self.P_gain = Kp
    self.I_gain = Ki
    self.D_gain = Kd
    self.dt = 10
    self.P = self.P_gain * self.difference
    self.I = self. I_gain * self.difference / 2 * self.dt
    self.D = self. D_gain * self.difference / self.dt

  def control(self):
    controller_output = self.P + self.I * + self.D
    return controller_output


class Output_Process:
  def __init__(self, controller_output, disturbance):
    self.process_variable = controller_output + disturbance


process_variable_pool = [0]
measured_variable_pool = [0]
controller_output = [0]
disturbance = [0]

input = Input(process_variable_pool[0])
measured_variable_pool.insert(0, input.measured_process_variable)
del measured_variable_pool[-1]


output = Output_Process(controller_output[0], disturbance[0])
process_variable_pool.insert(0, output.process_variable)
del process_variable_pool[-1]


for n in range(10):
    measured_process_variable = process_variable_pool[0]
#   Input = Input(measured_process_variable)
    set_point = 5
    Kp = 30
    Ki = 40
    Kd = 32
    Controller = PID_Controller(measured_process_variable, set_point, Kp, Ki, Kd)
    controller_output = [0, Controller.control()]
    disturbance_array = [109, 23, 32, 43, 54, 213, 12, 213, 2, 34]
    Process = Output_Process(controller_output[-1], disturbance_array[n])
    process_variable = Process.process_variable
    process_variable_pool.append(process_variable)


#   Visualize PID Control Process
plt_1 = controller_output
plt_2 = process_variable_pool
plt.figure(figsize=(16, 8))
plt.title('PID')
plt.xlabel('Time')
plt.ylabel('Measured Process Value')
plt.plot(plt_1)
plt.plot(plt_2)
plt.show()

