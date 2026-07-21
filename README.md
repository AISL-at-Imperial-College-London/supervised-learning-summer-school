## 1. Download the exercises

1. Open the course GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Locate the downloaded ZIP file.
5. Extract the ZIP file before continuing.

> Do not open or run the notebooks directly inside the ZIP file.

After extraction, the folder should contain:

```text
classification_students.ipynb
regression_students.ipynb
exercise_data.py
requirements.txt
```

Keep `exercise_data.py` in the same folder as both notebooks.

---

## 2. Open the complete folder in VS Code

1. Open Visual Studio Code.
2. Select **File → Open Folder**.
3. Select the extracted exercise folder.
4. Click **Select Folder**.

Do not use only **File → Open File**. Opening the complete folder helps VS Code locate:

- `requirements.txt`
- `exercise_data.py`
- The virtual environment created in the next step

If VS Code asks whether you trust the folder, select **Yes, I trust the authors** only if you downloaded it from the official course repository.

---

## 3. Create a virtual environment

A virtual environment is a private Python installation for this project. It prevents packages used in this exercise from interfering with packages used by other Python projects.

In VS Code:

1. Press `Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS.
2. Type:

   ```text
   Python: Create Environment
   ```

3. Select **Venv**.
4. Select the installed Python 3.12 interpreter.
5. If VS Code asks which dependency file to install, select:

   ```text
   requirements.txt
   ```

VS Code will create a folder named:

```text
.venv
```

The environment creation and package installation may take a few minutes.

---

## 4. Install the requirements

Even if VS Code appears to install the dependencies automatically, verify the installation explicitly.

Open a new terminal inside VS Code:

```text
Terminal → New Terminal
```

The beginning of the terminal prompt should contain:

```text
(.venv)
```

This indicates that the virtual environment is active.

First, upgrade the Python package installer:

```bash
python -m pip install --upgrade pip
```

Then install all packages listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

The `-r` option tells `pip` to read and install the packages listed in the requirements file.

Wait until the command finishes. A successful installation should not end with a red error message.

---

## 5. Verify the installation

Run the following command in the VS Code terminal:

```bash
python -c "import numpy, pandas, matplotlib, sklearn, ipykernel; print('Environment ready')"
```

The expected output is:

```text
Environment ready
```

This confirms that the required packages are installed in the virtual environment.

---

## 6. Connect the notebook to the virtual environment

The notebook must use the same virtual environment in which the packages were installed.

1. Open `regression_students.ipynb`.
2. Look at the upper-right corner of the notebook.
3. Click **Select Kernel**.
4. Select **Python Environments**.
5. Choose the interpreter containing `.venv`.

It may appear as:

```text
Python 3.12.x ('.venv')
```

Perform the same check when opening `classification_students.ipynb`.

The relationship between the files is:

```text
requirements.txt
      ↓ installs packages into
.venv
      ↓ selected as the notebook kernel
regression_students.ipynb
classification_students.ipynb
```

---

## 7. Test the notebooks

### Regression exercise

1. Open `regression_students.ipynb`.
2. Start with the first code cell.
3. Click the triangular **Run Cell** button.
4. Run the setup cells in order.

You should eventually see:

```text
Setup complete
```

The data-loading cell should print something similar to:

```text
Source: REAL CCPP data
```

### Classification exercise

1. Open `classification_students.ipynb`.
2. Confirm that `.venv` is selected as the kernel.
3. Run the setup cells in order.

The data-loading cell should report that it loaded the real AI4I data.

### Dataset information

No manual dataset download is required. The notebooks contain:

```python
PREFER_REAL_DATA = True
```

This tells `exercise_data.py` to download the published datasets automatically.

If downloading is unsuccessful, the notebooks use reproducible fallback datasets so that the exercises can still run.

---

## 8. Return to the exercises later

When returning to the project:

1. Open Visual Studio Code.
2. Select **File → Open Folder**.
3. Open the extracted exercise folder.
4. Open the required notebook.
5. Confirm that `.venv` is selected as the notebook kernel.
6. Continue running the notebook cells.

You normally do not need to reinstall the packages each time.

If the notebook cannot import a package, check the kernel before reinstalling anything:

```text
Select Kernel → Python Environments → .venv
```

### Closing the environment

You may close VS Code normally when finished. The `.venv` folder remains inside the project and will be available the next time you open it.

---

## Troubleshooting

### `ModuleNotFoundError` or “No module named ...”

The notebook is probably using the wrong Python kernel.

Select:

```text
Select Kernel → Python Environments → .venv
```

Then restart the notebook kernel and rerun the cells.

### `.venv` does not appear as a kernel

Open the VS Code terminal and run:

```bash
python -m pip install ipykernel
```

Close and reopen the notebook, then select the kernel again.

### The terminal does not show `(.venv)`

1. Open the VS Code Command Palette.
2. Select:

   ```text
   Python: Select Interpreter
   ```

3. Choose the interpreter inside `.venv`.
4. Close the existing terminal.
5. Open a new terminal.

### Python is not found

Close and reopen VS Code after installing Python.

On Windows, check:

```text
py -3.12 --version
```

If the command fails, reinstall Python and select **Add Python to PATH** during installation.

### The notebook reports a fallback dataset

Check your internet connection and rerun the data-loading cell.

The fallback dataset is reproducible and can still be used to complete the exercise, but the intended classroom workflow uses the real published dataset.

### A cell runs for a long time

The cross-validation and neural-network sections take longer than the initial setup cells.

Wait before restarting the kernel. If a cell appears frozen for several minutes, ask a teaching assistant for help.