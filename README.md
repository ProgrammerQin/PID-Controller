# PID-Controller

An OOP based application which implements PID control loop with Parallel Programming philosoph
Each object (input, PID control and output) is responsible for their tasks independently

The input object is responsible for generating input to the system. It simply provides an array of numbers to be supplied as input.
The control object is responsible for using input from the input object and the output object in the form of feedback to provide the control signal

The output object is responsible for displaying the output in the form of an array of numbers that result for a given input.
The feedback from the output into the control is simply the value of the current output for each input sample
The control object calculates the proportional, derivative, and integral term value which are then summed and provided to the output

Each object does all processing on separate threads.

