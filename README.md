# C3-Sex

![](https://img.shields.io/badge/python-3.6.2-brightgreen.svg)  ![](https://img.shields.io/badge/tensorflow-1.4.0-yellowgreen.svg?sanitize=true)

## Project Objectives:

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

![](/img/ACA_results.png)

To generate them you must train the generative model (which will require a lot of time, depending on the training data you want to use) or use the already trained data that can be found [here](https://www.dropbox.com/sh/c0q5g2c9c9cbkzp/AACNcggs-brWdeHdRaVi45-Ca?dl=0).
