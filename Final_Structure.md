ScoutSpeak/
│
├── data/
│   ├── raw_cards/
│   ├── ocr_text/
│   └── processed/
│       ├── player_text.csv
│       └── labeled_players.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_results_analysis.ipynb
│
├── src/
│   ├── ocr_pipeline.py
│   ├── player_extractor.py
│   ├── hall_score.py
│   ├── word_clouds.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── predict_hof_probability.py
│
├── models/
│   ├── hof_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── results/
│   ├── player_master.csv
│   ├── hof_wordcloud.png
│   ├── bust_wordcloud.png
│   ├── scores.csv
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│   └── hof_predictions.csv
│
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
