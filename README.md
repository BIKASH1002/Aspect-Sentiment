# Aspect-Based Sentiment Analysis with MongoDB

Customer reviews are a treasure trove of insights, revealing how users perceive a product and what improvements they desire. Understanding customer sentiment is crucial for driving product improvements and enhancing customer satisfaction. Businesses often face the challenge of deciphering vast amounts of feedback, where reviews can focus on multiple aspects with varied sentiments. Extracting actionable insights from this unstructured data requires advanced tools that can analyze text, identify key product aspects and determine sentiment accurately. This is where natural language processing (NLP) and machine learning converge, enabling businesses to unlock the hidden value in customer reviews. By combining NLP, sentiment analysis and robust data storage, this project empowers organizations to analyze customer feedback and make informed decisions.

## Table of Contents

- [Overview](#overview)

- [Setup](#setup)

- [Dataset](#dataset)

- [Features](#features)

- [Procedure](#procedure)

- [Workflow](#workflow)

- [Database Interface](#database-interface)

- [Conclusion](#conclusion)


## Overview

The Aspect-Based Sentiment Analysis is designed to extract specific product aspects from customer reviews and analyze their associated sentiments. Using a subset of the **Amazon Reviews dataset** from Kaggle, this project applies NLP techniques to parse and analyze text. With scalable MongoDB integration, the processed data is stored efficiently, enabling seamless querying and visualization. The machine learning component, powered by the **Stochastic Gradient Descent Classifier (SGDC)**, delivers an accuracy of 80%, ensuring reliable sentiment predictions. This project provides a pipeline for businesses to gain actionable insights from customer reviews across diverse product categories.

## Setup

- **Visual Studio Code:** for developement

- **MongoDB Compass:** for data storage

- **NLP packages:** for pre-procesing and sentiment analysis

## Dataset

Used a subset of the Amazon Reviews dataset from Kaggle, which contains millions of customer reviews spanning various product categories. For this project, I processed a chunk of the dataset to focus on textual reviews and associated scores. Each review in the dataset includes:

- **Text:** The written customer feedback.

- **Score:** A numerical rating (e.g., 1 to 5).

- **Sentiment:** Derived from the score (positive for scores >3, negative for scores ≤3).

This dataset serves as the foundation for extracting aspects and analyzing their sentiments. For complete dataset access [click here](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)

## Features

- **Aspect Extraction:** Identify product-related aspects (e.g., "battery life," "build quality") using NLP models.

- **Sentiment Analysis:** Perform sentiment classification (positive, negative) on extracted aspects.

- **SGDC Classifier Integration:** Utilize the Stochastic Gradient Descent Classifier to achieve 80% accuracy in sentiment classification.

- **Scalable Database Storage:** Store processed reviews and aspects in MongoDB for easy access.

- **User-Friendly Visualization:** Leverage MongoDB Compass for schema and document exploration.

## Procedure

**1. Data Preprocessing:**

- Clean and tokenize the review text.

- Remove stop words and irrelevant phrases.

**2. Aspect Extraction:**

- Use SpaCy and dependency parsing to identify noun chunks and meaningful phrases.

- Apply filters to retain product-relevant terms.

**3. Sentiment Classification:**

- Use the SGDC classifier with a custom pipeline for sentiment prediction.

- Achieve 80% accuracy using test data.

**4. Data Storage:**

- Store the processed data (reviews, aspects, and sentiments) in MongoDB.

**5. Visualization:**

Use MongoDB Compass to explore stored documents and validate the schema.

## Workflow

## Database Interface

The project uses MongoDB Compass for visualizing and managing stored data. Below are screenshots showcasing the database schema and sample documents.

**1. Database Overview**

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/5e5cbcc3-4a86-4095-b33e-cdf52793a576" alt = "DB overview" width = 50%>
</div>

**2. Document with updated sentiments**

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/085669a4-ba8e-4a2e-b2a2-916de4ed1bc0" alt = "Aspect sentiment" width = 50%>
</div>

**3. Schema Visualization**

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/a3b7931a-c741-4cf7-8c61-98b82e52b495" alt = "Aspect sentiment" width = 50%>
</div>

## Conclusion

This project bridges the gap between unstructured customer feedback and actionable insights using NLP and machine learning. The Stochastic Gradient Descent Classifier ensures accurate sentiment predictions, while MongoDB provides scalable storage for extensive review datasets. By enabling businesses to identify key product aspects and associated sentiments, this project fosters informed decision-making and customer-centric improvements. For future work we can integrate advanced sentiment models like BERT or other transformers for higher accuracy.

## Credits

- Kaggle: for dataset
