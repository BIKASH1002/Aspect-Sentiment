# Aspect-Based Sentiment Analysis with MongoDB

Customer reviews are a treasure trove of insights, revealing how users perceive a product and what improvements they desire. Understanding customer sentiment is crucial for driving product improvements and enhancing customer satisfaction. Businesses often face the challenge of deciphering vast amounts of feedback, where reviews can focus on multiple aspects with varied sentiments. Extracting actionable insights from this unstructured data requires advanced tools that can analyze text, identify key product aspects and determine sentiment accurately. This is where natural language processing (NLP) and machine learning converge, enabling businesses to unlock the hidden value in customer reviews. By combining NLP, sentiment analysis and robust data storage, this project empowers organizations to analyze customer feedback and make informed decisions.

## Table of Contents

- [Overview](#overview)

- [Setup](#setup)

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
