class Output_Process:
  def __init__(self, controller_output, disturbance):
    self.process_variable = controller_output + disturbance


process_variable_pool = [30]
controller_output = [23, 43, 32, 23]
disturbance = [22, 435, 3545, 234, 234]

output = Output_Process(controller_output[0], disturbance[0])
process_variable_pool.insert(0, output.process_variable)
del process_variable_pool[-1]
print(process_variable_pool)