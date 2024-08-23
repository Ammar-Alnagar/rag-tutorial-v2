from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function
from langchain.vectorstores.chroma import Chroma

from populate_database import split_documents



DATA_PATH = "data\Mawared full dataset alpaca_  - Sheet1.csv"



document_loader = CSVLoader(DATA_PATH)
chunks = split_documents(document_loader)
x = chunks()
print(x[0])

 
