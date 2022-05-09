% Generation d'une variable aleatoire de Poisson
% function X = poisson(lambda)

function X = poisson(lambda);

T = -1/lambda*log(rand(1));
X = 1;

while (T<1),
      T = T-1/lambda*log(rand(1));
      X = X+1;
end;

X = X-1;


