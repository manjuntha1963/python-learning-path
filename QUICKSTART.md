# Quick Start

## Requirements

- Python 3.10 or newer recommended
- Git
- A code editor
- Docker is optional for deployment modules

Check Python:

```bash
python --version
```

## Download the course

```bash
git clone https://github.com/manjuntha1963/python-learning-path.git
cd python-learning-path
git checkout content-development
```

You can also download a ZIP from the repository's **Code → Download ZIP** menu:

https://github.com/manjuntha1963/python-learning-path/archive/refs/heads/content-development.zip

## Create an isolated environment

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Install only what you need. For the early modules:

```bash
python -m pip install numpy pandas scikit-learn pytest
```

For web and capstone experiments, add:

```bash
python -m pip install fastapi uvicorn python-dotenv
```

Provider SDKs and cloud services are optional. Review current vendor pricing before using paid APIs.

## How to practise

1. Open a module README.
2. Copy an example into a scratch file or notebook.
3. Run it with `python your_file.py`.
4. Change one value and predict the result.
5. Complete the practice task without copying the example.
6. Add a test for your solution.

Free places to practise include:

- [Python interpreter](https://www.python.org/shell/)
- [Google Colab](https://colab.research.google.com/)
- [Jupyter](https://jupyter.org/try)
- [Exercism](https://exercism.org/tracks/python)
- [HackerRank](https://www.hackerrank.com/domains/python)
- [LeetCode](https://leetcode.com/)
- [Kaggle Learn](https://www.kaggle.com/learn)

## Run included examples

Every module has a small `examples/` program. For example:

```bash
python 01-basic-python/examples/hello.py
python 03-artificial-intelligence-and-machine-learning/examples/linear_model.py
python 10-real-world-python-ai-capstone-project/examples/qa_service.py
```

Some examples use only the Python standard library. Install the module dependencies when an import error identifies an optional library.

## Safe API use

```bash
cp .env.example .env  # if a module provides this template
```

Keep `.env` local, never paste keys into source code, and begin with free/local models or simulated responses. Set spending limits and use test data only.

## Suggested pace

- Weeks 1–2: Modules 01–02
- Weeks 3–4: Module 03
- Weeks 5–6: Modules 04 and 06–07
- Weeks 7–8: Modules 05 and 08–09
- Weeks 9–10: Module 10
- Week 11: Module 11
- Week 12: Module 12

## Troubleshooting

- `python` is not found: install Python and ensure it is on your PATH.
- `ModuleNotFoundError`: activate `.venv` and install the named package.
- Permission errors: use a virtual environment; do not install globally unless necessary.
- API errors: verify the key, endpoint, quota, model name, and current provider documentation.
- Docker errors: confirm Docker Desktop or the Docker daemon is running.
- Unexpected output: print intermediate values and compare them with the module's explanation.
