# Demo Anthropic Claude Sonnet SDK with Python

Demonstration of Anthropic Claude Sonnet SDK with Python.


## Create your Anthropic API key

Sign up for an Anthropic account at https://anthropic.com/

Create your Anthropic API key at https://console.anthropic.com/dashboard

Run:

```sh
export ANTHROPIC_API_KEY="your-api-key"
```


## Hello world

For our Python projects, we prefer to use the command `uv` to manage dependencies. You can use any way you wish.

Run:

```sh
uv sync
uv run demo.py
```

Output:

```stdout
[TextBlock(citations=None, text="Hello! It's nice to meet you. 
How can I help you today? I'm ready to assist with information, 
answer questions, or have a conversation about topics you're 
interested in.", type='text')]
```


## Aider AI pair programming (optional)

Aider lets you pair program with LLMs, to edit code in your local git repository. 

Run:

```sh
python -m pip install aider-install
aider-install
aider --model sonnet --api-key anthropic=your-api-key
```


## How we created this project

Run:

```sh
uv init
uv add anthropic
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/refs/heads/main/Python.gitignore
```


## Tracking

* Package: demo-anthropic-claude-sonnet-sdk-with-python
* Version: 1.0.0
* Created: 2025-02-25T04:59:23Z
* Updated: 2025-02-25T04:59:23Z
* License: Any of BSD, GPL, LGPL, MIT
* Contact: Joel Parker Henderson (joel@joelparkerhenderson.com)
