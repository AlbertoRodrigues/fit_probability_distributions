require(ggplot2)
require(fitdistrplus)
require(gridExtra)
require(VGAM)


ajuste=function(dados,opcao)
{
  dist1=fitdist(dados,"gamma");est1<<- dist1$estimate
  dist2=fitdist(dados,"lnorm");est2<<- dist2$estimate
  dist3=fitdist(dados,"weibull");est3<<- dist3$estimate
  dist4=fitdist(dados,"logis");est4<<- dist4$estimate
  dist5=fitdist(dados,"norm");est5<<- dist5$estimate
  dist6=fitdist(dados,"cauchy");est6<<- dist6$estimate
  dist7=fitdist(dados,"unif");est7<<- dist7$estimate
  
  if(opcao==1)
  {
    a=(ggplot(data.frame(x=dados),aes(x))+geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")+
         stat_function(fun = dgamma, args = list( est1[1], est1[2]),aes(fill="black"),size=1.2)
       +labs(title="Distribuição Gama")+theme_minimal())
    
    
    b=(ggplot(data.frame(x=dados),aes(x))+geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")
       +stat_function(fun = dweibull, args = list( est3[1], est3[2]),aes(fill="black"),size=1.2)
       +labs(title="Distribuição Weibull")+theme_minimal()
    )
    c=(ggplot(data.frame(x=dados),aes(x))+geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")
       +stat_function(fun = dnorm, args = list( est5[1], est5[2]),aes(fill="black"),size=1.2)
       +labs(title="Distribuição Normal")+theme_minimal())
    
    d=(ggplot(data.frame(x=dados),aes(x))+geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")
       +stat_function(fun = dlogis, args = list( est4[1], est4[2]),aes(fill="black"),size=1.2)
       +labs(title="Distribuição Logística")+theme_minimal())
    grid.arrange(a,b,c,d,ncol=2)
  }else if(opcao==2)
  {
    e=(ggplot(data.frame(x=dados),aes(x))+geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")
       +stat_function(fun = dlnorm, args = list( est2[1], est2[2]),aes(fill="black"),size=1.2)
       +labs(title="Distribuição Lognormal")+theme_minimal())
    
    est_rayleigh <<- sqrt(sum(x^2)/(2*length(x)))
    f=(ggplot(data.frame(x=dados),aes(x))+geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")
       +stat_function(fun = drayleigh, args = list(sqrt(sum(dados^2)/(2*length(dados))) ),aes(fill="black"),size=1.2)
       +labs(title="Distribuição Rayleigh")+theme_minimal())
    
    g=(ggplot(data.frame(x=dados),aes(x))+geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")
       +stat_function(fun = dcauchy, args = list(est6[1],est6[2]),aes(fill="black"),size=1.2)
       +labs(title="Distribuição Cauchy")+theme_minimal())
    
    h=(ggplot(data.frame(x=dados),aes(x))+geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")
       +stat_function(fun = dunif, args = list(est7[1],est7[2]),aes(fill="black"),size=1.2)
       +labs(title="Distribuição Uniforme")+theme_minimal())
    grid.arrange(e,f,g,h,ncol=2)
  }else if(opcao==3)
  {
    a1=ggplot(data.frame(x=dados), aes(sample=x)) +
      stat_qq(distribution = qgamma, dparams = est1) +
      stat_qq_line(distribution = qgamma, dparams = est1)+theme_minimal()+
    labs(title="Distribuição Gama")
    
    a2=ggplot(data.frame(x=dados), aes(sample=x)) +
      stat_qq(distribution = qnorm, dparams = est5) +
      stat_qq_line(distribution = qnorm, dparams = est5)+theme_minimal()+
    labs(title="Distribuição Normal")
    
    a3=ggplot(data.frame(x=dados), aes(sample=x)) +
      stat_qq(distribution = qlnorm, dparams = est2) +
      stat_qq_line(distribution = qlnorm, dparams = est2)+theme_minimal()+
    labs(title="Distribuição Lognormal")
    
    a4=ggplot(data.frame(x=dados), aes(sample=x)) +
      stat_qq(distribution = qweibull, dparams = est3) +
      stat_qq_line(distribution = qweibull, dparams = est3) +theme_minimal()+
    labs(title="Distribuição Weibull")
    grid.arrange(a1,a2,a3,a4,ncol=2)
  }else if(opcao==5)
  {
    valor_p=data.frame(valor.p=c(ks.test(x,pgamma,est1[1],est1[2])$p.value,
                                 ks.test(x,plnorm,est2[1],est2[2])$p.value,
                                 ks.test(x,pweibull,est3[1],est3[2])$p.value,
                                 ks.test(x,plogis,est4[1],est4[2])$p.value,
                                 ks.test(x,pnorm,est5[1],est5[2])$p.value,
                                 ks.test(x,prayleigh,est_rayleigh)$p.value,
                                 ks.test(x,pcauchy,est6[1],est6[2])$p.value,
                                 ks.test(x,punif,est7[1],est7[2])$p.value))
    rownames(valor_p)=c("gamma","lnorm","weibull","logis","norm","rayleigh",
                        "cauchy","unif")
    
    round(valor_p,4)
  }else if(opcao==4)
  {
    b1=ggplot(data.frame(x=dados), aes(sample=x)) +
      stat_qq(distribution = qlogis, dparams = est4) +
      stat_qq_line(distribution = qlogis, dparams = est4)+theme_minimal()+
    labs(title="Distribuição Logística")
    
    est_rayleigh <<- sqrt(sum(x^2)/(2*length(x)))
    b2=ggplot(data.frame(x=dados), aes(sample=x)) +
      stat_qq(distribution = qrayleigh, dparams = est_rayleigh) +
      stat_qq_line(distribution = qrayleigh, dparams = est_rayleigh)+
     theme_minimal()+labs(title="Distribuição Rayleigh")
    
    b3=ggplot(data.frame(x=dados), aes(sample=x)) +
      stat_qq(distribution = qcauchy, dparams = est6) +
      stat_qq_line(distribution = qcauchy, dparams = est6)+theme_minimal()+
    labs(title="Distribuição Cauchy")
    
    b4=ggplot(data.frame(x=dados), aes(sample=x)) +
      stat_qq(distribution = qunif, dparams = est7) +
      stat_qq_line(distribution = qunif, dparams = est7)+theme_minimal()+
    labs(title="Distribuição Uniforme")
    grid.arrange(b1,b2,b3,b4,ncol=2)
  }
}

x=rgamma(350,2,2)
ajuste(x,1)
ajuste(x,2)
ajuste(x,3)
ajuste(x,4)
ajuste(x,5)

x=rnorm(1000,7,1)
ajuste(x,1)
ajuste(x,2)
ajuste(x,3)
ajuste(x,4)
ajuste(x,5)

x=rrayleigh(80,3)
ajuste(x,1)
ajuste(x,2)
ajuste(x,3)
ajuste(x,4)
ajuste(x,5)

x=rnorm(500,1.71,0.08)
dist5=fitdist(x,"norm")
est5= dist5$estimate
(ggplot(data.frame(x),aes(x))+geom_histogram(fill="#00AFBB",color="black")+
theme_test())

(ggplot(data.frame(x),aes(x))
  +geom_histogram(aes(y =..density..),fill="#00AFBB",color="black")
  +stat_function(fun = dnorm, args = list( est5[1], est5[2]),aes(fill="black"),size=1.2)
  +labs(title="Normal distribution")+theme_test())
