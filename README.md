**Meu Segundo Cérebro com IA:** https://notebook.google.com/notebook/3f126bd0-0531-4f2b-a92e-90604b2ab848

AI Engineering | Meu Segundo Cérebro com IA
Projeto de portfólio — Desafio DIO: Acelere sua Aprendizagem com IA / NotebookLM  
Autoria: Dayane Beltrame · Data: 7 de novembro de 2026  
Ferramenta: Gemini Notebook (NotebookLM)
Acessar meu Segundo Cérebro com IA · Apresentação em PDF · Evidência de fontes e resposta
1. Tema e objetivo
Tema: Engenharia de Inteligência Artificial aplicada a Python, APIs REST, desenvolvimento backend, agentes inteligentes, automação e segurança.
> Desenvolver um segundo cérebro inteligente, fundamentado em documentação técnica e fontes verificáveis, para aprofundar meus conhecimentos em Python, engenharia de software, APIs, agentes de inteligência artificial e automação, transformando o aprendizado em competências aplicáveis a projetos reais.
Escolhi este tema para consolidar minha formação em Análise e Desenvolvimento de Sistemas e praticar uma habilidade fundamental em Engenharia de IA: não apenas obter respostas, mas examinar suas fontes, detectar imprecisões e documentar o processo de aprendizagem.
2. Metodologia
Defini o objetivo e os limites de atuação do notebook.
Selecionei cinco fontes em formatos complementares: documentação e artigos web, vídeo do YouTube e PDF.
Configurei um tutor personalizado para explicar conceitos técnicos com base exclusivamente nas fontes importadas.
Fiz perguntas sobre Python e FastAPI e solicitei revisão crítica de respostas problemáticas.
Gerei uma apresentação no Estúdio do Gemini Notebook e organizei as evidências e os materiais de estudo.
Critério de qualidade: diferenciar fatos verificados, análises críticas e propostas conceituais. O projeto não declara que arquiteturas ilustradas foram efetivamente implementadas.
3. Fontes utilizadas e critérios de confiança
ID	Fonte	Formato	Por que considero confiável	Uso no notebook
F01	Python Tutorial — Python Software Foundation	Documentação oficial	Referência primária da linguagem	Funções, estruturas de dados e execução
F02	FastAPI — First Steps	Documentação oficial	Mantida pelo próprio projeto FastAPI	Rotas, métodos HTTP e documentação automática
F03	Google Cloud — What are AI agents?	Artigo técnico	Fonte identificável de fornecedor de infraestrutura de IA	Agentes e seus componentes
F04	Harvard CS50P — Lecture 0	Vídeo do YouTube	Aula universitária publicada pelo curso CS50	Funções e variáveis em Python
F05	OWASP GenAI LLM Top 10 (2026)	PDF	Projeto especializado em segurança de aplicações com IA	Riscos e medidas defensivas
As cinco fontes carregadas aparecem na captura real do notebook. O inventário está em `fontes.csv` e os critérios detalhados, em `criterios-de-curadoria.md`.
4. Diretriz personalizada do tutor
Configurei a opção Personalizado no Gemini Notebook com a seguinte orientação central:
> Atue como meu mentor de Engenharia de IA, Python, backend, APIs e agentes inteligentes. Responda exclusivamente com base nas fontes selecionadas. Inclua referências verificáveis para afirmações técnicas, explique os conceitos progressivamente e proponha exercícios. Não invente informações, citações, códigos executados ou resultados. Quando as fontes não forem suficientes, informe a limitação. Diferencie fatos, exemplos e hipóteses.
Diretriz completa: `diretriz-do-notebook.md` · `DIRETRIZ_COPIAR.txt`.
5. Perguntas executadas, respostas e análise crítica
Q01 — Como Python e FastAPI ajudam a desenvolver APIs REST?
Pergunta: “Explique como Python e FastAPI podem ser utilizados para desenvolver uma API REST profissional. Apresente os conceitos fundamentais, um exemplo prático de endpoint e boas práticas de desenvolvimento. Fundamente sua resposta nas documentações oficiais presentes neste notebook, incluindo citações verificáveis.”
Resposta observada: o tutor explicou funções e parâmetros Python, métodos HTTP, caminhos, decoradores e endpoints FastAPI, Uvicorn, OpenAPI, Swagger e recomendações de segurança.
Fontes relevantes: F01 (Python Tutorial), F02 (FastAPI First Steps) e F05 (OWASP). Pendente: captura com os identificadores de citação abertos e o trecho original correspondente.
Q02 — Revisão crítica da resposta
Pergunta: “Revise criticamente sua resposta anterior sobre Python e FastAPI. Corrija qualquer imprecisão técnica, especialmente sobre a execução do Python e a sanitização de entradas. Apresente uma resposta resumida, com cinco conceitos fundamentais, citando expressamente os trechos das fontes oficiais que sustentam cada afirmação. Se uma informação não estiver fundamentada nas fontes, sinalize isso.”
Resposta observada: o tutor reconheceu que operações simples de formatação de strings não são suficientes para proteger APIs contra injeção e reorganizou os conceitos, mas manteve uma explicação muito simplificada da execução do Python.
Minha avaliação técnica: `.strip()`, `.title()` e `.split()` não são mecanismos de sanitização de segurança. Na implementação CPython, o código é normalmente compilado em bytecode e executado por máquina virtual; a ideia de “tradução linha por linha” é imprecisa. A detecção dessas falhas demonstra a importância da supervisão humana mesmo em respostas ancoradas em fontes.
Registro: `registro-das-respostas.md` · captura real · `perguntas-e-testes.md`.
6. Materiais entregues
Material	Tipo	Origem
AI_Second_Brain_Architecture.pdf	Apresentação de 10 slides	Gerada no Estúdio do Gemini Notebook
REVISAO_TECNICA_DA_APRESENTACAO.md	Avaliação técnica dos slides	Análise complementar
guia-de-estudos-autoral.pdf	Guia de conceitos e exercícios	Material autoral complementar
mapa-conceitual-autoral.png	Organização visual dos conceitos	Material autoral, não exportado do Estúdio
fontes-e-primeira-resposta-real.png	Captura das fontes e da conversa	Evidência de uso real
Evidências finais pendentes: adicionar a imagem real do mapa mental gerado no Estúdio e uma captura da resposta contendo ao menos uma citação aberta e o trecho de origem visível. Esses itens não são substituídos pelo mapa autoral.
7. Limites, próximos passos e transparência
Este projeto demonstra curadoria de fontes, configuração de um tutor com IA, aprendizagem ativa e avaliação crítica. Diagramas de agentes, microsserviços e nuvem na apresentação são modelos conceituais, não sistemas implementados ou testados.
[ ] Verificar e registrar o trecho original de uma citação de Python e outra de FastAPI.
[ ] Publicar a captura/exportação do mapa mental real do Estúdio.
[ ] Testar o acesso ao notebook compartilhado em janela anônima ou outra conta.
[x] Criar o notebook, configurar o tutor e importar cinco fontes.
[x] Realizar duas interações de estudo e uma revisão crítica.
[x] Gerar a apresentação em PDF e publicar o repositório no GitHub.
8. Ética, segurança e direitos autorais
Fontes de terceiros são referenciadas por links e atribuições; credenciais e materiais internos de outros projetos não devem ser publicados. As saídas de IA são distintas da avaliação humana e de funcionalidades apenas propostas.
Links: Gemini Notebook compartilhado · Desafio DIO
