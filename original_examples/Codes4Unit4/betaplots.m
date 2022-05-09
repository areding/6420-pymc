   
clear all
close all

disp('BETA PLOTS FOR BAYES')
  lw = 2; 
  set(0, 'DefaultAxesFontSize', 16);
  fs = 15;
  msize = 10;
% end of preabmle--------------------------------------

  figure(1)
xx = 0:0.0001:1;
subplot(3,3,1)
  yy1 = betapdf(xx, 1/2, 1/2);
  plot(xx, yy1, 'linewidth',lw)
  text(0.25, 4, '0.5, 0.5')
  axis([0 1 0 5])
subplot(3,3,2)
  yy1 = betapdf(xx, 1, 1);
  plot(xx, yy1, 'linewidth',lw)
   text(0.25, 0.9, '1, 1')
  axis([0 1 0 1.1])
subplot(3,3,3)
  yy1 = betapdf(xx, 2, 2);
  plot(xx, yy1, 'linewidth',lw)
    text(0.35, 1.1, '2, 2')
  axis([0 1 0 1.7])
subplot(3,3,4)
  yy1 = betapdf(xx, 10, 10);
  plot(xx, yy1, 'linewidth',lw)  
  text(0.05, 3.1, '10, 10')
subplot(3,3,5)
  yy1 = betapdf(xx, 1, 5);
  plot(xx, yy1, 'linewidth',lw)
  text(0.15, 4.1, '1, 5')
  axis([0 1 0 5.5])
subplot(3,3,6)
  yy1 = betapdf(xx, 1, 0.4);
  plot(xx, yy1, 'linewidth',lw)
  text(0.05, 4.1, '1, 0.4')
  axis([0 1 0 5.5])
subplot(3,3,7)
  yy1 = betapdf(xx, 3, 5);
  plot(xx, yy1, 'linewidth',lw)
  text(0.6, 2, '3, 5')
  axis([0 1 0 2.7])
subplot(3,3,8)
  yy1 = betapdf(xx, 50, 30);
  plot(xx, yy1, 'linewidth',lw)
  text(0.05, 6.1, '50, 30')
  axis([0 1 0 8])
subplot(3,3,9)
  yy1 = betapdf(xx, 5000, 3000);
  plot(xx, yy1, 'linewidth',lw)
  text(0.05, 50, '5000, 3000')
  axis([0 1 0 70])
 %print -depsc 'C:\Brani\Courses\bmestatu\BMESBOOK\RVar\betapdfs.eps'
%%
  figure(2)
   yycoin = betapdf(xx, 500, 500);
  plot(xx, yycoin, 'linewidth',lw)
  text(0.1, 25, '500, 500')
  axis([0 1 0  28])
