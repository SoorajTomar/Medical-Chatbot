import speech_recognition as sr
import pyttsx3
from tkinter import *
import pandas as pd
question=""
def speech(text):
engine=engine = pyttsx3.init()
voices=engine.getProperty(‘voices’)
engine.setProperty(‘voice’,voices[1].id)
engine.say(text)
engine.runAndWait()
def this_is_where_the_magic_happens():
global question
treatments_df = pd.read_csv("treatments_data.csv", encoding="latin1")
treatments_df["Disease"] = treatments_df["Disease"].str.lower()
symptoms_df = pd.read_csv("symptoms_data.csv", encoding="latin1")
symptoms_df["Disease"] = symptoms_df["Disease"].str.lower()
question = question.lower()
match = re.search(r'\bsymptoms of (\w+)\b', question)
if match:
disease_name = match.group(1).lower()
data = symptoms_df.loc[symptoms_df["Disease"] == disease_name,
"Symptoms"].iloc[0]

ans=(f"The symptoms of {disease_name} are: {data}")
print(ans)
speech(ans)
else:
match = re.search(r'\btreatment of (\w+)\b', question)
if match:
disease_name = match.group(1).lower()
data = treatments_df.loc[treatments_df["Disease"] == disease_name,
"Treatment"].iloc[0]
ans=(f"The treatment for {disease_name} is: {data}")
print(ans)
speech(ans)
else:
ans="I'm sorry, I didn't understand your question."
speech(ans)
global Answer
ans = "answer to query".upper()
Answer["text"]="Answer: "+ans
def get_input():
print("Working")
r = sr.Recognizer()
global question
question="Sorry! Didn't catch that, kindly speak again."
try:
with sr.Microphone() as source2:

r.adjust_for_ambient_noise(source2, duration=0.2)
audio2 = r.listen(source2)
MyText = r.recognize_google(audio2)
MyText = MyText.lower()
question=MyText.upper()
except :
question="Sorry! Didn't catch that, kindly speak again."
speech(question)
global Query
Query["text"]="Query: "+question
root=Tk()
root.title('🤖')
root.geometry('400x200')
Query=Label(root,text="Query: ")
Query.place(x=0,y=0)
Answer=Label(root,text="Answer: ")
Answer.place(x=0,y=50)
Input=Button(root,text="Speak",command=get_input)
Input.place(x=70,y=170)
Search=Button(root,text="Go",command=this_is_where_the_magic_happens)
Search.place(x=240,y=170)
root.mainloop()
