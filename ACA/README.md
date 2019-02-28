# Artificial Conversational Agent

## Training Generative-Based Model
Other than Python 3.6 (3.5 should work as well), Numpy, and TensorFlow 1.4. You also need NLTK (Natural Language Toolkit) version 3.2.4 (or 3.2.5).

During the training, I really suggest you to try playing with a parameter (colocate_gradients_with_ops) in function tf.gradients. You can find a line like this in modelcreator.py:
gradients = tf.gradients(self.train_loss, params). Set colocate_gradients_with_ops=True (adding it) and run the training for at least one epoch, note down the time, and then set
it to False (or just remove it) and run the training for at least one epoch and see if the times required for one epoch are significantly different. It is shocking to me at least.

Other than those, training is straightforward. Remember to create a folder named Result under the Data folder first. Then just run the following commands:

```bash
cd chatbot
python bottrainer.py
```

Good GPUs are highly recommended for the training as it can be very time-consuming. If you have multiple GPUs, the memory from all GPUs will be utilized by TensorFlow, and you can adjust the batch_size parameter in hparams.json file accordingly to make full use of the memory. You will be able to see the training results under Data/Result/ folder. Make sure the following 2 files exist as all these will be required for testing and prediction (the .meta file is optional as the inference model will be created independently): 

1. basic.data-00000-of-00001
2. basic.index

## Testing / Inference
For testing and prediction, we provide a simple command interface and a web-based interface. Note that vocab.txt file (and files in KnowledgeBase, for this chatbot) is also required for inference. In order to quickly check how the trained model performs, use the following command interface:

```bash
cd chatbot
python botui.py
```

Wait until you get the command prompt "> ".

## References and Credits:
1. ChatLearner by Bo Shao: https://github.com/bshao001/ChatLearner
2. AIML basics - ALICE: https://github.com/datenhahn/python-aiml-chatbot
