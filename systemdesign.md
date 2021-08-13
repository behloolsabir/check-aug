# System Design

## Model Development

### Data Prep 
We can use data augmentation method used in the coding assignment to generate compliance positive and compliance negative cases. We can use other sentences from any chat data for Non-compliance data (it might bring in some noise of compliance data but if enough data is used it wont be a problem)
### Model
Keyword based methods have its challenges. We can use word embeddings to avoid most of those problems. We can use simpler techniques such as GloVe/FastText/Word2vec. These can be limiting if very long sentences are used and also it won't be able to capture double negations etc. 

We can use \*BERT\* models which can iron out all the problems and is also easier to build a feedback loop. 

Using the word embeddings we can create the input vector for these sentences for the model. Using the data discussed above with labels we can create a classification model.

We can design two styles of model: 
1. Two level of classification. One which classifies whether compliance topic is talked about and another which classifies it into positive and negative sentiment of it. 
2. Three class classification. Non-compliance topic, positive compliance and negative compliance. 

## User Feedback System
User feedback can be collected at two levels. Compliance discussed or no and sentiment positive or negative. 
This feedback can then be used to fine-tune our models. 

We can create model monitoring system which can capture data drift and model drift. 
On crossing certain threshold of data drift, we can do the fine-tune of our models. 
On crossing certain threshold of concept drift, we have reassess the labels we were initially preparing. 

## Interpretability 
We can use post-hoc model agnostic local surrogate models to find out the responsible words in the sentence which contributed to the output. We can try ELI5/LIME for the same. The top words can be highlighted in the output for officer's review. 