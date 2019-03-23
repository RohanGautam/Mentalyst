my = __import__("my-voice-analysis")
# 'On Rosie  Fat Ugly Face'
def properties(p='/home/rohan/Desktop/Python_Files/HackNTU/emotions-video/pauses_articulation', m='output_audio'):
    # Add the following two lines
    # p=input("enter the path to the dataset: ")
    # #then copy/paste C:\Users\Desktop\dataset
    # m=input("enter the audio file name: ") # the audio fiile name without extention

    my.mysppaus(m,p)
    x=my.myspsr(m,p)
    my.myspatc(m,p)
    my.myspst(m,p)
    my.myspod(m,p)
    my.myspbala(m,p)
    my.myspf0mean(m,p)
    my.myspf0sd(m,p)
    my.myspf0med(m,p)
    my.myspf0min(m,p)
    my.myspf0max(m,p)
    my.myspf0q25(m,p)
    my.myspf0q75(m,p)
    my.mysptotal(m,p)
    my.mysppron(m,p)
    my.myspgend(m,p)

properties()