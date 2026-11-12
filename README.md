# git-deliverables
Obligatory deliverables in INF201
Deliverable 3 revolves around constructing a rpg game simulator that includes methods and classes for dicerolls, weapons for characters, and simulating battles between different subclasses.

Repository: https://github.com/Trygve-Refsnes/git-deliverables

The simulator requires Python 3.10 or later. The pinned notebook/export
environment was created with Python 3.14; use that version to reproduce it.
Create a separate environment for this deliverable:

```powershell
python -m venv venv_d3
.\venv_d3\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name venv_d3 --display-name "Deliverable 3"
```

Open `deliverable3_notebook.ipynb` in Jupyter or VS Code and select that kernel.
The notebook presents every class and simulates Warrior/Mage battles with and
without weapons. The simulator itself uses only the Python standard library.

Validation and PDF export:

```powershell
python -m unittest discover -s tests -v
python export_notebook.py
```

The exporter executes the notebook's plain Python cells in order, updates their
saved outputs and writes `deliverable3_notebook.pdf` with the same explanations,
code and output. ReportLab is required only for this export.

The notebook includes the GenAI disclosure for this session. Review it and add
any earlier AI use before submission. `SUBMISSION.md` contains the remaining
hand-in checklist and a five-minute video outline. Both group members must
contribute to the recording.
