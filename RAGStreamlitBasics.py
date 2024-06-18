# From the Retrieval Augmented Generation Notebook
import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_community.document_loaders import PyPDFLoader
from operator import itemgetter

@st.cache_resource
def load_and_split_pdf(path):
    loader = PyPDFLoader(path)
    pages = loader.load_and_split()
    return pages
@st.cache_resource
def create_vector_storage(_documents):
    vectorstore = FAISS.from_documents(_documents, embedding = OpenAIEmbeddings(openai_api_key = st.secrets["OPENAI_API_KEY"]))
    return vectorstore
pdf_path = "./documents/Streamlit Basics .pdf"
pages = load_and_split_pdf(pdf_path)
vectorstore = create_vector_storage(pages)

# Retrieval Method
retriever = vectorstore.as_retriever()
# Prompt Template
template = '''
Answer the question based only on the following context
{context}

Question: {question}
'''
prompt = ChatPromptTemplate.from_template(template)
# Connection with OpenAI
llm = ChatOpenAI(openai_api_key= st.secrets["OPENAI_API_KEY"])

# Chain
chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()

def answer(question):
    response = chain.invoke(question)
    return response