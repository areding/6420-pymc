#COIN
p = seq(0,1,0.01)
P10T = function(p) {11 * (1-p)^10} 
#  11 to normalize to a density
plot(p, P10T(p),"l")
# 
integrate(P10T, lower=0, upper=1)
#
# for the mean
pP10T = function(p)  11 * p * (1-p)^10 
integrate(pP10T, lower=0, upper=1) #0.08333333 (1/12)
points(c(0, 0),c(0, 11), pch=16, col="red")
points(c(1/12, 1/12),c(0,  P10T(1/12)),pch=16,col="green")
# for the median
integrate(P10T, lower=0, upper=0.061069081)  #0.50000
points(c(0.061069081, 0.061069081),
     c(0,  P10T(0.061069081)), pch=16, col="blue")
legend(0.6,10, #location
      c("Mode","Mean","Median"), #labels
      cex= 1, #size 
      pch=c(16,16,16), #filled circle
      col=c("red","green","blue")) #color
    
 

