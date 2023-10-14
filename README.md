# Processing Large Files
## Purpose of the Program
- compare the 10 most popular words of two large files [True.csv and Fake.csv](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) which contain real and fake news articles accordingly to see how these files are different

## Design of the Program
- Reads the content of both files and counts the number of each word
- Ignore uninteresting words like **‘the’, ‘is’, ‘in’** in [ignore_words.txt](ignore_words.txt)
- Create two new files (fake_popular_words.txt and true_popular_words.txt) with the 10 most
popular words on the corresponding files.

## Output of the Program
[10 most popular words in True.csv](true_popular_words.txt)

[10 most popular words in Fake.csv](fake_popular_words.txt)
