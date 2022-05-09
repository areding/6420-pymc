clear; clf;

r = 3;  % 3 liens monodirectionnels
c = 5;  % 5 paires Origine/Destination

% c=12; r=7; % 12 paires OD, 7 liens monodirectionnels

%%%%%%%%%%%%%%%%%%%
% le routage est specifie par la matrice A
%%%%%%%%%%%%%%%%%%%

A = [1 0 0 1 1;0 1 0 1 0;0 0 1 0 1];
% y1 = x1+x4+x5
% y2 = x2+x4
% y3 = x3+x5

% A = [1 0 0 0 0 0 0 1 0 1 1 1;0 1 0 0 0 0 0 0 1 1 0 1;0 0 1 0 0 0 0 1 0 0 1 1;0 0 0 1 0 0 0 1 1 0 0 0;0 0 0 0 1 0 0 1 0 1 0 0;0 0 0 0 0 1 0 0 0 1 0 0;0 0 0 0 0 0 1 0 1 0 0 0;]

A1 = A(:,1:r);  % A1 est inversible
A2 = A(:,r+1:c);

invA1 = inv(A1);


%%%%%%%%%%%%%%%%%%%%%%%%
%
% Ici, on simule les paires Origine/Destination
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%

lambda = [8 20 60 38 3]'; % valeurs moyennes des 5 paires Origine/Destination
% lambda = [12 20 5 32 70 55 10 29 15 2 50 15];

xvrai = zeros(c,1);
for i=1:c, xvrai(i) = poisson(lambda(i)); end;

y = A*xvrai;

xvrai

y


%%%%%%%%%%%%%%%
%
% Hastings Metropolis within Gibbs algorithm
%
%%%%%%%%%%%%%%%%%%


NGibbs = 100;  % nombre de passages de l'algorithme de Gibbs
NHM = 10;     % nombre de passages de l'algorithme de Hastings Metropolis

% initialisation de l'algorithme de Gibbs
%-------------------------

x1 = zeros(r,1); x2 = zeros(c-r,1);
while (min(x1)<1),
  for j=1:c-r, 
     x2(j) = poisson(mean(lambda)); % ici, toutes les composantes 
                                    % sont initialisees de la meme facon
  end;
  x1 = invA1*(y-A2*x2);  % x1 est tel que y=Ax 
end;    % end while


% fin de l'initialisation


% Initialisation du denominateur dans le ratio de Hastings Metropolis
%----------------------
DEN = 1;
for i=1:r,
  DEN = DEN*(lambda(i))^x1(i)/gamma(x1(i)+1);
end;

x_ = [];

%%%%%%%%%%%%%%%%%%%%%%%%
% NGibbs passages de l'algorithme de Gibbs
% A chaque passage on reactualise tous les sites x2(j) conditionnellement
% à x2(-j) et a y
%%%%%%%%%%%%%%%%%%%%

for iG=1:NGibbs,
  iG
  for j=1:c-r,
    % on reactualise le site x2(j)
    % NHM iterations de l'algorithme de Hastings Metropolis sont requises
     for iHM = 1:NHM,
         candidat = poisson(lambda(r+j));
         x2new = x2; x2new(j) = candidat;
         x1 = invA1*(y-A2*x2new);
         if (min(x1)>-1),
	   NUM = 1; for k=1:r, NUM = NUM*(lambda(k))^x1(k)/gamma(x1(k)+1); end;
           ratio = NUM/DEN;
           if (rand(1)<ratio) x2 = x2new; DEN = NUM; end;
         end; % end if (min(x1)>-1)
     end;  % end for iHM (fin de l'algo de Hastings Metropolis)
  end;  % end for j=1:c-r (on a balaye toutes les coordonnees de x2)
x_ = [x_ [x1;x2]];
end; % end for iG (fin de l'algo de Gibbs)


for i=1:c,
subplot(c,1,i), plot(x_(i,:)); 
H = xlabel('it. # de Gibbs');
H = ylabel('paire OD');
hold on;
plot([1:NGibbs],xvrai(i)*ones(1,NGibbs),'--');
end;



