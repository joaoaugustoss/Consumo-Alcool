# Estudo do Comportamento de Consumo de Bebida em Centros Urbanos usando Redes de Sensoriamento Participativo
O número de pessoas acometidas por doenças relacionadas ao abuso no consumo de bebidas alcoólicas tem crescido consideravelmente ao longo dos anos, contabilizando um total de 3 milhões de mortes ao ano em todo o mundo. Entretanto, não existem muitas aplicações voltadas à auxiliar essas pessoas em recuperação. Tendo em vista este cenário, na literatura encontramos técnicas de aprendizado de máquina que podem ajudar na identificação e caracterização de regiões geográficas propícias para o consumo alcoólico em grandes cidades utilizando dados urbanos. Este trabalho analisa o uso de Redes Sociais baseadas em Localização (LBSN) para avaliar o consumo de bebidas em Tóquio e Nova York. Foram coletados dados de check-ins em bares e restaurantes em ambas as cidades e, a partir de técnicas de aprendizagem de máquina foi possivel examinar os padrões de consumo de bebidas morados das cidades. Resultados indicaram que, embora houvesse diferenças culturais nos hábitos de consumo de bebidas entre as duas cidades, os usuários tendiam a consumir mais álcool nos finais de semana e à noite. Além disso, foi possível identificar as regiões mais propícias a esse consumo.

## Código
### twitter_api.py
O arquivo [twitter_api.py](Consumo-Alcool/twitter_api.py)  contém o código desenvolvido para a coleta de check-ins postados no Foursquare Swarm e publicados 
no Twitter utilizados para montagem da base de dados a ser utilizada na sequência do trabalho. Para o funcionamento do código foram feitas requisições
na [Twitter API](https://developer.twitter.com/en) utilizando o serviço de [Filtered Stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction), que retorna todos os tweets postados durante a execução do código com uma determinada tag
escolhida pelo desenvolvedor.

### filter.py
O arquivo [filter.py](Consumo-Alcool/filter.py) é o código desenvolvido para o tratamento dos dados coletados pelo código anterior. O tratamento foi
feito através da abertura do arquivo gerado pela coleta na API. O primeiro passo no código consiste na abertura do arquivo gerado pela API para armazenar
os atributos necessários e descartar o que foi considerado lixo, para isso, foi utilizada a metodologia de abrir o código HTML do site utilizando a linguagem
python observando os padrões necessários para a extração dos atributos necessários, que na primeira versão, foram utilizados como parâmetro na 
[Places API](https://developer.foursquare.com/docs/places-api-overview) do Foursquare, mas pelo baixo limite de requisições disponíveis, passamos a resgatar todos
os atributos necessários no próprio código HTML do link extraído do Twitter. <br>
Seguem os atributos utilizados para a montagem do arquivo CSV:

<ul>
  <li>Identificador da venue no Foursquare</li>  
  <li>Identificador do usuário no Swarm</li>  
  <li>Nome da venue onde foi efetuado o check-in</li>  
  <li>Link coletado no Twitter</li>  
  <li>Categoria da venue onde foi efetuado o check-in</li>  
  <li>País da venue onde foi efetuado o check-in</li>  
  <li>Cidade da venue onde foi efetuado o check-in</li>
  <li>Horário no qual o check-in foi compartilhado no Twitter</li> 
  <li>Latitude da venue onde foi efetuado o check-in</li> 
  <li>Longitude da venue onde foi efetuado o check-in</li>  
</ul>

### update.py
O arquivo [update.py](IC/update.py) é o código desenvolvido para o tratamento de diferentes versões da base de dados fazendo com que ela fosse atualizada
de acordo com os atributos escolhidos para a composição da mesma.
