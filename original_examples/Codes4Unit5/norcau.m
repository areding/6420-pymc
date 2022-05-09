%norcau
%
x=2;
N=100000;
num = 0; denom = 0;
%
for i=1:N
theta = x + randn;  %theta ~ N(x,1)
num = num + theta/(1+theta^2);
denom = denom + 1/(1+theta^2);
end
delta21 = num/denom

%%

x=2;
N=100000;
num = 0; denom = 0;
%
for i=1:N
a=randn(2,1);
theta = a(1)/a(2);  %theta ~ Ca(0,1)
num = num + theta * exp(-1/2 *(x-theta)^2);
denom = denom + exp(-1/2 *(x-theta)^2);
end
delta22 = num/denom
