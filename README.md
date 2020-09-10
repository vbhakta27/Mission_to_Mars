# Mission to Mars

## Background
With all the recent excitement with potential Mars colonization I wanted to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page

## Web Scrape
I first completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. This was stored in a Jupyter Notebook file called `mission_to_mars.ipynb`.

The following sources were scraped: 
### NASA Mars News
* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image
* Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and used splinter to navigate the site and found the image url.

### Mars Weather
* Visited the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scraped the latest Mars weather tweet from the page.

### Mars Facts
* Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. I then used Pandas to convert the data to a HTML table string.

### Mars Hemispheres
* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres. I used a Python dictionary to store the data using the keys `img_url` and `title`. I appended the dictionary with the image url string and the hemisphere title to a list. The list contains one dictionary for each hemisphere.

