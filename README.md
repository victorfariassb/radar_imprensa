# iPrensa
Olá, seja bem-vinde ao iPrensa. Este programa raspa os dados dos dois principais portais de notícias do Brasil (Uol e Globo) e dos sites da Folha, do Estadão da CNN e da Jovem Pan. Além de raspar os dados, o programa guarda as informações na planilha abaixo. A raspagem é programada para ocorrer a cada hora,

DADOS
https://docs.google.com/spreadsheets/d/1UY2MkXq41EBEU5AXxGDE2oVrd8rQgPcc28xWi7oHVOU/edit?usp=sharing

Com algumas exceções, os dados coletados dos sites são: 
- nº da matéria;
- data;
- título;
- posição ou classe(se é manchete, destaque, coluna etc);
- link.

### Análise dos dados
Com os dados da planilha, o iPrensa faz análises e salva essas informações em uma tabela:
1. Termos mais mencionados nos jornais;
2. Número de vezes que os pré-candidatos à Presidência em 2022 foram mencionados;
3. Número de vezes que times foram mencionados nas seções de esportes do Uol e da Globo;
4. A palavra que mais apareceu na parte principal dos sites;


## Como funcionam as análises:

### Termos mais mencionados
O filtro funciona da seguinte forma:
1. Todas as palavras foram colocadas em caixa baixa;
2. Foi feito um filtro para tirar uma série de palavras que são comuns em textos, mas não acrescentam muito significado em uma análise como esta. Entre as palavras retiradas estão: verbos, números e adjetivos;
3. Uma ordenação trouxe as 10 mais mencionadas.

OBS: Neste caso, queremos saber quais palavras apareceram mais e por mais tempo nos sites. Por isso, títulos iguais que aparecem mais de uma vez no dia (algo comum) são considerados na análise. Isso quer dizer que se a palavra "milho" apareceu somente em uma matéria no ano, mas essa matéria passou 2 dias na página principal do site, ela irá aparecer com um número bem maior que 1.

### Ranking dos pré-candidatos
O filtro funcinou assim:
1. Foi retirado alguns nomes que poderiam confundir com os dos pré-candidatos. "Eduardo Bolsonaro", por exemplo, virou "Eduardo B.";
2. Cada vez que o nome de um pré-candidato apareceu em um título foi contado.

OBS: Neste caso, como queremos saber a quantidade de matéria produzida sobre o candidato, não consideramos na conta matérias iguais. Ou seja, se o Doria só apareceu em uma matéria durante o ano, mas essa matéria passou 2 dias na página principal do site, ele irá aparece com o número 1.

### Termo do dia
1. As 35 primeiras matérias (que ficam no topo da página e, por isso, são mais importantes) são selecionadas;
2. Remove-se os links duplicados;
3. Faz-se um processamento de linguagem natural por meio do Spacy;
4. A palavra mais mencionada é selecionada;

### Ranking dos times
1. Faz-se uma busca pelos nomes dos times em matérias qdo Uol e da Globo que contenham "futebol" ou "esporte" no link;
2. Deleta-se links duplicados;
3. Os termos são contados, e o ranking é gerado

## Última atualização
24/07/2022

## Autoria
Victor Farias, com orientação de Eduardo Cuducos, Bernardo Vianna, Paula Cristina dos Santos, Vinícius Sueiro, Rodrigo Menegat, Tiago Maranhão e Álvaro Justen, no âmbito do Master em Jornalismo de Dados do Insper. 
Contato victorfariassb@gmail.com
