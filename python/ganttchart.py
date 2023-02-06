import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job 0", Start='2023-01-15', Finish='2023-01-29', Resource="PREPARATION"),    
    dict(Task="Job A", Start='2023-01-15', Finish='2023-01-22', Resource="Prep. and Outstanding Analysis:"),
    dict(Task="JobA", Start='2023-01-22', Finish='2023-01-29', Resource="Update Literature Review"),
    dict(Task="Job 1", Start='2023-01-29', Finish='2023-02-05', Resource="PHASE 1"),
    dict(Task="JobA", Start='2023-01-29', Finish='2023-02-05', Resource="Data Gathering and Prep."),
    dict(Task="Job 2", Start='2023-02-05', Finish='2023-03-19', Resource="PHASE 2"),
    dict(Task="JobA", Start='2023-02-05', Finish='2023-02-12', Resource="Initial Coding"),
    dict(Task="JobA", Start='2023-02-12', Finish='2023-02-26', Resource="Evaluation of ML Models"),
    dict(Task="JobA", Start='2023-02-26', Finish='2023-03-04', Resource="Coding and additional work"),
    dict(Task="JobA", Start='2023-03-04', Finish='2023-03-11', Resource="Unavailable"),
    dict(Task="JobA", Start='2023-03-11', Finish='2023-03-19', Resource="Train Model on test election data"),
    dict(Task="Job 3", Start='2023-03-19', Finish='2023-05-01', Resource="PHASE 3"),
    dict(Task="JobA", Start='2023-03-19', Finish='2023-03-26', Resource="Apply Trained Model"),# to target election to generate “signed” ballots"),
    dict(Task="JobA", Start='2023-03-27', Finish='2023-04-02', Resource="Evaluate performance"),# “uniqueness” of generated “signed” ballots"),
    dict(Task="JobA", Start='2023-04-02', Finish='2023-04-09', Resource="Results and Conclusions"),
    dict(Task="JobA", Start='2023-04-09', Finish='2023-04-23', Resource="Finish Writing Dissertation"),
    dict(Task="JobA", Start='2023-04-23', Finish='2023-05-01', Resource="Proof-reading Final Dissertation")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
fig.show()