<img src="../static/logo-inteli.png" alt="Logo do Inteli" style="height: 100%; width:50vp; display: block; margin-left: auto; margin-right: auto; margin-bottom:16px"/>

# Atividade 5: Resenha sobre o artigo

## Enunciado

Esta atividade ponderada tem por objetivo realizar a construção de uma comparação com o que foi desenvolvido nas outras atividades ponderadas e o artigo lido durante o autoestudo da semana. Os alunos deverão fazer uma comparação do que foi implementado por eles, com o que foi proposto pelo artigo, comparando as similaridades e diferenças. A resenha não deve possuir mais que 1000 palavras, sendo que, eventuais códigos utilizados para demonstração, não fazem parte desta contagem.

Artigo de referência: [Machine learning for internet of things data analysis: a survey](https://www.sciencedirect.com/science/article/pii/S235286481730247X)

## Padrão de qualidade

Os pontos que serão avaliados na entrega do projeto:
1. ***(Até 4.0 ponto)*** Sumarização dos pontos principais do artigo: apresentou uma sumarização com as informações principais do artigo;
2. ***(Até 3.0 ponto)*** Comparação com as técnicas utilizadas no desenvolvimento do projeto;
3. ***(Até 3.0 ponto)*** Resenha Crítica: desenvolvimento de uma resenha crítica sobre o artigo, apresentando os pontos positivos e negativos, destacando o que foi testado no projeto.

## Instruções:

A entrega do projeto deve ser realizada dentro de um repositório público do Github do estudante. Ao entregar a atividade no sistema da instituição, o estudante deve colocar o link para seu repositório.

O arquivo README do repositório deve conter as informações do estudante e a resenha desenvolvida sobre o artigo.

## Prazo de Entrega:

O prazo oficial de entrega é até o dia 28/09/2023 (23h59).

## Resenha sobre o artigo

No artigo “Machine learning for internet of things data analysis: a survey” os autores utilizaram 70 artigos da área de IoT (internet das coisas) para estabelecer uma relação entre esta área e a área de ciência dos dados e estabelecer uma estrutura investigacional e de classificação para a aplicação de algoritmos de aprendizagem de máquina nesse contexto. Esse tipo de contribuição é importante pois estima-se que já em 2020 cerca de 25 a 50 bilhões de dispositivos já estejam conectados. Dentre este dispositivos estão tecnologias embarcadas, dispositivos de comunicação com e sem fio, sensores, atuadores e demais artefatos de hardware conectados à internet.

No contexto de IoT, a ciência dos dados é uma ferramenta poderosa para tornar esses dispositivos mais inteligentes em suas intervenções nos ambientes e em seus processos de coleta de dados. Com isso, técnicas de mineração de dados e aprendizado de máquina podem ser utilizadas para extrair insights valiosos dos dados coletados por aplicações IoT. O presente artigo se propôs a estabelecer um tipo de “taxonomização” para diferentes algoritmos de machine learning aplicados a dados de IoT, características inerentes a dados extraídos dessas fontes e cidades inteligentes como uma aplicação das tecnologias mencionadas. 

Para tanto, os autores do artigo revisaram cerca de 70 artigos na área de análise de dados de IoT e separaram oito tipos principais de algoritmos que podem ser utilizados para processar esses dados. Os algoritmos analisados pelos autores foram categorizados com base em suas similaridades estruturais, tipos de dados que processam e quantidade de dados que são capazes de processar em um período de tempo razoável para a aplicação em dispositivos de IoT. 

O artigo ainda introduz o novo conceito de “smart data”, que, segundo os autores, seria uma forma de transformar dados brutos em dados inteligentes, visando sua aplicação em cenários de aumento de produtividade e eficiência de processos. Este conceito foi discutido em grande parte no caso das smart cities, uma vez que elas representaram cerca de 60% dos artigos que os autores revisaram. Da mesma forma, o funcionamento de alguns algoritmos clássicos de machine learning como a máquina de vetores suplementares (SVM) é explicado no contexto da previsão do tráfego em uma cidade inteligente.

Por fim, a estrutura do artigo envolve revisão dos artigos mencionados, uma discussão sobre aplicações potenciais de IoT, tipos de protocolos de comunicação, ferramentas computacionais para gestão da infraestrutura de IoT, arquiteturas de IoT e o segmento de cidades inteligentes. O artigo também passa pelos pontos de qualidade dos dados coletados, gerenciamento de big data, integração de dados de diferentes fontes e sua anotação semântica. Uma análise de algoritmos de aprendizado de máquina foi feita no final com uma divisão de oito categorias, seguidas de uma correspondência com suas aplicações no campo de cidades inteligentes.

Durante a leitura do artigo, foi possível encontrar diversos paralelos com a realização das ponderadas propostas durante o módulo 7 do curso de engenharia de computação do Inteli Instituto de Tecnologia e Liderança. No início das atividades ponderadas, o objetivo foi a criação de uma aplicação web simples que tivesse um controle de acesso para a funcionalidade de incluir, editar e excluir notas. O diferencial deste módulo para o módulo 2, onde o desenvolvimento web era o foco, foi no deploy da aplicação web em nuvem. Neste ponto, já encontramos o primeiro paralelo com o artigo, uma vez que disponibilizar aplicações na internet com suas devidas modularizações e controle de acesso são pilares compartilhados pela arquitetura IoT discutida no artigo. No decorrer das ponderadas, o escopo assumido foi o treinamento e disponibilização de um modelo de machine learning em nuvem, também essencial para a arquitetura de soluções de IoT, uma vez que a disponibilidade de modelos em nuvem permite que os dispositivos físicos sejam mais baratos ao poderem ter poder de processamento e memória reduzidos. Para o treinamento do modelo das ponderas em si, as técnicas de pré-processamento, curadoria dos dados, modelos, treinamento e configuração de um modelo para deploy, várias das técnicas discutidas no artigo foram utilizadas, como a extração de características por análise de componentes principais e a avaliação de sua classificação por modelos como K Vizinhos Mais Próximos, Naive Bayes, Máquina de Vetores de Suporte, Regressão Linear e Árvores de Decisão Aleatórias. 

No que diz respeito a importância da visualização de dados discutida no artigo, ela foi a mesma temática da última ponderada, onde foi feito um dashboard para a visualização de dados e resultados dos modelos. Novamente, é percebida a similaridade nas ênfases em tecnologias de infraestrutura de nuvem e aplicações que sejam capazes de integrar dados de várias fontes. Ao mesmo tempo, enquanto o projeto feito durante as atividades ponderas tinha como objetivo o desenvolvimento de habilidades na construção e disponibilização de aplicações web em nuvem, o artigo teve como objetivo a discussão de um framework de análise e categorização de modelos, bem como a discussão destes no contexto de smart cities. 

Em síntese, o artigo "Machine Learning for Internet of Things Data Analysis: A Survey" apresenta uma contribuição significativa ao estabelecer uma estrutura investigacional para a aplicação de algoritmos de aprendizado de máquina na análise de dados de IoT. Tanto o artigo quanto às atividades ponderadas convergem para a importância da integração entre IoT, ciência de dados e machine learning. Essa convergência destaca a relevância prática e aplicabilidade dos conceitos discutidos, contribuindo para a compreensão e avanço dessas tecnologias.

