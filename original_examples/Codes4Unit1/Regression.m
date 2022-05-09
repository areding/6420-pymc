%if OCTAVE is used
%pkg load statistics
x = [1 2 3 4 5];
y = [1 3 3 3 5];
xx=[ones(5,1) x'];
b = regress(y', xx)
