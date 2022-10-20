A brief explanation of the Inverted Index
The inverted index is a database index storing a mapping from content, such as words or numbers, to its locations in a database, or in a document or a set of documents. The purpose of an inverted index is to allow a fast full-text search.<br><br>
![image](https://user-images.githubusercontent.com/56029669/196867374-dc333866-98a9-4ba6-984c-07ee42018156.png)


To better understand what is the inverted index and how to use this index, let’s review a simple example with two documents:

Document#1 with text “Recipe of pasta with sauce pesto”
Document#2 with text “Recipe of delicious carbonara pasta”
To build the inverted index, we have to split those sentences into tokens, in our case, the tokens are words. After this, tokens will be saved with links to documents, in some cases, before saving tokens can be transformed.

The inverted index for those sentences will look like this simplified schema:
![image](https://user-images.githubusercontent.com/56029669/196867262-61abd02d-e4ec-49c2-94a8-67bc99c4a6e8.png)


The simplified schema of the inverted index
In this inverted index, we can find a link to the document by token(a word from the text).

Let’s look at a few examples of search queries:

The search query “pasta recipe” will be divided into two tokens (“pasta” and “recipe”), then it will be matched with the inverted index and will return both documents with the same score(the score is a similarity of a document and a search phrase; we will review the score later in this article).
The search query “carbonara pasta” will give you both documents as well, but document#2 will have a bigger score then document#1. Because document#2 has both tokens (and “carbonara” and “pasta”), but document#1 has only one(“pasta”) token.
The search query “delicious carbonara” will give you only document#2, because this document has both tokens, and document#1 has none of them.
Sometimes we can transform tokens before saving and searching. The most popular kinds of transformation are:

Dropping of the stop words. Stop words are the most popular words in the language or in your dataset, which don’t have any semantic weight. For example, in English, it can be the following words “of”, “the”, “for”, etcetera.
Lemmatization. Lemmatization is a process of changing a word to a dictionary form of the word, “running” => “run”, “walks” => “walk”, “thought” =>“think”
Stemming. Stemming is a process of transforming a word into root form by cutting the ending of the word. This is similar to Lemmatization, but can not handle cases with irregular verbs, but can handle words which are not in the dictionary.
That’s all.

