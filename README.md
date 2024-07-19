# Lichess Visualizations ♟
Web-based chess dashboard composed of data visualizations sourced from [Lichess](https://database.nikonoel.fr/)' high elo chess games in January 2023.

Developed using Streamlit and Plotly.

---
<h3 align="center">
    ♟ Try it out here: <a href="https://chessinsight.streamlit.app">chessinsight on streamlit </a> ♟
</h3>

---

# Running the app locally

It is recommended to create a virtual environment first when installing the app locally.

### Clone GitHub repository
```
git clone https://github.com/jamesmostajo/checkmating-january.git
```

### Install requirements
```
pip install -r requirements.txt
```

### Run webapp
```
streamlit run app.py
```

### (Optional) Download additional data from GDrive
Google Drive link [here](https://drive.google.com/drive/folders/1eSEvHXplYsLy1jnb8LXypWg24gdbgnM6?usp=sharing).
These files are used for preprocessing data for the visualizations. These files are not being used by the app as it is being ran by Streamlit.