# Alinhamento com AI Engineering From Scratch — dois medidores independentes

**Referência externa verificada em 2026-11-07:** [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch), currículo oficial em [AI Engineering From Scratch](https://aiengineeringfromscratch.com/), com **20 fases e 542 aulas** nessa revisão.

## 1. Medidor curricular — APRENDIZAGEM PESSOAL

**Objetivo:** acompanhar o progresso real nas 20 fases/542 aulas, independente da produção de código empresarial. O denominador oficial é o total do currículo verificado na data. O mapa completo está em [`data/ai-engineering-from-scratch-curriculum.json`](../data/ai-engineering-from-scratch-curriculum.json); o teste confere os 542 itens totais e os vínculos com a versão local de 11 trilhas.

**Privacidade:** não registrar aulas estudadas pelo usuário em arquivos deste repositório **público**. Dados individuais de estudo, leituras, avaliações e respostas de entrevista ficam em fonte PRIVADA previamente autorizada. Sem fonte privada verificável ou confirmação do próprio usuário, reportar **PERCENTUAL CURRICULAR NÃO VERIFICADO** (não 0% fictício).

**Critério de avanço:** uma aula só é marcada como **ESTUDADA** após confirmação explícita do estudante com referência específica de fase/aula e data; uma aula só é marcada como **PRÁTICA VERIFICADA** com prova técnica real, quando o tipo de lição a exigir. Não inferir que um vídeo assistido, um resumo gerado por agente ou um trabalho de terceiro prova domínio; leitura e implementação devem permanecer métricas distintas.

Formato para relatório diário:
```text
CURRÍCULO AI ENGINEERING FROM SCRATCH
Fases: 20 | Aulas na revisão atual: 542
Aulas com estudo confirmado: NÃO VERIFICADO (sem dados privados)
Aulas com prática verificada: NÃO VERIFICADO
Próxima fase/aula: referenciar fonte e pendência real
```

Quando dados privados verificados existirem, usar `estudadas/542 × 100` e `praticadas/542 × 100`, sempre com **referência versionada** e contagem sem duplicações; nunca publicar respostas, histórico, notas pessoais ou fonte privada no GitHub. Não usar 100% de leitura como alegação de prontidão de carreira.

## 2. Medidor aplicado — PORTFÓLIO AI ENGINEER

**Objetivo:** concluir [11 trilhas internas](../README.md) com seis critérios profissionais de aceite, totalizando **66 gates de engenharia**. Código, CI do SHA exato, avaliação, segurança, reprodutibilidade e demo verificada. Resultado inicial da nova auditoria conservadora: **0/66 gates certificados sob a nova régua; 0/11 trilhas integralmente homologadas**. Isso não apaga trabalho parcial pré-existente. Detalhes em [PROGRESS_METER.md](PROGRESS_METER.md).

## Por que não combinar as porcentagens?

Uma aula lida e uma integração em produção são unidades distintas. Somar ambas produziria um índice sem interpretação objetiva e permitiria **100% falso**. A rotina deve trazer **dois indicadores paralelos**, com seus próprios denominadores, estados e provas.

- 100% **Currículo** = todas as aulas do escopo de referência estudadas e confirmadas; domínio prático tem acompanhamento separado.
- 100% **Portfólio** = 66/66 gates independentes aceitos e 11/11 trilhas homologadas.
- 100% **InstantWork** = NÃO é calculado desses indicadores; depende de gates próprios de produto e release.

## Mapa de cobertura

Todas as 20 fases constam no mapa versionado de 2026-11-07. **17** estão ligadas diretamente a pelo menos uma das 11 trilhas de portfólio; as fases **06 Speech & Audio**, **09 Reinforcement Learning** e **12 Multimodal AI** não têm trilha diretamente dedicada nesta versão e não podem ser consideradas cumpridas pelo progresso no portfólio. Isso revela lacunas do currículo completo, mas não obriga criar 3 apps desconectados para preenchê-las; podem ser estudadas de modo independente e avaliadas por projetos futuros.

A rota profissional preferencial é [Applied AI Engineer / LLM Product Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json). O curso também oferece módulos especializados de MCP e Agent Skills; são referências complementares, não garantias de certificação.

## Revalidação da fonte

O curso tem histórico de atualizações; a contagem de 542 foi observada na data acima. Quando o upstream aumentar/reorganizar conteúdos, comparar a versão e mostrar a mudança do denominador **antes** de recalcular porcentagens, preservando histórico. Nunca atualizar total de aulas silenciosamente nem marcar todos os tópicos do novo currículo como concluídos automaticamente.

### Reproduzir o mapa público (sem dados privados)

```sh
node scripts/ai-engineering-from-scratch-alignment.mjs
node --test tests/ai-engineering-from-scratch-alignment.test.mjs
```
