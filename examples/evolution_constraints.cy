# Evolution Constraints Example
# Temperature controller with safety limits
A(temperature)
G(temperature;value:20;unit:celsius)
# Set evolution boundaries
F(temperature;min:15;max:30;auto_evolve:true;adapt_rate:0.1)

# Pressure monitor with discrete states
A(pressure)
G(pressure;value:normal)
# Only allowed states
F(pressure;allowed:[normal,high,critical];forbidden:[unsafe];auto_evolve:true)

L(system;life)
