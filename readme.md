## BaseSoAR
Welcome to BaseSoAR!

BaseSoAR allows you to build a quick web-app to help your students learn more effectively with online resources and the deployment of this app is also for free!

## Setting Up BaseSoAR

In this guide, you are assumed to have basic Python knowledge and have installed Python and Visual Studio Code in your computer.

* Clone the repo in a folder
* Open the folder in Visual Studio Code
* Run the file `BaseSoAR.py` to start a terminal (you can ignore any errors for now)
* In the terminal below, create a virtual environment using `python -m venv .venv` on Windows and `python3 -m venv .venv` on Mac OS
* At the bottom right of Visual Studio code, you should see that a new environment is found as a pop up and click "Yes"
* Kill the terminal by clicking the trash icon logo
* Rerun `BaseSoAR.py`
* Install all the dependencies by using `pip install -r requirements.txt` in the terminal
* Create a folder called `.streamlit` in the current folder (where `BaseSoAR.py` is located in)
* Create a file named `secrets.toml` in the `.streamlit` folder
* Generate an OpenAI API Key and create a field `OPENAI_API_KEY = "(paste your API key here without the brackets)`

