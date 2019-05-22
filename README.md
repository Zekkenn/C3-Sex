# C3-Sex

![](https://img.shields.io/badge/python-3.6.2-brightgreen.svg)  ![](https://img.shields.io/badge/tensorflow-1.4.0-yellowgreen.svg?sanitize=true)

## Project Objectives

This project aims to design and build a Bot with interactive sentimental intelligence, able to discover and reveal the profile of cybercriminals in massive online chats, through the elaboration of pertinent answers considering the linguistic and sentimental content.

In addition, the following are the specific objectives, which are established to describe the expected results of the project:

1. Design a chatbot solution based on an integration of different models of the artificial intelligence domain; a generative based model and another on retrieval-based.

2. Implement a chatbot capable of generating responses in order to empathize with the suspect and manipulate it to obtain useful information.

3. Profile suspects (by sentiment analysis and emotions classification) using the data obtained from the interaction with the Bot with interactive sentimental intelligence.

## How to install & Set Up

### System Requirements

|                   |                  Minimum                 |                     Recommended                     |
|-------------------|:----------------------------------------:|:---------------------------------------------------:|
|        CPU:       | Cores: 2; Frequency: 1,70GHz; Cache: 3MB | Cores: 4; Frequency: 2,80GHz; Cache: 6MB            |
|      Memory:      | 8GB RAM                                  | 12GB RAM                                            |
|  Free Disk Space: | 2GB                                      | 2GB                                                 |
| Operative System: | Windows 7/8/10                           | Windows 7/8/10                                      |
|        GPU:       | None                                     | Nvidia GeForce GTX 950                              |
|     Software:     | Python 3.6.2; Pip; Google Chrome         | Python 3.6.2; Pip; CUDA Toolkit 10.1; Google Chrome |
|  Network Access:  | Yes                                      | Yes                                                 |

### Required Packages

Before installing or downloading the project, you must ensure that you have installed the following packages:

| Package Name |                                                                              Description and Functionality                                                                             |
|:------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|   selenium   | It provides the Selenium WebDriver API, which allows the project to connect to a browser natively.                                                                                     |
|  tensorflow  | As a Machine Learning library, the project use it to build the recurrent neural network (RNN), which simulates the generative conversational agent                                     |
|    pandas    | A data analysis library used to manage and read certain data structures, such as csv and dataframes                                                                                    |
|    sklearn   | In addition to making use of tensorflow, sklearn is available for the adoption of ML algorithms, such as the Bayesian network in the opinion classification model.                     |
|     nltk     | The natural language tool gives the project the advantage of tokenize words, its used in the different models.                                                                         |
|      bs4     | The Beautiful Soup library allows you to extract data from HTML files, the project use it to extract the knowledge of a GitHub repository, for mapping Slangs in the English language. |
|  python-aiml | This library serves as an inference engine to read xml files as the AIML form, which contain the entire knowledge base of the retrieval-based conversational module                    |

To download any of the packages its recommended to use the pip command, replacing the _package-name_ part:

```bash
pip install package-name
```

### Before using the project

Before starting to use the product and to ensure that each functionality works properly, you should consider the following instructions.

* To use the ACA module where all the logic of the conversational agent resides, you must ensure that it is trained, for this, the following files must be in the _./ACA/Data/Result_ folder:

![](/ACA/Data/ACA_results.jpg)

To generate them you must train the generative model (which will require a lot of time, depending on the training data you want to use) or use the already trained data that can be found [here](https://www.dropbox.com/sh/c0q5g2c9c9cbkzp/AACNcggs-brWdeHdRaVi45-Ca?dl=0).

## Software Modules usage

The following information is provided so that the user will be able to use each of these services individually, taking advantage of everything they can offer.

### Artifitial Conversational Agent/Entity (ACA)

This conversation module can be used in different ways, depending on what you want to do:

1. **Model Training:** During this stage, the model whould be trained based on the dataset and the vocabulary provided. To do so, you should run the following command from the root of the project.

```bash
py ACA/chatbot/bottrainer.py
```
*Keep in mind that training can take a long time (depending on parameters you want to train with). These parameters can be modified in ACA/Data/Corpus/hparams.json. Likewise, the dataset that is provided for training can be modified by adding files in ACA/Data/Corpus/Argument0 with the format Question-Answer, as its show in the clean data that we used. Once the training has begun, you must ensure that the following files are created in ACA/Data/Result, which are used for testing and prediction.*

- basic.data-00000-of-00001
- basic.index

2. **Test / Inference:** This stage provide a simple interface and a web-based one. Note that *ACA/Data/Corpus/vocab.txt* and *ACA/Data/Rules/hot-startup.aiml* files are necessary for inference. To see the performance of the model, you must execute the following command and wait until the ">" indicator appears:

```bash
py ACA/chatbot/botui.py
```

### Sentiment Analysis Module

For the sentiment analysis module, you can make use of the two classifiers; opinion and emotions, the first one developed on Python and the second one on R.

1. **Opinion Classifier:** You can access the file *SA_Module/sentimentAnalysis.py* from the root, and make use of the following functions, considering their inputs.

```python
predict(data) # data should be a response
predict_proba(data) # Same way, a sentence and the output differs 'cause returns the probability
sa_measure(replies_file) # A text file with sentences/responses to be classified with probabilities.
```

2. **Emotions Classifier:** In the case of emotions module implemented in R, you can make use of the model trained by the *EC_Module/emotional_classifier.py* file, which executes an R script to generate prediction for those sentences that will be classified.

```python
ec_measure(replies_file) # A text file with sentences to classify, returns a list with positive (1) emotions or negative (0)
```

*You must consider that the two modules in addition to returning the above, they generate a file with the respective opinions and emotions by sentence, these files have the same name as the one provided, but adding an "_SA" and "_EC" in the end respectively.*

### Slangs PreProcessing

To make use of this module, you can get the slangs saved on a csv file through a method that offers *Slangs / slangExtractor.py*, with the following method inside the file:

```python
getSlangs() # Returns a slangs map with its formal language representation
```

## Software General Usage

To use the software as a whole (which integrates all the mentioned modules). You need to execute the following command from the root of the project.

However, before doing so, you must ensure the following indications:

- Check your Google Chrome browser; you must keep your Telegram account open (where the suspects will speak to you) and you must verify the anti-bot captcha on Omegle. Also, you must close all Google Chrome processes on Task Manager.

- You must change in the file *./ACA/Data/Rules/illegalcontent/hotmaterial.aiml* all those fields about the Telegram username (by default is @alanaJe) that you are going to use.

```bash
py main.py
```

## References and Credits

1. C3-Sex: a Chatbot to Chase Cyber perverts : (Paper link Soon)
2. ACA Generative Module : [ChatLearner by Bo Shao](https://github.com/bshao001/ChatLearner)
3. ACA Retrieval Module Intro : [AIML basics - ALICE](https://github.com/datenhahn/python-aiml-chatbot)
