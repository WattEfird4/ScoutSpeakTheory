SpeakScout/
│
├── data/
│   ├── raw_cards/
│   ├── ocr_text/
│   └── processed/
│       ├── player_master.csv
│       └── scouting_reports.csv
│
├── models/
│   ├── hall_score_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_ocr_validation.ipynb
│   ├── 03_hall_score_analysis.ipynb
│   └── 04_ml_prototype.ipynb
│
├── results/
│   ├── scores.csv
│   ├── hof_wordcloud.png
│   ├── bust_wordcloud.png
│   ├── feature_importance.png
│   └── hof_predictions.csv
│
├── src/
│   ├── pybaseball_loader.py
│   ├── card_catalog.py
│   ├── ocr_pipeline.py
│   ├── player_matcher.py
│   ├── scouting_cleaner.py
│   ├── hall_score.py
│   ├── feature_engineering.py
│   ├── train_classifier.py
│   ├── word_clouds.py
│   └── run_pipeline.py
│
├── requirements.txt
└── README.md
