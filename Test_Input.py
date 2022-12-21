class Input:
  def __init__(self, process_variable):
    self.measured_process_variable = process_variable


process_variable_pool = [30]
measured_variable_pool = [0]

input = Input(process_variable_pool[0])
measured_variable_pool.insert(0, input.measured_process_variable)
del measured_variable_pool[-1]
print(measured_variable_pool)