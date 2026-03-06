# 🎬 Movie Recommender System

A content-based movie recommendation system built with **Machine Learning, Python, and Streamlit**.
Select a movie and the system recommends similar movies along with their posters.

---

## 🚀 Live Demo

Streamlit App:
https://ai-movie-recommender-07.streamlit.app

---

## ✨ Features

* Content-based movie recommendations
* Movie posters fetched using **TMDB API**
* Interactive UI built with **Streamlit**
* Deployed on **Streamlit Cloud**
* Large similarity model automatically downloaded from Google Drive

---

## 🧠 How It Works

1. The dataset contains movie metadata including:

   * genres
   * keywords
   * cast
   * crew
   * overview

2. These features are combined into a single **tags column**.

3. Text data is converted into vectors using:

   * **CountVectorizer**
   * **Cosine Similarity**

4. When a user selects a movie:

   * The system finds the most similar vectors
   * Returns the **top 5 recommended movies**
   * Fetches posters using **TMDB API**

---

## 🛠️ Tech Stack

* **Python**
* **Scikit-Learn**
* **Pandas**
* **Streamlit**
* **TMDB API**
* **gdown (for model download)**

---

## 📂 Project Structure

```
movie-recommender-system/
│
├── app.py
├── movies.pkl
├── similarity.pkl (downloaded automatically)
├── requirements.txt
├── README.md
│
├── datasets/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/rabbitx07/movie-recommender-system-ml.git
cd movie-recommender-system-ml
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 TMDB API Setup

Create a file:

```
.streamlit/secrets.toml
```

Add your TMDB API key:

```
TMDB_API_KEY = "your_api_key_here"
```

You can get a free API key from:

https://www.themoviedb.org/

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 📊 Dataset

Dataset used:

* TMDB 5000 Movie Dataset

Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---
# 🎬 Movie Recommender System

A content-based movie recommendation system built with **Machine Learning, Python, and Streamlit**.
Select a movie and the system recommends similar movies along with their posters.

---

## 🚀 Live Demo

Streamlit App:
https://ai-movie-recommender-07.streamlit.app

---

## ✨ Features

* Content-based movie recommendations
* Movie posters fetched using **TMDB API**
* Interactive UI built with **Streamlit**
* Deployed on **Streamlit Cloud**
* Large similarity model automatically downloaded from Google Drive

---

## 🧠 How It Works

1. The dataset contains movie metadata including:

   * genres
   * keywords
   * cast
   * crew
   * overview

2. These features are combined into a single **tags column**.

3. Text data is converted into vectors using:

   * **CountVectorizer**
   * **Cosine Similarity**

4. When a user selects a movie:

   * The system finds the most similar vectors
   * Returns the **top 5 recommended movies**
   * Fetches posters using **TMDB API**

---

## 🛠️ Tech Stack

* **Python**
* **Scikit-Learn**
* **Pandas**
* **Streamlit**
* **TMDB API**
* **gdown (for model download)**

---

## 📂 Project Structure

```
movie-recommender-system/
│
├── app.py
├── movies.pkl
├── similarity.pkl (downloaded automatically)
├── requirements.txt
├── README.md
│
├── datasets/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/rabbitx07/movie-recommender-system-ml.git
cd movie-recommender-system-ml
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 TMDB API Setup

Create a file:

```
.streamlit/secrets.toml
```

Add your TMDB API key:

```
TMDB_API_KEY = "your_api_key_here"
```

You can get a free API key from:

https://www.themoviedb.org/

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 📊 Dataset

Dataset used:

* TMDB 5000 Movie Dataset

Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 👩‍💻 Author

**Anshika**

BCA (AI & Data Science)
Graphic Era University

GitHub:
https://github.com/rabbitx07

---

## ⭐ If you like this project

Give the repository a **star** ⭐

