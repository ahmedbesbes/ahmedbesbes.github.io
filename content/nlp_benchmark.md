Title: Overview and benchmark of traditional and deep learning models in text classification
Date: 2018-06-12 10:00
Category: Deep Learning
Tags: NLP, CNN, RNN, GRU, transfer learning, deep learning, keras, neural networks, Twitter, GloVe, Bag of words, word ngrams, character ngrams
Authors: Ahmed Besbes
Summary: This article is an extension of a <a href="https://ahmedbesbes.com/sentiment-analysis-on-twitter-using-word2vec-and-keras.html">previous one</a> I wrote when I was experimenting sentiment analysis on twitter data. Back in the time, I explored a simple model: a two-layer feed-forward neural network trained on keras. The input tweets were represented as document vectors resulting from a weighted average of the embeddings of the words composing the tweet. The embedding I used was a word2vec model I trained from scratch on the corpus using gensim. The task was a binary classification and I was able with this setting to achieve 79% accuracy. </br> The goal of this post is to explore other NLP models trained on the same dataset and then benchmark their respective performance on a given test set. We'll go through different models: from simple ones relying on a bag-of-word representation to a heavy machinery deploying convolutional/recurrent networks: We'll see if we'll score more than 79% accuracy! </br> Let's investigate ! </br></br><a href="https://ahmedbesbes.com/overview-and-comparison-of-tranditional-and-deep-learning-models-in-text-classification.html"><img src="./images/article_5/investigate.jpg"></img></a>

{% notebook article_5.ipynb cells[:1] language[python] %}

<!-- <img src="https://ahmedbesbes.com/images/article_5/cover_resized.png" class="center"></img> -->

![energy]({attach}images/article_5/cover_resized.png)

{% notebook article_5.ipynb cells[2:] language[python] %}