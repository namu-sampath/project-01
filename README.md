## Net(flexing) My Streaming Habits
 
This is a repository of an analysis of three years of my personal tv watching habits taken from my original [Google Drive spreadsheet](https://docs.google.com/spreadsheets/d/18k4Fz02x1VXgSbI4WbPkUuSoTdogD4LEDrniXcm7as4/edit#gid=0)


## What I aimed to accomplish

I thought it would be interesting to take a look at what I watch on TV, which platforms I watch TV on the most, and my favorite genres, and how many shows I average per year. Because I already had an existing spreadsheet that I frequently update, I figured it would be easiest to just analyze this information; however, I also wanted (and potentially could for a future project) to understand how my reviews and watching patterns compare to other viewers' reviews and watching patterns. 

## My Findings

First and foremost, I am most shocked by what the data says is my most watched genre: 'Teen Dramas.' 

In my original spreadsheet, I had personally labeled each of my 'watched genres.' My top 10 most watched are: teen drama, crime, drama, reality tv, documentary, thriller, rom-com, dramedy, comedy, and family dramas. 

To me, teen dramas are shows that include themes of romance, drama, and comedy, but are also coming-of-age stories, and generally explore topics including budding romance, exploring relationships, and school issues, etc., that high schoolers or young adults may prefer over an older audience. 

I also found that I only scored three of the 138 shows I watched below a 5. Interestingly, two of those shows were reality TV (Bling Empire and Koffee with Karan). Both were also directed toward being an influencer or celebrity, or to an audience of people who enjoy learning about influencers and celebrities. 

Additionally, I found that Netflix is my most used streaming platform. Going forward, with the new [Netflix policy](https://about.netflix.com/en/news/an-update-on-sharing) about account sharing, I am interested to see how these numbers might not only change for me, but other viewers as well. 

## Data Collection Process

As I used data that I already had spent a lot of time with, the data collection process for me was not much about scraping or cleaning, and much more about consolidating what I thought would be the most interesting to discover. 

For ease, I used Jupyter Notebooks to parse through my data using pandas. 

## Installation

pip install pandas 

## Usage
```python
import pandas as pd
```

```python
import matplotlib.pyplot as plt
```

While I didn't end up using matplotlib.pyplot for my graphs, it could still be useful for a future data analysis. 

## Asking questions
I then printed my dataframe and the index of my columns: 'year_watched', 'show_title', 'genre', 'num_of_seasons', 'rating', 'streaming_platform', 'namu_reviews'. 

This was to better understand what questions to ask about my streaming habits. 

I then came up with a few questions that I was most interested to know: 
1. How many seasons of shows have I seen in a three year span?
2. How many shows have I rated under 5?
3. How many shows per streaming platform? 
4. How many shows do I watch per year?
5. What genre do I watch the most?
6. What are my top 5 (and top 10) most watched genres?

## Visuals
To understand my data better, I used [Datawrapper](https://www.datawrapper.de/) to make two bar charts (one horizontal and one vertical) and one 'election donut', which I used to break down my top five genres. 

I also used [Figma's Iconify feature](https://www.figma.com/community/plugin/735098390272716381/Iconify) to add an artistic perspective to one of my bar charts - referring to my streaming platform breakdown. 

## New skills and approaches
I am brand new to coding, Github, making data visualizations, and HTML/CSS. So really, this whole project was a learning curve for me. My favorite thing we've learned so far (in terms of coding), is pandas. I feel like it has really helped me see that data does not have to be so scary to understand. Sure, overwhelming at times, but nothing I can't handle. 

*Coding*
Using Jupyter Notebooks also made using pandas easier for me to understand visually because it was simpler to follow.

*Visualizations*
As I mentioned before, I used both Datawrapper and Figma to visualize my data. This was, by far, the most creative side of my project, I am glad I was able to see a sketch I had in my head of a prototype for the visualizations become reality on my webpage. 

*Webpage*
Unlike my approach to my data, I built my ```index.html``` on VS Code. I copied styles from previous Lede students and organized the page using my own stylistic choices. I played around a lot with CSS to find what worked best for me. 

## What would I do differently next time?
If given more time to pursue this project, I would've reached out to each of the streaming platforms to request viewers' TV watching information as it related to my analysis. I would have also tried to delve into IMDb's and Letterbox'd's APIs to take a look at whether my reviews reflect those of a greater audience. 

If I had known how to change the background color of my webpage, I would've liked it to be a different color other than white. I think I also would have wanted to make my data interactive somehow, so that if someone were viewing my data in the future, they could put in a show that they really liked (or hated) and see how it fared compared to my ratings as well as other viewers' ratings. 







