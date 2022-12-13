class Input:
  def __init__(self, measured_process_variable):
    self.measured_process_variable = measured_process_variable


class Controller:
  def __init__(self, measured_process_variable, set_point, proportional_gain, integral_gain, derivative_gain):
    self.measured_process_variable = measured_process_variable
    self.set_point = set_point
    self.P_gain = proportional_gain
    self. I_gain = integral_gain
    self. D_gain = derivative_gain
    self. difference = measured_process_variable - set_point

  def control(self):
    controller_output = self.difference + 2 * self.D_gain
    return controller_output


class Process:
  def __init__(self, controller_output, disturbance):
    self.process_variable = controller_output + disturbance


measured_process_variable = 0
Input = Input(measured_process_variable)


measured_process_variable = 10
set_point = 5
proportional_gain = 30
integral_gain = 40
derivative_gain = 32
Controller = Controller(measured_process_variable, set_point, proportional_gain, integral_gain, derivative_gain)

controller_output = Controller.control()


controller_output = 30
disturbance = 0
disturbance_array = [109, 23, 32, 43, 54]
Process = Process(controller_output, disturbance)
process_variable = Process.process_variable



for n in disturbance_array:
  disturbance = n
  measured_process_variable = process_variable
  print(disturbance, measured_process_variable, set_point, controller_output, process_variable)

