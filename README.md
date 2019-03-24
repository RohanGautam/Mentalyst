# Mentalyst
Hack developed at HackNTU 2019
## Inspiration

According to American journalist, we live in what he calls a "post-truth political environment". A political culture in which debate is framed largely by appeals to emotion disconnected from the details of policy. We often find ourselves surrounded by lies and political scandals. Studies have also shown that humans can detect lies in 54% of all cases. So this begs the question, how can we do better?

## What it does

Our system takes in a video and analyses the emotional discrepancies in the audio and the video. The system also detects tell-tale signs of lying such as extensive pausing to show whether a politician has a probability of lying or not. We additionally display the transcript of the text. Our fact-checking feature allows users to highlight pieces of text and see if the statements are correct according to the PolitiFact database.This system has vast applications such as during parliament sessions as well as criminal interrogations.

## How we built it
### Lie Detection
* The sample video is split into frames. Facial recognition is then performed to extract the faces from these frames.
* The faces are given probabilities of 5 key emotions, and we store the frame by frame information in a csv file.
* We also obtain sentiment analysis information from each sentence from the video transcript we generate.
* We perform a weighted average of these two, taking into consideration the pronunciation and articulation data for the audio, and use that as a metric, setting a threshold for what’s a lie and what’s not.


### Fact Checker
* We use google sub-search using politifact to get information about claims, the person who claimed it, and the verdict about the claim in reality.
* Since this information is rendered after the page loads, instead of just “requesting” the page and reading the html, we actually launch a full-blown headless browser with selenium in the background, which you cannot see, and scrape data loaded from there.

### Dashboard
* Use Express server to run fact-checker as well as for video upload
* Used React to make the video playback, lie indicators as well as the transcript.


## Challenges we ran into
*Finding an appropriate database* - Our initial idea also included training on voice modulation and microexpressions. However, later on in the hack, we came to know that these are paid datasets and not open source. Hence we couldn’t integrate them with our projects. There were also nothing like these datasets available for free, hence we had to work with whatever we got.
*Setting up server* to deliver facts, run video and show lies in real time - We use local data as of now, and that in itself turned out to be quite a challenge when it was time for the backend(python) and the frontend(react) to communicate.  
*Finding how to decide if lie or not* - We had to read up a lot of psychological research papers to come up with suitable metrics for the algorithm


## Accomplishments that we're proud of
* Figuring out a suitable metric for approximating lie detection using open source resources. 
* Using headless browsers to scrape dynamically loaded data and using scraped information to perform fact-checking.
* Getting frontend and backend to talk through a child process, and thus integrating python and javascript.
* Not giving up halfway!

## What we learned
* The various factors that go into identifying liars
* The benefits of using multiple metrics such as NLP, Emotion Recognition, Speech analysis to improve our prediction accuracy
* How to use headless browsers(python+javascript)
* Inter-language communication

## What's next for Mentalyst
* Develop more metrics to increase accuracy of the system
* Train our lie detection algorithm over multiple videos for better weighting of factors
* Using microexpressions and richer [data sets](https://catalog.ldc.upenn.edu/LDC2013S09) for better models to train our algorithm
* Working with live video and audio input to process it in real time.
