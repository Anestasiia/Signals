import function
from coefficients import coefficients
from harmonic import harmonic, spectrum
from approximation import approximation, print_approximation
import constants as const
import deviation as dev
import file
import plots as plot

b_k = coefficients()

harmonic(b_k)
spectrum(b_k)

x, y = approximation(b_k, const.N)

plot.plots(x, function.function(x), y)

delta = dev.deviation(x, y)

file.write_to_file(const.N, b_k, delta)
