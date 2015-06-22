#Projeto PDS

Hélio de Meira Lins Neto


## Ferramentas

Todo o projeto foi feito usando ferramentas opensource. Seguem as ferramentas usadas:

* Python
* Pillow
* Numpy
* Scypy
* Matplotlib
* Tesseract-ocr
* Octave

##Parte 1

###Questão 1

Código: parte1/q1.py

Gráficos das letras **a)**, **b)** e **c)**. Todos feitos usando Numpy/Scipy.

![plot_y](parte1/y.png)

![plot_z](parte1/z.png)

![plot_w](parte1/w.png)

#### **d)**
A função z tem o dobro da frequência da função y. Assim, a transformada de fourier Z(f)=Y(f/2) e
seus picos são em pontos com o dobro da frequência dos de y.
A transformada da função w, obtida a partir da concatenação das anteriores, possui os picos de Z
e de Y. Note que, graficamente, não é possível inferir quando as frequências estão ativas.

#### **e)**

As bibliotecas Numpy e Scipy não tem uma função pronta do espectograma. Para evitar implementá-la,
usei o GNU Octave. Seguem os comandos:

    pkg load signal
    t = [0:0.01:9.99];
    w = [sin(20*pi*t) + cos(30*pi*t), sin(40*pi*t) + cos(60 * pi * t)];
    specgram(w, 256, 100, 500)

![spec](parte1/spec.png)

Agora vemos as componentes de frequência pelo tempo, o que não era claro na transformada de fourier.
Isso acontece pois o espectrograma faz transformadas de fourier em subintervalos.

## Parte2

### Questão 1

Código: parte2/q1.py

A maneira mais simples de resolver o problema dos Ringings é aplicando um filtro passa baixa.
Apliquei um filtro gaussiano (do scipy) com sigma 1.5. Segue o resultado:

![gaussian](parte2/gaussian.bmp)

A desvantagem do filtro gaussiano é que ele embaça bastante a foto. Provavelmente, pode-se obter
um resultado melhor usando filtro sinc. fonte: [https://en.wikipedia.org/wiki/Ringing_artifacts#Causes](https://en.wikipedia.org/wiki/Ringing_artifacts#Causes)

### Questão 2

Código: parte2/q2.py
Parte mais relevante do código:

    text = pytesseract.image_to_string(img)
    without_spaces = re.sub('\s+', '', text)

    print(len(without_spaces))

Não obtive muito sucesso com meus algoritmos, então apelei para o Tesseract, que é uma ferramenta para reconhecer textos em imagens. Bastou apenas remover os espaços e os '\n' ( usei expressões regulares). Número de caracteres: 211.

TODO: explicar minhas tentativas

### Questão 3

Analisando as componentes RGB da imagem separadamente( e em tons de cinza), notei que o número fica evidente ao comparar
as imagens das componentes R e G ( passando de uma para outra, como em um slideshow). Comparar a componente azul com qualquer uma das outras duas não deixou o número evidente para mim.
Assim, decidi trocar as componentes vermelhas e verdes assim:

    cb[:, :, 0] = 255 / 2 + (dalton[:, :, 0] - dalton[:, :, 1])
    cb[:, :, 1] = 255 / 2 + (dalton[:, :, 1] - dalton[:, :, 0])

Resulta em:

![color_blind](parte2/color_blind.bmp)

É meio difícil explicar a motivação de tal transformação, mas devo dizer que foram várias tentativas até chegar nesta, que deixa bem evidente a distinção.
