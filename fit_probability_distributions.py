from plotnine import *
from scipy.stats import gamma, rayleigh, uniform, norm, logistic
from scipy.stats import weibull_min, cauchy, lognorm, kstest, probplot
import numpy as np
import pandas as pd
from fitter import Fitter

#f = Fitter(gamma.rvs(2, loc=1.5, scale=2, size=320), distributions=['gamma', 'rayleigh', 'uniform',"norm"
#                                ,"logistic","weibull_min","cauchy","lognorm"])
#f.fit()
#f.summary()

#f.fitted_param['rayleigh']

def fit_gamma(dados):
    f = Fitter(dados, distributions=['gamma'])
    f.fit()
    global est1
    est1=f.fitted_param['gamma']
    return((ggplot(pd.DataFrame({"x":dados}),aes("x"))+geom_histogram(aes(y ="..density.."),
    fill="#00AFBB",color="black")+
    stat_function(fun = gamma.pdf, args=dict(a=est1[0], loc=est1[1], 
                                             scale=est1[2]),size=1.2)+
    theme_minimal()+labs(title="Distribuição Gama")))
    
def fit_rayleigh(dados):
    f = Fitter(dados, distributions=['rayleigh'])
    f.fit()
    global est2
    est2=f.fitted_param['rayleigh']
    return((ggplot(pd.DataFrame({"x":dados}),aes("x"))+geom_histogram(aes(y ="..density.."),
    fill="#00AFBB",color="black")+
    stat_function(fun = rayleigh.pdf, args=dict(loc=est2[0], scale=est2[1]),size=1.2)+
    theme_minimal()+labs(title="Distribuição Rayleigh")))    

def fit_uniform(dados):
    f = Fitter(dados, distributions=['uniform'])
    f.fit()
    global est3
    est3=f.fitted_param['uniform']
    return((ggplot(pd.DataFrame({"x":dados}),aes("x"))+geom_histogram(aes(y ="..density.."),
    fill="#00AFBB",color="black")+
    stat_function(fun = uniform.pdf, args=dict(loc=est3[0], scale=est3[1]),size=1.2)+
    theme_minimal()+labs(title="Distribuição Uniforme")))
    
def fit_norm(dados):
    f = Fitter(dados, distributions=['norm'])
    f.fit()
    global est4
    est4=f.fitted_param['norm']
    return((ggplot(pd.DataFrame({"x":dados}),aes("x"))+geom_histogram(aes(y ="..density.."),
    fill="#00AFBB",color="black")+
    stat_function(fun = norm.pdf, args=dict(loc=est4[0], scale=est4[1]),size=1.2)+
    theme_minimal()+labs(title="Distribuição Normal")))

def fit_logistic(dados):
    f = Fitter(dados, distributions=['logistic'])
    f.fit()
    global est5
    est5=f.fitted_param['logistic']
    return((ggplot(pd.DataFrame({"x":dados}),aes("x"))+geom_histogram(aes(y ="..density.."),
    fill="#00AFBB",color="black")+
    stat_function(fun = logistic.pdf, args=dict(loc=est5[0], scale=est5[1]),size=1.2)+
    theme_minimal()+labs(title="Distribuição Logística")))

def fit_weibull(dados):
    f = Fitter(dados, distributions=['weibull_min'])
    f.fit()
    global est6
    est6=f.fitted_param['weibull_min']
    return((ggplot(pd.DataFrame({"x":dados}),aes("x"))+geom_histogram(aes(y ="..density.."),
    fill="#00AFBB",color="black")+
    stat_function(fun = weibull_min.pdf, args=dict(c=est6[0], loc=est6[1],scale=est6[2])
    ,size=1.2) + theme_minimal()+labs(title="Distribuição Weibull"))) 

def fit_cauchy(dados):
    f = Fitter(dados, distributions=['cauchy'])
    f.fit()
    global est7
    est7=f.fitted_param['cauchy']
    return((ggplot(pd.DataFrame({"x":dados}),aes("x"))+geom_histogram(aes(y ="..density.."),
    fill="#00AFBB",color="black")+
    stat_function(fun = cauchy.pdf, args=dict(loc=est7[0],scale=est7[1])
    ,size=1.2) + theme_minimal()+labs(title="Distribuição Cauchy")))

def fit_lnorm(dados):
    f = Fitter(dados, distributions=['lognorm'])
    f.fit()
    global est8
    est8=f.fitted_param['lognorm']
    return(ggplot(pd.DataFrame({"x":dados}),aes("x"))+geom_histogram(aes(y ="..density.."),
    fill="#00AFBB",color="black")+
    stat_function(fun = lognorm.pdf, args=dict(s=est8[0], loc=est8[1],scale=est8[2])
    ,size=1.2) + theme_minimal()+labs(title="Distribuição Log-Normal")) 
        
def qq_gamma(dados):
    qq=probplot(dados,dist=gamma,sparams=est1)
    return((ggplot(pd.DataFrame({"teorico":qq[0][0],"amostra":qq[0][1]}))
        +geom_point(aes("teorico","amostra"))+ theme_minimal()+
        labs(title="Distribuição Gama")+
        geom_abline(intercept=qq[1][1] , slope= qq[1][0])))

def qq_rayleigh(dados):
    qq=probplot(dados,dist=rayleigh,sparams=est2)
    return((ggplot(pd.DataFrame({"teorico":qq[0][0],"amostra":qq[0][1]}))
        +geom_point(aes("teorico","amostra"))+ theme_minimal()+
        labs(title="Distribuição Rayleigh")+
        geom_abline(intercept=qq[1][1] , slope= qq[1][0])))

def qq_uniform(dados):
    qq=probplot(dados,dist=uniform,sparams=est3)
    return((ggplot(pd.DataFrame({"teorico":qq[0][0],"amostra":qq[0][1]}))
        +geom_point(aes("teorico","amostra"))+ theme_minimal()+
        labs(title="Distribuição Uniforme")+
        geom_abline(intercept=qq[1][1] , slope= qq[1][0])))

def qq_norm(dados):
    qq=probplot(dados,dist=norm,sparams=est4)
    return((ggplot(pd.DataFrame({"teorico":qq[0][0],"amostra":qq[0][1]}))
        +geom_point(aes("teorico","amostra"))+ theme_minimal()+
        labs(title="Distribuição Normal")+
        geom_abline(intercept=qq[1][1] , slope= qq[1][0])))

def qq_logistic(dados):
    qq=probplot(dados,dist=logistic,sparams=est5)
    return((ggplot(pd.DataFrame({"teorico":qq[0][0],"amostra":qq[0][1]}))
        +geom_point(aes("teorico","amostra"))+ theme_minimal()+
        labs(title="Distribuição Logística")+
        geom_abline(intercept=qq[1][1] , slope= qq[1][0])))

def qq_weibull(dados):
    qq=probplot(dados,dist=weibull_min,sparams=est6)
    return((ggplot(pd.DataFrame({"teorico":qq[0][0],"amostra":qq[0][1]}))
        +geom_point(aes("teorico","amostra"))+ theme_minimal()+
        labs(title="Distribuição Weibull")+
        geom_abline(intercept=qq[1][1] , slope= qq[1][0])))

def qq_cauchy(dados):
    qq=probplot(dados,dist=cauchy,sparams=est7)
    return((ggplot(pd.DataFrame({"teorico":qq[0][0],"amostra":qq[0][1]}))
        +geom_point(aes("teorico","amostra"))+ theme_minimal()+
        labs(title="Distribuição Cauchy")+
        geom_abline(intercept=qq[1][1] , slope= qq[1][0])))

def qq_lnorm(dados):
    qq=probplot(dados,dist=lognorm,sparams=est8)
    return((ggplot(pd.DataFrame({"teorico":qq[0][0],"amostra":qq[0][1]}))
        +geom_point(aes("teorico","amostra"))+ theme_minimal()+
        labs(title="Distribuição Log-Normal")+
        geom_abline(intercept=qq[1][1] , slope= qq[1][0])))          
    
x = gamma.rvs(2, loc=1.5, scale=2, size=320)
  
fit_gamma(x) 
fit_rayleigh(x)  
fit_uniform(x) 
fit_norm(x) 
fit_logistic(x)    
fit_weibull(x) 
fit_cauchy(x)    
fit_lnorm(x)

qq_gamma(x) 
qq_rayleigh(x)  
qq_uniform(x) 
qq_norm(x) 
qq_logistic(x)    
qq_weibull(x) 
qq_cauchy(x)    
qq_lnorm(x)

pd.DataFrame({"valor_p":np.round(np.array([kstest(x,"gamma",args=est1)[1]
                    ,kstest(x,"rayleigh",args=est2)[1]
                    ,kstest(x,"uniform",args=est3)[1]
                    ,kstest(x,"norm",args=est4)[1]
                    ,kstest(x,"logistic",args=est5)[1]
                    ,kstest(x,"weibull_min",args=est6)[1]
                    ,kstest(x,"cauchy",args=est7)[1]
                    ,kstest(x,"lognorm",args=est8)[1]]),3)},
    index=np.array(["Gama","Rayleigh","Uniforme","Normal","Logistica"
                        ,"Weibull","Cauchy","Lognormal"]))
    