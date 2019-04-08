## DATA622 Project
- Assigned on November 13, 2018
- Due on December 11, 2018 12:00 PM EST
- 25 points possible, worth 25% of your final grade

### Instructions:
Read the online textbook [Neural Networks and Deep Learning by Michael Nielsen](http://neuralnetworksanddeeplearning.com/) in its entirety.  Use the code in the book to guide your steps to build an image recognition model on the classic MNIST dataset.  The data pull steps can also be found in the book.

### Critical Thinking (10 points)
Submit a ~500 word explanation of the choices and tradeoffs you made in the process of building this model.  (e.g. why did you go X layers deep? why did you choose X cost function?).

After reading articles on hidden layers in the neural network, I understood that there are no set rules on the number of hidden layers a model should have. It is a hyper-parameter that can be tuned to get better results. I have used two hidden layers with 36 neurons each for the scope of the assignment. Hidden layers and the number of neurons per layer play an important role in predicting the output. More hidden layers and/or more neurons per hidden layer will need a high amount of resources for processing. 

I also tried to tune weights and biases using the entire dataset in one go, due to limited resources process failed. Using the steps described in the online book, _Neural Networks and Deep Learning_ by Michael Nielsen, I have learned to split the dataset into multiple mini batches and process one batch at a time.

I have used two different cost functions, quadratic cost, and cross-entropy. I couldn't find much difference between the accuracy of the output. However, cross-entropy cost function had better performance. Also, cross-entropy gives one more additional hyper-parameter(lambda) that could be tuned for optimal performance.

### Applied (20 points)
Submit all code, clean and commented.  Feel free to use any distributed computing methods we discussed in previous lessons to help you in this process, but it's not necessary.  

I have uploaded minist dataset to Hadoop and used Spark for processing. Dataset upload script and jupyter notebook are uploaded to GitHub.

### Additional Resources

1. The [Goodfellow book](http://www.deeplearningbook.org/) on Deep Learning is the authorative resource on this subject still.  
2. Check out [this curated list](https://github.com/ChristosChristofidis/awesome-deep-learning) for even more resources on deep learning.  
