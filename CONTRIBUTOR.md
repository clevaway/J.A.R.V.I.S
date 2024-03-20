# Contributor's Guide

Welcome to the Jarvis project! We appreciate your interest in contributing. This guide provides information on how to contribute to the project.

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork to your local machine.
3. Create a new branch for your work.
4. Make your changes in your branch.
5. Push your changes to your fork.
6. Submit a pull request from your fork to the main repository.

## Code of Conduct

We expect all contributors to follow our Code of Conduct. Please review it before you start contributing.

## How to Contribute

You can contribute in several ways:

- Submitting a pull request for bug fixes or new features.
- Improving documentation.
- Reporting issues.
- Suggesting new features or improvements.
- Improving the dataset

## Deployment

We use [llama.cpp](https://github.com/ggerganov/llama.cpp) to convert and quantize the model. The deployment of the model is done using [Ollama](https://github.com/ollama/ollama). If you make changes that affect the model, you may need to quantize it and run it locally before pushing you code. Please refer to the Ollama documentation for more information.

## Setup local

1. Clone the this repo
2. Make sure you have the python dep needed, we useing `pythin 3.10.13` for this project
3. That's it, you are in.

## Model convertion and quantization

First, clone the ollama/ollama repo:

```bash
git clone https://github.com/ollama/ollama.git
cd ollama
```

after cloning this repo you will then fetch its llama.cpp submodule:

  ```bash
git submodule init
git submodule update llm/llama.cpp
  ```

  Next, install the Python dependencies:

  ```bash
python3 -m venv llm/llama.cpp/.venv
source llm/llama.cpp/.venv/bin/activate
pip install -r llm/llama.cpp/requirements.txt

  ```

  you can use whatever python version manager you want, we use anaconda.

  then build the quantize tool:

  ```bash
  make -C llm/llama.cpp quantize
  ```

### Convert the model
>
> Note: some model architectures require using specific convert scripts. For example, Qwen models require running `convert-hf-to-gguf.py` instead of `convert.py`

```bash
python llm/llama.cpp/convert.py ./model --outtype f16 --outfile converted.bin
```

### Quantize the model

```bash
llm/llama.cpp/quantize converted.bin quantized.bin q4_0
```

## Questions

If you have any questions, please open an issue and we'll be happy to help.

Lets bring Jarvis to life together with today's tech:)
