# Introdução

## O que é Visão Computacional?

**Visão Computacional** é um campo dentro de Inteligência Artificial, no qual estamos interessados em realizar tarefas complexas a partir de **imagens**. Antes de explicarmos em detalhes sobre como as imagens funcionam, vamos falar sobre algumas das suas principais utilizações.
Tais tarefas podem ser:

1. **Reconhecimento facial**, que pode localizar na imagem onde está um rosto humano.
2. **Classificação de imagens**, como predizer se uma imagem contém um cachorro ou gato, por exemplo.
3. **Segmentação de imagens**, por exemplo, que pode separar em uma imagem de tomografia a localização do pulmão e do que não é pulmão.
4. **Detecção de Veículos**, como detectar carros que cometeram infrações no trânsito.

## Reconhecimento facial
Um **sistema de reconhecimento facial** é uma técnica de visão computacional que tem como objetivo reconhecer e localizar o padrão característico facial em uma imagem utilizando algum algoritmo.

![1](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/reconhecimento_facial.png)

## Classificação de imagens
Técnica de aprendizagem de máquina onde estamos interessados em classificar se determinada classe utilizando imagens.

![2](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/classificacao.jpg)

## Segmentação de imagens
**Segmentação** é o processo de dividir uma imagem em regiões, com o objetivo de simplificar e/ou mudar a representação de uma imagem para facilitar a sua análise.

![3](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/segmentacao.jpg)

## Detecção de imagens
**Detecção de imagens** é o procedimento onde detectamos e localizamos determinado objeto em uma imagem.

![4](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/deteccao.png)

### Observação
Muitas pessoas se confundem detecção e classificação, pois os resultados finais são parecidos. Porém, na tarefa de classificação apenas é dada uma **classe** para a imagem, enquanto que em detecção o objeto é **localizado** na imagem.

![5](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/diff_deteccao_classificacao.jpg)

## Fundamentos de imagens
A forma mais simples de uma **imagem** é basicamente uma matriz, com um número de linhas e número de colunas que definem o tamanho da imagem. Cada elemento da matriz é chamada de **pixel**, que possui uma “cor”.

Na sua forma mais básica, a cor de um pixel pode ser representado por 1 bit. O bit com o valor 1 indica que o pixel representa a cor “branco”. O bit com o valor 0 indica que o pixel representa a cor “preto”. **Imagens binárias** são aquelas em que cada pixel é branco ou preto.
Por exemplo, a matriz:

![a](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/matrixex.png)

representa a seguinte imagem:

![a](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/imgbinaria1.png)

Outro exemplo seria o logo da USP:

![b](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/usplogo2.png)

Em geral, os níveis, 0 e 1 são **insuficientes** para representarmos o que costumamos chamar de imagens em preto e branco, pois em geral as imagens possuem **vários** níveis de cinza. Uma forma tradicional de representar uma imagem com vários tons de cinza é reservando um byte para cada pixel. Um byte consiste de 8 bits representando um valor entre 0 e 255. Portanto, temos muitos mais possibilidades de representar nossa imagem adequadamente.

![7](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/cinza1.png)

![8](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/cinza2.png)

Com um byte por pixel podemos representar imagens com até **256 níveis de cinza**. Chamamos as imagens em que cada pixel pode ter vários tons de cinza de imagens com **níveis de cinza** (grayscale).

![9](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/cinza3.jpg)

Que representa a seguinte matriz:

![1](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/cinza3_array.png)

Uma imagem com níveis de cinza nos permite ver as variações de luminosidade da cena. Já uma **imagem colorida** requer ainda mais informação para cada pixel. Baseado no sentido da visão humana, que é **tricromática**, a representação de imagens mais comum é obtida decompondo uma cor nas componentes básicas **vermelho** (red), **verde** (green), e **azul** (blue) ou **RGB**. Assim, usando um total de três bytes: um byte para níveis de vermelho; um byte para níveis de verde e um byte para níveis de azul, podemos representar aproximadamente todas as cores.

![10](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/imgcolorida.jpg)

Os canais de cores de uma imagem colorida são representados por três matrizes. Nesse exemplo, as matrizes são:

![1](https://github.com/turing-usp/Visao-Computacional/blob/intro/images/imgcolorida_array.png)

## Veja os conceitos matriciais apresentados neste [notebook em python](https://github.com/turing-usp/Visao-Computacional/blob/intro/Introdu%C3%A7%C3%A3o/Introdu%C3%A7%C3%A3o.ipynb)

### Links introdutórios:
 
1. [Turing Talks - Introdução à Visão Computacional](https://medium.com/turing-talks/introdu%C3%A7%C3%A3o-%C3%A0-vis%C3%A3o-computacional-b13698774adc)  
2. [Processamento de imagens](https://www.youtube.com/playlist?list=PL5TJqBvpXQv54i_HWjd7s70vbP4Is7sK_)    
3. [Documentação da biblioteca OpenCV](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)    





