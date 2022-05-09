% Example 3
close all
clear all
 
 %pkg load statistics  %needed for 'randsample'


% The 112 data points represent the numbers of coal-mining 
% disasters involving 10 or more men killed per year between 
% 1851 and 1962. 
%  
% Based on the observation that the there was a significant 
% decrease around 1900, it is suitable to apply a change-point 
% model to divide the whole dataset into two periods; each period 
% with its own distribution of number of disasters.
%  
% The data set was compiled by
% Maguire, Pearson and Wynn in 1952 and 
% updated by Jarrett (1978). This data have been used by a 
% number of authors to illustrate various techniques that can 
% be applied to point processes
% 
% 
% Maguire, B. A., Pearson, E. S. and Wynn, A. H. A. (1952). The time intervals between industrial accidents. Biometrika, 39, 168–180.
% 
%  Jarrett, R.G. (1979). A note on the intervals between coal-mining disasters. Biometrika, 66, 191-193. 
% 
%  Carlin, Gelfand, and Smith (1992) Heirarchical Bayesian Analysis of Changepoint Problems. Applied Statistics, 41, 389-405.


% x is the number of coal mine disasters per year
x =[ 4     5     4     1     0     4     3     4     0     6     3     3     4     0     2     6     3     3     5     4     5     3 ...
     1     4     4     1     5     5     3     4     2     5     2     2     3     4     2     1     3     2     2     1     1     1 ...
     1     3     0     0     1     0     1     1     0     0     3     1     0     3     2     2     0     1     1     1     0     1 ...
     0     1     0     0     0     2     1     0     0     0     1     1     0     2     3     3     1     1     2     1     1     1 ...
     1     2     4     2     0     0     0     1     4     0     0     0     1     0     0     0     0     0     1     0     0     1 ...
     0     1];
 
% year corresponding to x
year = [1851        1852        1853        1854        1855        1856        1857        1858        1859        1860        1861 ...
        1862        1863        1864        1865        1866        1867        1868        1869        1870        1871        1872 ...
        1873        1874        1875        1876        1877        1878        1879        1880        1881        1882        1883 ...
        1884        1885        1886        1887        1888        1889        1890        1891        1892        1893        1894  ...
        1895        1896        1897        1898        1899        1900        1901        1902        1903        1904        1905 ...
        1906        1907        1908        1909        1910        1911        1912        1913        1914        1915        1916 ...
        1917        1918        1919        1920        1921        1922        1923        1924        1925        1926        1927 ...
        1928        1929        1930        1931        1932        1933        1934        1935        1936        1937        1938 ...
        1939        1940        1941        1942        1943        1944        1945        1946        1947        1948        1949 ...
        1950        1951        1952        1953        1954        1955        1956        1957        1958        1959        1960 ...
        1961        1962];
% y contains number of disasters.
% year contains the year.
n = length(x);
NN = 10500;						%total number in chain
burn = 500;           %burn
  lambda = zeros(1,NN);
  mu = zeros(1,NN);
  m = zeros(1,NN);
% Get starting points.
m(1) = 10;
% Note that m will indicate an index to the year
% that corresponds to a hypothesized change-point.
lambda(1) = 4; %initial lambda
mu(1) = 1/2;  %initial mu
% Set the hyperparameters
alpha = 4; %hyperparameter
beta = 1; %hyperparameter
gamma = 1/2; %hyperparameter
delta = 1; %hyperparameter
% Start the Gibbs Sampler.
tic
for i = 2:NN
   mm = m(i-1);  
   % Get parameters for generating lambda
   alpha1 = alpha + sum(x(1:mm));
   beta1 = mm + beta;
   % Generate the variate for lambda.
   lambda(i) = gamrnd(alpha1,1/beta1,1,1);
   % Get parameters for generating mu.
   gamma1 = gamma + sum(x) - sum(x(1:mm));
   delta1 = n-mm+delta;
   % Generate the variate for mu.
   mu(i) = gamrnd(gamma1,1/delta1,1,1);
    % Now get the probabilities for m.
   for j = 1:n
      posteriorm(j) = exp((mu(i)-lambda(i))*j)*(lambda(i)/mu(i))^sum(x(1:j));
   end
   m(i) = randsample(n,1,true,posteriorm);
end
toc
figure(1)
hist(m(burn+1:NN)+1850, n)
figure(2)
subplot(121)
hist(lambda(burn+1:NN), 40)
xlabel('\lambda')
subplot(122)
hist(mu(burn+1:NN), 40)
xlabel('\mu')