# Knowledge-Graph-Implementation Dissertation
This is my resp for the implementation of two knowledge graph from scratch
## Description 

### Data Collection

For developing the knowledge graph it is mandatory to have the data so, first we need scrape the data that's why you need to run this file `song_facts_scrapper.py` But for the convience I had scarpped quite a amount data which is saved in the file called Data.
### Implementation Knowledge Graph using the DBpedia

Before runing the file `Knowledge_Graph_using_DBpedia.ipynb` . You need to make sure few things are already imported in you device:-
1. Download the python file called `entityRecognitionLinking.py` because it is been imported in `Knowledge_Graph_using_DBpedia.ipynb`
   Which as the details of DBpedia API, so it is mandatory to call and import that file before running `Knowledge_Graph_using_DBpedia.ipynb`
2. Download the dataset from the `Data`, the code specifically say to fetech `Data\Music_related_sent.csv`

### Implementation Knowledge Graph Using My State of Art:

Before Runing the file `Knowledge_graph(with_coreferencing_and_spaCy).ipynb`
1. !pip install spacy==2.3.7
2. Follow the following code to enable the coreferencing:

   2.1 !git clone https://github.com/huggingface/neuralcoref.git
   
   2.2 import os
   
       os.chdir("/content/neuralcoref")
       
       !pip install -r requirements.txt
       
       !pip install -e .     
       
Then restart your runtime then start running the code 

3.Just like before use the datasets from the file Data in the resp

4.For Making the Spotify API works we need to make:[1]

      Spotipy is a Python client for the Spotify Web API that makes it easy for developers to fetch data and query Spotify’s catalog for songs. You have to       install using:-
      
      !pip install spotipy
      
      After installing Spotipy, you will need to create an app on the Spotify Developer’s page and save your Client ID and secret key.
      Then you need to call few datasets from Data:
          1.data.csv
          2.data_by_genres.csv
          3. data_by_year.csv
          
Reference
1. https://www.kaggle.com/code/vatsalmavani/music-recommendation-system-using-spotify-dataset/notebook
