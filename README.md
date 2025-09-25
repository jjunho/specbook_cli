# SpecBook CLI

**SpecBook** é uma ferramenta de linha de comando (CLI) para escrita de livros e narrativas longas baseada em especificações, inspirada na filosofia do *Specification-Driven Development* (SDD) do mundo da engenharia de software.

## Filosofia

A escrita de uma longa narrativa é um projeto complexo. O SpecBook ajuda a gerenciar essa complexidade aplicando uma ideia fundamental: **nenhuma parte da história (capítulo, cena) é escrita sem uma especificação (spec) clara e definida.**

O fluxo de trabalho incentiva o autor a pensar e responder perguntas sobre personagens, cenários, arcos narrativos e a estrutura do mundo *antes* de escrever a prosa. Essas respostas são salvas como arquivos de texto estruturados (YAML), que se tornam a "fonte da verdade" e o esqueleto para a história.

## Instalação

Você pode instalar o SpecBook de duas maneiras: como um usuário final ou como um desenvolvedor.

### 1. Instalação Padrão (Ambiente Virtual)

Esta é a maneira recomendada para usar a ferramenta de forma isolada e segura.

1.  **Crie e ative um ambiente virtual (`venv`):**
    ```sh
    # Navegue até uma pasta de sua escolha e crie o ambiente
    python3 -m venv meu_ambiente_de_escrita
    
    # Ative o ambiente (Linux/macOS)
    source meu_ambiente_de_escrita/bin/activate
    ```

2.  **Instale o pacote:**
    Após baixar o pacote (por exemplo, o arquivo `.whl` da seção de [Releases](https://github.com/jjunho/specbook_cli/releases)), instale-o com o `pip`:
    ```sh
    # Instale a partir do arquivo wheel
    pip install /caminho/para/specbook-0.1.0-py3-none-any.whl
    ```
    O comando `specbook` estará disponível enquanto o ambiente virtual estiver ativo.

### 2. Instalação para Desenvolvimento

Se você deseja modificar ou contribuir com o projeto, instale-o em modo "editável".

1.  **Clone o repositório:**
    ```sh
    git clone https://github.com/jjunho/specbook_cli.git
    cd specbook_cli
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale em modo editável (`-e`):**
    Este comando instala as dependências e cria um link para o comando `specbook` que aponta diretamente para o seu código-fonte. Qualquer alteração que você fizer será refletida imediatamente.
    ```sh
    pip install -e .
    ```

## Como Usar

O fluxo de trabalho do `specbook` é dividido em comandos que representam as fases da escrita.

### `specbook init`

Cria a estrutura de pastas para um novo projeto de livro.

-   **Uso:** `specbook init <nome_da_pasta_do_projeto>`
-   **Exemplo:**
    ```sh
    specbook init ./meu-livro-incrivel
    ```
    Isso criará a pasta `meu-livro-incrivel/` com todos os subdiretórios necessários (`specs`, `drafts`, `plans`, etc.).

### `specbook specify`

O coração da ferramenta. Usado para criar os arquivos de especificação.

-   **`specbook specify seed`**: Cria o arquivo `seed.yml` com a ideia central, gênero e temas do livro.
    ```sh
    specbook specify seed --project ./meu-livro-incrivel
    ```
-   **`specbook specify character`**: Inicia um prompt interativo para criar um novo personagem.
    ```sh
    specbook specify character --project ./meu-livro-incrivel
    ```
-   **`specbook specify setting`**: Inicia um prompt interativo para criar um novo cenário.
    ```sh
    specbook specify setting --project ./meu-livro-incrivel
    ```

### `specbook generate`

Gera arquivos de rascunho baseados nas especificações existentes.

-   **`specbook generate scene`**: Gera um arquivo de cena em Markdown, puxando informações de um personagem e um cenário para servirem de guia.
    ```sh
    # O comando iniciará um menu para você escolher o personagem e o cenário
    specbook generate scene --project ./meu-livro-incrivel
    
    # Ou de forma não-interativa
    specbook generate scene --project ./meu-livro-incrivel --character "Nome do Personagem" --setting "Nome do Cenário"
    ```

### Outros Comandos (Resumo)

-   **`specbook status`**: Mostra um resumo do estado atual do projeto (quantas specs, rascunhos, etc.).
-   **`specbook plan`**: Gerencia os arquivos de planejamento de alto nível.
-   **`specbook tasks`**: Gerencia a lista de tarefas de escrita.
-   **`specbook draft`**: Cria novos arquivos de rascunho.
-   **`specbook review`**: Gerencia os ciclos de revisão da história.

## Empacotamento e Distribuição (Para Mantenedores)

Para criar os pacotes distribuíveis do projeto:

1.  **Garanta que as ferramentas de empacotamento estão atualizadas:**
    ```sh
    pip install --upgrade setuptools wheel
    ```

2.  **Execute o comando de construção na raiz do projeto:**
    ```sh
    python3 setup.py sdist bdist_wheel
    ```
    Isso criará uma pasta `dist/` com os arquivos `.tar.gz` (Source Distribution) e `.whl` (Wheel), prontos para serem distribuídos ou publicados.

## Testes

Para rodar a suíte de testes e garantir que tudo está funcionando como esperado:

```sh
python3 -m unittest test_specbook.py
```

## Licença

Este projeto é distribuído sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.
