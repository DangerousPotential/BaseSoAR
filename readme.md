## BaseSoAR
Welcome to BaseSoAR!

BaseSoAR allows you to build a quick web-app to help your students learn more effectively with online resources and the deployment of this app is also for free!

## Setting Up BaseSoAR

In this guide, you are assumed to have basic Python knowledge and have installed Python and Visual Studio Code in your computer.

* Clone the repo in a folder using `git clone https://github.com/DangerousPotential/BaseSoAR.git`
* Open the cloned folder in Visual Studio Code (File -> Open Folder)
* Run the file `BaseSoAR.py` to start a terminal (you can ignore any errors for now)
* In the terminal below, create a virtual environment using `python -m venv .venv` on Windows and `python3 -m venv .venv` on Mac OS / Chromebook
* At the bottom right of Visual Studio code, you should see that a new environment is found as a pop up and click "Yes"
    * Alternatively, you can hold `Ctrl + Shift + P` and type in `Python: Select Interpeter` and choose the environment with the `.venv` name
* Kill the terminal by clicking the trash icon logo
* Rerun `BaseSoAR.py` and expect an error
* Install all the dependencies by using `pip install -r requirements.txt` in the terminal
* Create a folder called `.streamlit` in the current folder (where `BaseSoAR.py` is located in)
* Create a file named `secrets.toml` in the `.streamlit` folder
* Generate an OpenAI API Key and create a field `OPENAI_API_KEY = "(paste your API key here without the brackets)`

## Using BaseSoAR
* `BaseSoAR.py` is the main page where user will load into (feel free to adjust the title name and contents in the page)
* `./pages/*.py`: All Python files in the `pages` folder will be a single page accessible in the sidebar (the name of the `.py` file represents the name of the page)
    * For this page, you can refer to `Chapter 1.py` to see how buttons can be created and how information can be presented with the click of the button
    * How to initialise a temporary list to store conversation history
    * How to spawn the chat bot interface
* `./images/chapterno/*.png`: All images file would be stored in their sub-folder located in the images directory (e.g. chapter 1 images are stored in `./images/chapter1/test.png`)
* `./documents/(pdf file)`: All documents that you need to connect to the LLM should be loacted in the documents folder (e.g. chapter 1 document is stored in `./documents/chapter1.pdf`)
## Document Usage
* `RAG*.py`: To connect the files to the LLM, you can reuse the code from `RAGChapter1.py` changing only the document path file in line 20
* **Example**: If I have another file for Chapter 2, I will copy and paste the file `RAGChapter1.py` and rename it to `RAGChapter2.py` and change the pdf file path in RAGChapter2.py to `./documents/chapter2.pdf`.
    * I will then go over to `./pages/Chapter 2.py` and import the `answer` function from `RAGChapter2.py` by adding an import statement like this ```from RAGChapter2 import answer```

