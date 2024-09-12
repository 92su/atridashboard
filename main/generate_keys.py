import pickle
from pathlib import Path

import streamlit_authenticator as stauth


names = ["Peter Parker", "Rebecca Miller","Su Mon Aung"]
usernames = ["pparker", "rmiller","smaung"]
passwords = ["abc123","def456","sma123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent/ "hashed_pw.pkl" # run this app in terminal first
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)
