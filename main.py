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

  def control(self):
    controller_output = self.set_point + 2
    return controller_output


class Output:
  def __init__(self, controller_output, disturbance):
    self.process_variable = controller_output + disturbance


measured_process_variable = 0
Input = Input(measured_process_variable)

set_point = 5
Controller = Controller(Input.measured_process_variable, set_point, 5, 1, 1)

disturbance = 100
Output = Output(Controller.control(), disturbance)

print(Output.process_variable)

