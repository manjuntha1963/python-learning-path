# Contributing

Thank you for improving this learning path.

## Good contributions

- Correct inaccurate explanations or code.
- Add beginner-friendly examples and practice tasks.
- Add tests or runnable examples.
- Update links and clearly label free, open-source, and paid tools.
- Explain security, privacy, cost, and licensing implications.

## Before opening a pull request

1. Create a branch from the latest `content-development` branch.
2. Keep one topic or fix per pull request when practical.
3. Use clear headings and explain why each example is useful.
4. Test Python snippets locally.
5. Do not commit API keys, credentials, private data, generated files, or large model files.
6. Check links and preserve the learning order.

Run basic checks:

```bash
python -m compileall .
python -m pytest
```

If a dependency is optional, say so in the module README rather than making every learner install it.

## Documentation style

Prefer:

- plain English before code;
- small, runnable examples;
- comments that explain purpose rather than every obvious syntax detail;
- a common mistake, error, cause, and fix where useful;
- practice tasks without immediately giving away the answer;
- current links to official documentation.

## Pull requests

Describe the change, modules affected, commands tested, and any paid services or credentials required. Contributions are reviewed for correctness, clarity, safety, and maintainability.
