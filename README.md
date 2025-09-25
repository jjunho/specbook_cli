# SpecBook CLI

Um protótipo de ferramenta de linha de comando (CLI) para escrita de livros baseada em especificações, inspirada no *Specification-Driven Development* (SDD).

## Filosofia

A escrita de uma longa narrativa é um projeto complexo. O SpecBook ajuda a gerenciar essa complexidade aplicando uma ideia do mundo do software: **nenhuma funcionalidade (capítulo) é escrita sem uma especificação (spec) clara.**

O fluxo de trabalho incentiva o autor a pensar e responder perguntas sobre personagens, cenários e arcos narrativos *antes* de escrever a prosa. Essas respostas são salvas como arquivos de texto estruturados (YAML), que se tornam a "fonte da verdade" para a história.

## Instalação e Desenvolvimento

Esta é a maneira recomendada de instalar o `specbook` para desenvolvimento, permitindo que suas alterações no código sejam refletidas imediatamente.

1.  **Clone o repositório (se aplicável) e navegue até a pasta `specbook_cli`**.

2.  **Crie e ative um ambiente virtual (`venv`):**
    Um `venv` é um ambiente Python isolado que previne conflitos de dependência.
    ```sh
    # Crie o ambiente
    python3 -m venv venv

    # Ative o ambiente (Linux/macOS)
    source venv/bin/activate
    ```

3.  **Instale o pacote em modo editável (`-e`):**
    Este comando instala as dependências e cria o link para o comando `specbook`, apontando diretamente para o seu código-fonte.
    ```sh
    pip install -e .
    ```

4.  **(Opcional, mas recomendado) Instale o PyYAML:**
    O `specbook` funciona sem ele, mas o `PyYAML` gera arquivos `.yaml` mais limpos e legíveis.
    ```sh
    pip install pyyaml
    ```

Após estes passos, o comando `specbook` estará disponível no seu terminal (enquanto o `venv` estiver ativo).

## Como Usar

(Esta seção permanece a mesma, detalhando os comandos `init`, `specify`, `status`, `review`, `generate`, etc.)

## Empacotamento e Distribuição

Se você quiser construir o `specbook` como um pacote distribuível (por exemplo, para instalar em outro lugar ou compartilhar), siga estes passos.

### Passo 1: Construir o Pacote

O projeto usa `setuptools` e `wheel` para criar os pacotes.

1.  **Garanta que as ferramentas de empacotamento estão atualizadas:**
    ```sh
    pip install --upgrade setuptools wheel
    ```

2.  **Execute o comando de construção na pasta `specbook_cli`:**
    ```sh
    python3 setup.py sdist bdist_wheel
    ```

    Isso criará uma pasta `dist/` contendo dois arquivos:
    -   Um arquivo `.tar.gz` (Source Distribution)
    -   Um arquivo `.whl` (Built Distribution / Wheel). Este é o formato preferido para instalação com `pip`.

### Passo 2: Instalar o Pacote Localmente

Para testar a instalação do pacote que você acabou de criar, você pode instalá-lo em um novo ambiente virtual.

1.  **Crie e ative um novo `venv` em outra pasta.**

2.  **Instale o pacote usando `pip` e o caminho para o arquivo `.whl`:**
    ```sh
    # Exemplo, o nome do arquivo pode variar
    pip install /caminho/para/specbook_cli/dist/specbook-0.1.0-py3-none-any.whl
    ```

3.  **Teste o comando:**
    Agora o comando `specbook` deve estar disponível, funcionando a partir do pacote instalado, e não mais diretamente do código-fonte.

## Testes

Para rodar a suíte de testes e garantir que tudo está funcionando como esperado, execute o seguinte comando na pasta `specbook_cli`:

```sh
python3 -m unittest test_specbook.py
```