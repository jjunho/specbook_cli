# SpecBook CLI

Um protótipo de ferramenta de linha de comando (CLI) para escrita de livros baseada em especificações, inspirada no *Specification-Driven Development* (SDD).

## Filosofia

A escrita de uma longa narrativa é um projeto complexo. O SpecBook ajuda a gerenciar essa complexidade aplicando uma ideia do mundo do software: **nenhuma funcionalidade (capítulo) é escrita sem uma especificação (spec) clara.**

O fluxo de trabalho incentiva o autor a pensar e responder perguntas sobre personagens, cenários e arcos narrativos *antes* de escrever a prosa. Essas respostas são salvas como arquivos de texto estruturados (YAML), que se tornam a "fonte da verdade" para a história.

## Instalação

Recomenda-se o uso de um ambiente virtual do Python.

1.  **Clone o repositório (se aplicável) e navegue até a pasta `specbook_cli`**.

2.  **Crie e ative um ambiente virtual:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale o pacote em modo editável:**
    Isso instalará as dependências e o comando `specbook` no seu ambiente.
    ```sh
    pip install -e .
    ```

4.  **(Opcional, mas recomendado) Instale o PyYAML para melhor formatação:**
    ```sh
    pip install pyyaml
    ```

## Como Usar

O `specbook` funciona com uma série de comandos. A maioria deles exige o argumento `--project` para saber em qual projeto você está trabalhando.

---

### `init`

Inicializa uma nova estrutura de projeto de livro.

-   **Comando:** `specbook init [nome_do_projeto]`
-   **Exemplo:**
    ```sh
    specbook init meu_livro_de_fantasia
    ```
    Isso cria uma pasta `meu_livro_de_fantasia/` com todos os subdiretórios necessários (`specs/`, `drafts/`, `plans/`, etc.).

---

### `specify`

Cria ou atualiza as especificações (specs) do seu mundo. Este comando tem subcomandos.

-   **`seed`**: Define a ideia central, gênero e temas do livro.
    -   **Comando:** `specbook specify seed --project [projeto]`
    -   **Exemplo:**
        ```sh
        specbook specify seed --project meu_livro_de_fantasia
        ```
        O sistema fará perguntas interativas sobre a sua ideia.

-   **`character`**: Cria uma nova especificação de personagem.
    -   **Comando:** `specbook specify character --project [projeto]`
    -   **Exemplo:**
        ```sh
        specbook specify character --project meu_livro_de_fantasia
        ```
        O sistema fará perguntas sobre nome, idade, papel, desejos, medos, etc.

-   **`setting`**: Cria uma nova especificação de cenário ou local.
    -   **Comando:** `specbook specify setting --project [projeto]`
    -   **Exemplo:**
        ```sh
        specbook specify setting --project meu_livro_de_fantasia
        ```

---

### `status`

Exibe um painel com o status atual do projeto.

-   **Comando:** `specbook status --project [projeto]`
-   **Exemplo:**
    ```sh
    specbook status --project meu_livro_de_fantasia
    ```
    A saída mostrará a contagem de specs, o progresso dos rascunhos (contagem de palavras) e as tarefas pendentes.

---

### `review`

Roda uma verificação de consistência avançada no projeto.

-   **Comando:** `specbook review --project [projeto]`
-   **Exemplo:**
    ```sh
    specbook review --project meu_livro_de_fantasia
    ```
    Ele gera um relatório em `reviews/consistency_report.md` que aponta:
    -   Campos essenciais faltando nos specs de personagens.
    -   Referências a personagens ou locais nos rascunhos que não existem nos specs.
    -   Uma pontuação de consistência geral para o projeto.

---

### `generate`

Ajuda a vencer a página em branco gerando esqueletos de escrita.

-   **`scene`**: Gera um arquivo de cena com um prompt personalizado.
    -   **Comando:** `specbook generate scene --project [projeto]`
    -   **Exemplo:**
        ```sh
        specbook generate scene --project meu_livro_de_fantasia
        ```
        O sistema listará os personagens e cenários existentes para você escolher e criará um novo arquivo em `fragments/scenes/`.

---

### Outros Comandos

-   **`plan`**: Atualiza o `plans/plan.md` com a ideia do `seed.yaml`.
    -   `specbook plan --project [projeto]`
-   **`tasks`**: Gera uma lista de tarefas padrão em `tasks/tasks.md`.
    -   `specbook tasks --project [projeto]`
-   **`draft`**: Cria um novo arquivo de rascunho para um capítulo.
    -   `specbook draft [numero_capitulo] --project [projeto]`

## Workflow de Exemplo

1.  **Inicie seu projeto:**
    ```sh
    specbook init cronicas_de_aethel
    ```

2.  **Defina a ideia central:**
    ```sh
    specbook specify seed --project cronicas_de_aethel
    ```

3.  **Crie seu protagonista e um cenário:**
    ```sh
    specbook specify character --project cronicas_de_aethel
    # (Responda as perguntas para criar 'Luna')

    specbook specify setting --project cronicas_de_aethel
    # (Responda as perguntas para criar 'Aethelgard')
    ```

4.  **Verifique o status do projeto:**
    ```sh
    specbook status --project cronicas_de_aethel
    ```

5.  **Gere uma cena para começar a escrever:**
    ```sh
    specbook generate scene --project cronicas_de_aethel
    # (Escolha 'Luna' e 'Aethelgard' na lista)
    ```

6.  **Escreva o primeiro capítulo:**
    ```sh
    specbook draft 1 --project cronicas_de_aethel
    # (Abra o arquivo drafts/01_chapter.md e escreva, referenciando os specs)
    # Ex: **Influências de spec**: personagens=[Luna], locais=[Aethelgard]
    ```

7.  **Revise a consistência:**
    ```sh
    specbook review --project cronicas_de_aethel
    # (Verifique o relatório em reviews/consistency_report.md)
    ```

## Desenvolvimento

Para rodar a suíte de testes e garantir que tudo está funcionando, execute:

```sh
python3 -m unittest test_specbook.py
```
