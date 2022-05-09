% Simulation d'une loi de Poisson
% par une methode de Hastings Metropolis
% Cette methode converge quelque soit la valeur de lambda mais elle
% est particulierement bien adaptee dans le cas ou lambda est grand

clear; clf;

lambda = 1000;

n = ceil(log(sqrt(lambda))/log(2));
% le deplacement est code sur n bits + un bit de signe

pond = zeros(1,n); pond(1) = 1; 
for i=2:n, pond(i) = 2*pond(i-1); end; 

NHM = 500;  % nombre d'iterations de Hastings Metropolis

% initialisation de l'algorithme de Hastings Metropolis
x = lambda/3;
x_ = x;

for i=1:NHM,
  i
  bits = rand(1,n+1)<0.5;
  z =  (2*bits(1)-1)*sum(bits(2:n+1).*pond);
  xnew = x+z;

  ratio = exp(z*log(lambda)+0.5*log(x/xnew)+z*(1-log(x))-(x+z)*log(1+z/x));

 if (rand(1) < ratio), x = xnew; end;
 x_ = [x_ x];
end;


% expression analytique de la densite de probabilite

range = [max(0,round(lambda-5*sqrt(lambda))):1:round(lambda+5*sqrt(lambda))];
p = exp(-lambda+range*log(lambda)-log(sqrt(2*pi*range))-range.*(log(range)-ones(size(range))));
figure(1);
plot3([1:NHM],x_,zeros(1,NHM));
hold on;grid;
plot3(NHM*ones(size(range)),range,p);
axis([1 NHM 0 max(max(range),max(x_)) 0 max(p)*1.1]);

H = xlabel('it. #'); set(H,'FontSize',15);
H = ylabel('sampler'); set(H,'FontSize',15);
H = zlabel('Objective distribution'); set(H,'FontSize',15);

H = title('Hastings Metropolis algorithm'); set(H,'FontSize',18);
