AI Engineering | Meu Segundo Cérebro com IA
Projeto de portfólio — Desafio DIO: Acelere sua Aprendizagem com IA / NotebookLM  
Autoria: Dayane Beltrame | Data: 7 de novembro de 2026  
Ferramenta: Gemini Notebook (NotebookLM)
Acessar o meu Segundo Cérebro com IA · Apresentação em PDF · Evidência de fontes e resposta
1. Tema e objetivo
Tema: Engenharia de Inteligência Artificial aplicada a Python, APIs REST, desenvolvimento backend, agentes inteligentes, automação e segurança.
> Desenvolver um segundo cérebro inteligente, fundamentado em documentação técnica e fontes verificáveis, para aprofundar meus conhecimentos em Python, engenharia de software, APIs, agentes de inteligência artificial e automação, transformando o aprendizado em competências aplicáveis a projetos reais.
Escolhi este tema para consolidar minha formação em Análise e Desenvolvimento de Sistemas e praticar uma habilidade fundamental na Engenharia de IA: não apenas obter respostas de modelos, mas investigar suas fontes, identificar imprecisões e documentar os resultados.
2. Metodologia
Defini o objetivo e os limites de atuação do notebook.
Selecionei fontes de referência em três formatos: documentação e artigos web, vídeo e PDF.
Configurei um tutor personalizado para explicar conceitos técnicos com base nas fontes importadas.
Fiz perguntas sobre Python e FastAPI e pedi uma revisão crítica de respostas problemáticas.
Gerei uma apresentação no Estúdio e organizei as evidências, materiais de estudo e observações técnicas neste repositório.
Princípio de qualidade: diferenciar fatos comprovados, análises críticas e propostas conceituais; não afirmar que um software foi implementado ou testado quando se trata apenas de um exercício de aprendizagem.
3. Fontes utilizadas
ID	Fonte	Tipo	Justificativa da escolha	Conteúdo estudado
F01	Python Tutorial — Python Software Foundation	Documentação oficial	Referência primária da linguagem	Funções, estruturas de dados e execução
F02	FastAPI — First Steps	Documentação oficial	Material mantido pelo projeto FastAPI	Rotas, métodos HTTP e documentação automática
F03	Google Cloud — What are AI agents?	Artigo técnico	Explicação de um provedor reconhecido de infraestrutura de IA	Agentes e seus componentes
F04	Harvard CS50P — Lecture 0	Vídeo do YouTube	Aula universitária de introdução à programação	Funções e variáveis em Python
F05	OWASP GenAI LLM Top 10 (2026)	PDF	Projeto especializado em riscos de segurança de aplicações com IA	Ameaças e medidas defensivas
As cinco fontes aparecem na captura do notebook. O inventário está em `fontes.csv`, com os critérios em `criterios-de-curadoria.md`.
4. Diretriz dada ao notebook
Configurei a opção Personalizado para orientar o comportamento do tutor:
> Atue como meu mentor de Engenharia de IA, Python, backend, APIs e agentes inteligentes. Responda exclusivamente com base nas fontes selecionadas. Inclua referências verificáveis para afirmações técnicas, explique os conceitos progressivamente e proponha exercícios. Não invente informações, citações, códigos executados ou resultados. Quando as fontes não forem suficientes, informe a limitação. Diferencie fatos, exemplos e hipóteses.
Versão completa: `diretriz-do-notebook.md` · `DIRETRIZ_COPIAR.txt`.
5. Perguntas feitas, respostas e análise crítica
Pergunta 1 — Python e FastAPI
Pergunta executada: "Explique como Python e FastAPI podem ser utilizados para desenvolver uma API REST profissional. Apresente os conceitos fundamentais, um exemplo prático de endpoint e boas práticas de desenvolvimento. Fundamente sua resposta nas documentações oficiais presentes neste notebook, incluindo citações verificáveis."
Síntese da resposta real: o notebook explicou funções e parâmetros em Python, métodos HTTP, caminhos de API, decoradores FastAPI, endpoints, Uvicorn, OpenAPI, Swagger e considerações de segurança.
Fontes pertinentes à resposta: F01 (Python Tutorial), F02 (FastAPI First Steps) e F05 (OWASP). A correspondência exata de cada citação com seu trecho de origem ainda precisa ser documentada por captura de tela.
Pergunta 2 — Revisão crítica
Pergunta executada: "Revise criticamente sua resposta anterior sobre Python e FastAPI. Corrija qualquer imprecisão técnica, especialmente sobre a execução do Python e a sanitização de entradas. Apresente uma resposta resumida, com cinco conceitos fundamentais, citando expressamente os trechos das fontes oficiais que sustentam cada afirmação. Se uma informação não estiver fundamentada nas fontes, sinalize isso."
Síntese da resposta real: o tutor reconheceu que operações simples de formatação de strings não são suficientes para proteger APIs contra injeção e reestruturou cinco conceitos fundamentais, mas manteve uma descrição excessivamente simplificada da execução de Python.
Fontes pertinentes à resposta: F01, F02 e F05, também com validação visual das citações pendente.
Minha avaliação técnica: métodos como `.strip()`, `.title()` e `.split()` não equivalem à validação de entradas contra ataques. Além disso, na implementação CPython o código geralmente é compilado para bytecode, depois executado pela máquina virtual; a descrição "tradução linha por linha" não é tecnicamente adequada. Registrar e corrigir esses erros é parte da proposta educacional.
Evidências e detalhes: `registro-das-respostas.md` · `fontes-e-primeira-resposta-real.png` · `perguntas-e-testes.md`.
6. Materiais e entregáveis
Arquivo	Descrição	Origem
`AI_Second_Brain_Architecture.pdf`	Apresentação de 10 slides sobre arquitetura, Python, FastAPI, agentes e OWASP	Gerada no Estúdio do Gemini Notebook
`REVISAO_TECNICA_DA_APRESENTACAO.md`	Análise crítica dos conceitos e limites dos slides	Avaliação complementar
`guia-de-estudos-autoral.pdf`	Guia de estudo, conceitos e exercícios	Material autoral complementar
`mapa-conceitual-autoral.png`	Organização visual dos conteúdos	Material autoral complementar, não exportado do Estúdio
`fontes-e-primeira-resposta-real.png`	Captura real das fontes e interação	Evidência do notebook
Pendente: adicionar o mapa mental efetivamente exportado ou capturado no Estúdio e uma captura com pelo menos uma citação aberta, mostrando claramente a resposta e o trecho correspondente da fonte.
7. Limitações e próximas etapas
Este é um projeto de curadoria, estudo e avaliação de uma ferramenta de IA. Os diagramas de arquitetura da apresentação são ilustrativos: não comprovam que um agente autônomo, microsserviço ou infraestrutura cloud foram implementados ou testados.
Antes da entrega definitiva, ainda é necessário:
[ ] Confirmar, por captura, o trecho de origem de uma citação do Python e outra do FastAPI.
[ ] Publicar a captura ou exportação real do mapa mental gerado no Gemini Notebook.
[ ] Testar o acesso ao notebook compartilhado em uma janela anônima ou com outra conta.
[x] Publicar o repositório GitHub com materiais de estudo, fontes e apresentação.
8. Ética, segurança e direitos autorais
As fontes de terceiros são referenciadas por links e atribuição. Este repositório não deve conter credenciais, dados privados nem conteúdo de outros projetos. Resultados da IA são distinguidos das avaliações humanas e de propostas que ainda não foram implementadas.
Links
Notebook compartilhado
Desafio DIO
---
Status: repositório publicado e documentação preparada. A validação final exige as capturas de citações e o mapa mental real, sem apresentar pendências como entregas concluídas.
