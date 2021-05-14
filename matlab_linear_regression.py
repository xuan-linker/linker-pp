from matplotlib.pyplot import figure, plot
from numpy import linspace, sin, cos, pi

x = linspace(-2*pi,2*pi);
y1 = sin(x);
y2 = cos(x);

figure
plot(x,y1,x,y2)