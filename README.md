# Supervised Learning After-Class Exercises

This folder contains two independent exercises. Allow about 90 minutes for each one.

- `regression_students.ipynb`: predict combined-cycle power-plant output.
- `classification_students.ipynb`: design a predictive-maintenance alarm.
- `exercise_data.py`: dataset loaders and reproducible offline fallbacks.
- `MODEL_GUIDE.md`: a short comparison of the model families used in the exercises.

## Before you start

You need Python 3.10 or later. Keep `exercise_data.py` in the same folder as both notebooks.

For a local installation, open a terminal in this folder and run:

```text
python -m pip install -r requirements.txt
```

If you do not already have a notebook environment through Jupyter or VS Code, install and start JupyterLab with:

```text
python -m pip install jupyterlab
python -m jupyter lab
```

Open one notebook and work through it from top to bottom. Complete the required sections before attempting the optional extensions.

If you use Google Colab, upload the notebook and `exercise_data.py` to the same Colab session. If you see `ModuleNotFoundError: exercise_data`, check that both files appear in the Colab Files panel, then restart the runtime and run the setup cells again.

## How to work through the notebooks

1. Read the engineering question before writing code.
2. Replace each `...` in the required sections.
3. Run the cell and check the assertion below it.
4. Use a collapsed hint only after making a first attempt.
5. Write the short interpretation before moving on.
6. Keep the final test set untouched until the notebook explicitly opens it.

The exercises are designed to assess decisions as well as code. A model score without units, a baseline, or an operational interpretation is not a complete answer.

## Datasets

The regression exercise uses the [UCI Combined Cycle Power Plant dataset](https://archive.ics.uci.edu/dataset/294/combined%2Bcycle%2Bpower%2Bplant), containing real full-load plant observations.

The classification exercise uses the [UCI AI4I 2020 Predictive Maintenance dataset](https://archive.ics.uci.edu/dataset/601/ai4i), a published synthetic, physics-based benchmark. It is useful for studying known failure rules, but it is not a substitute for validation on time-separated data from a real asset fleet.

Each loader first attempts to download the published dataset. If the download is unavailable, `exercise_data.py` creates a seeded fallback with the same columns and teaching behaviour. The notebook prints the source it used.

## Expected submission

Submit the two completed notebooks with all required cells run in order. Include the written answers and the final recommendation in each notebook. Optional extensions are not required unless your instructor assigns them.
