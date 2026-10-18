
n <-100
set.seed(2)
y <- 2 * rnorm(100) + 1 
#------------------------------------------
NN <- 10000 
mus <- c()  
taus <- c()
sumdata <- sum(y)
#hyperparameters
mu0 <- 0.5
tau0 <- 1/100 
a <- 1/2 
b <-  2 
# start, initial values
mu <- 0.5
tau <- 0.5 
for (i in 1 : NN){
   newmu <- rnorm(1, (tau * sumdata+tau0*mu0)/(tau0+n*tau),
                  sqrt(1/(tau0+n*tau)) ) 
      
   rat  <- b + 1/2 * sum ( (y - newmu)^2) 
   newtau <- rgamma(1,shape=a + n/2,
                    rate=rat)   
   mus <-  c(mus, newmu)
   taus <- c(taus, newtau)
   mu <- newmu 
   tau<- newtau 
}

burn <- 200 
mus <- mus[burn:NN] 
taus <- taus[burn:NN] 

mean(mus)
mean(taus)

par(mfrow=c(1,2))
hist(mus, 40)
hist(taus, 40)
 
