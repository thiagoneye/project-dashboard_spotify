# project-dashboardspotify

“Sem música a vida não faria sentido."
Nietzsche, F.

Nos últimos meses, durante estudos sobre o Power BI, algumas pessoas buscaram fazer análises dos seus dados pessoais no Spotify, uma alternativa à tradicional e querida retrospectiva disponibilizada pela plataforma no fim de cada ano.
Eis que resolvo entrar na brincadeira e desenvolver um projeto com base nos meus dados. Para tanto, dividi todo o processo em três etapas: pré-processamento; visualização de dados e análise crítica.

1. Pré-processamento:

Os dados foram gerados em dois arquivos no formato JSON, contendo as informações: endTime (data e hora de finalização), artistName (nome do artista), trackName (nome da trilha de reprodução) e msPlayed (tempo de reprodução em milissegundos).

A partir disso, através da linguagem Python, realizei uma análise exploratória e as seguintes features (características) foram geradas: turnos e gêneros musicais. Para a obtenção dessa última, executei uma web scraping, buscando o principal gênero de cada artista através do site da Wikipédia.
Por fim, exportei os dados no formato CSV.

2. Visualização de dados:

Para a visualização de dados, a ferramenta escolhida foi o Power BI. A paleta de cores selecionada foi a da identidade visual da marca (inclusive, o brandbook foi consultado para conhecimento das recomendações da empresa).
Para melhor organização, os dados foram apresentados em três categorias de análise: frequência (número de ocorrências), tempo (duração das reproduções) e gênero.

3. Análise crítica:

Por fim, vários insights foram obtidos, como explico a seguir:

- Houve uma alta variedade de músicas, artistas e gêneros (principalmente variações de Rock);
- A banda Arctic Monkeys foi a mais reproduzida, assim como seu gênero e várias de suas músicas;
- O mês de menor reprodução foi o de abril: quando iniciei o estágio, passando boa parte do meu tempo em atividades presenciais;
- O mês de maior reprodução foi o de maio: quando iniciei o regime home office, as músicas de plano de fundo foram minhas companheiras durante minhas horas de trabalho;
- Meus hábitos noturnos foram evidenciados através da análise, visto que boa parte das reproduções foram durante a madrugada;
- A web scraping não conseguiu categorizar todas as reproduções, porém a eficiência foi satisfatória.

Apesar de o projeto ser bem simples, sem dúvidas agregou muito em minha busca pelo conhecimento, ajudando-me a praticar alguns conceitos e aprender sobre outros.

Créditos: Parte do layout foi inspirado no layout de [Letícia Bahr](https://dribbble.com/shots/6434639-Artists-Spotify-Dashboard).
