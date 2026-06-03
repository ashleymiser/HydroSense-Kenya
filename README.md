# HydroSense-Kenya

Smart irrigation decision support system for a Nairobi demonstration farm.
Built for ICS 2207 Scientific Computing capstone project.

## What this project does

Uses daily weather data and soil sensor readings from three farm zones to:
- Estimate daily evapotranspiration
- Model soil moisture using the discrete water balance equation
- Simulate future soil moisture using Euler and Runge-Kutta methods
- Quantify rainfall uncertainty using Monte Carlo simulation
- Recommend an optimized irrigation schedule that minimizes water use while
  keeping crops above the minimum moisture threshold

## Project structure

```
HydroSense-Kenya/
├── data/
│   ├── raw/                          # original datasets from project brief
│   └── processed/                    # cleaned dataset
├── notebooks/                        # six level notebooks
├── src/                              # reusable Python modules
├── tests/                            # pytest test files
├── reports/                          # plots and final report
├── AI_USE_LOG.md
├── README.md
└── requirements.txt
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the notebooks

Run notebooks in order from Level 1 to Level 6:

```bash
jupyter notebook
```

Open each notebook in the `notebooks/` folder and run all cells top to bottom.

## Running the tests

```bash
pytest tests/ -v
```

## Dataset source

All datasets are synthetic and included in `data/raw/`. They were provided in
the project brief appendices (Appendix A, B, and C). Additional live weather
data can be accessed via the JHub Africa Conduit API at https://conduit.jhubafrica.com/

## Group members

- Ashley Miser
