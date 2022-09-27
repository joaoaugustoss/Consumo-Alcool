# Iniciação Científica
Repositório para manutenção de código desenvolvido no projeto de pesquisa orientado pelo professor Felipe Domingos da Cunha - PUC Minas

## Código
### twitter_api.py
O arquivo [twitter_api.py](IC/twitter_api.py)  contém o código desenvolvido para a coleta de check-ins postados no Foursquare Swarm e publicados 
no Twitter utilizados para montagem da base de dados a ser utilizada na sequência do trabalho. Para o funcionamento do código foram feitas requisições
na [Twitter API](https://developer.twitter.com/en) utilizando o serviço de [Filtered Stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction), que retorna todos os tweets postados durante a execução do código com uma determinada tag
escolhida pelo desenvolvedor.

### filter.py
O arquivo [filter.py](IC/tfilter.py) e [filter2.py](IC/filter2.py) foram duas versões do código desenvolvido para o tratamento dos dados coletados pelo código anterior. O tratamento foi
feito através da abertura do arquivo gerado pela coleta na API. O primeiro passo no código consiste na abertura do arquivo gerado pela API para armazenar
os atributos necessários e descartar o que foi considerado lixo, para isso, foi utilizada a metodologia de abrir o código HTML do site utilizando a linguagem
python observando os padrões necessários para a extração dos atributos necessários, que na primeira versão, foram utilizados como parâmetro na 
[Places API](https://developer.foursquare.com/docs/places-api-overview) do Foursquare, mas pelo baixo limite de requisições disponíveis, passamos a resgatar todos
os atributos necessários no próprio código HTML do link extraído do Twitter. <br>
Seguem os atributos utilizados para a montagem do arquivo CSV:

<ul>
  <li>ID do tweet coletado</li>  
  <li>ID do local onde o check-in foi realizado no Foursquare</li>  
  <li>ID do usuário que fez o check-in no Swarm</li>  
  <li>Link coletado no Twitter</li>  
  <li>Nome do local onde o check-in foi realizado</li>  
  <li>Categoria do local onde o check-in foi realizado</li>  
  <li>País do check-in</li>  
  <li>Estado do check-in</li>
  <li>Cidade do check-in</li>  
  <li>Timestamp indicando o horário de coleta do tweet</li>  
</ul>
