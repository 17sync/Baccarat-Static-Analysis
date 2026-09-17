# Baccarat

A Python implementation of the **Baccarat (Punto Banco)** card game, originally developed as a personal learning project.

This repository is a **cloned copy of an existing open-source project** being used for a **Static Code Quality Analysis assignment** in Software Quality Engineering.

The original project's core functionality and design are preserved as the baseline for analysis. Any changes made in this repository are part of the static analysis, refactoring, and quality improvement process.

> **Note:** This repository is not the original work. The original project and its author are credited below.

## Static Analysis

The project uses two main branches to separate the original implementation from the analysis and modification work:

### `main`

The `main` branch preserves the **original project as the baseline**.

No analysis-related modifications are made to the original implementation on this branch. It provides a fixed reference point against which the results of static analysis and subsequent improvements can be compared.

### `static-analysis`

The `static-analysis` branch is used for the **actual analysis and modification process**.

This branch contains the changes made as part of the assignment, including:

* Static code quality analysis
* Identification of code quality issues
* Refactoring where appropriate
* Improvements to readability and maintainability
* Verification of changes against the original baseline

Keeping the two branches separate makes it possible to compare the modified code with the original implementation and preserve the original project as an identifiable baseline.

## Project Structure

```text
baccarat/
├── baccarat-cli.py
├── baccarat-sim.py
├── cards.py
├── hands.py
├── players.py
└── rules.py
```

## Running the Game

### Baccarat CLI

Run the command-line version with:

```bash
python3 baccarat-cli.py
```

### Baccarat Simulation

Run the simulation with:

```bash
python3 baccarat-sim.py [-h] [-s SHOES] [-d DECKS]
```

## Credits

This project is based on the original **Baccarat** repository by **rjsilvestre**.

**Original Repository:**
https://github.com/rjsilvestre/baccarat

**Original Author:**
[rjsilvestre](https://github.com/rjsilvestre)

All original credit for the underlying project and its source code belongs to the original author. This repository is intended for **educational and static analysis purposes** and should not be presented as the original work of this repository's maintainer.

## License

Please refer to the original repository for the applicable license and usage terms:
https://github.com/rjsilvestre/baccarat
