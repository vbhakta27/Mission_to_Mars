
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import re
import time


def init_browser():
    # Setting up chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)



def scrape():
    browser = init_browser()

    ########## Nasa Mars News ##########
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    # Wait for 5 seconds
    time.sleep(5)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain news information
    news = soup.find('div', class_='list_text')

    # Use Beautiful Soup's find() method to navigate and retrieve attributes
    # Get the news title
    content_title = news.find('div', class_="content_title")
    news_title = content_title.find('a').text

    # Get the news paragraph text
    news_p = news.find('div', class_="article_teaser_body").text


    ########## JPL Mars Space Images ##########
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Wait for 5 seconds
    time.sleep(5)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain the first mars picture information
    mars_latest_pic = soup.find('li', class_="slide")

    # Dissect the anchor which contains the img link
    anchor = mars_latest_pic.find('a')
    image_link = anchor['data-fancybox-href']
    featured_image_url = ('https://www.jpl.nasa.gov/' + image_link)


    ########## Mars Weather ##########
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    # Wait for 5 seconds
    time.sleep(5)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Find latest (first) tweet using Regular Expression Patterns
    mars_weather = soup.find("span", text=re.compile("InSight")).text


    ########## Mars Facts ##########
    url = 'https://space-facts.com/mars/'

    # Convert html table into pandas
    mars_facts_tables = pd.read_html(url)
    mars_facts_tables[0]

    # Save table into dataframe
    mars_facts_df = mars_facts_tables[0]

    # Convert dataframe into html and removed new line (\n) in code
    mars_fact_html_table = mars_facts_df.to_html()
    mars_fact_html_table = mars_fact_html_table.replace('\n', '')
    mars_fact_html_table


    ########## Mars Hemispheres ##########
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Wait for 5 seconds
    time.sleep(5)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain news information
    results = soup.find_all('div', class_='item')

    # Create empty list to store dictionary containing all img titles and urls
    hemisphere_image_urls = []

    # Iterate through each hemisphere link
    for result in results:
        # Get url for each hemisphere result
        hemisphere_anchor = result.find('a')
        hemisphere_url = ('https://astrogeology.usgs.gov/') + hemisphere_anchor['href']

        # Go to hemisphere url
        browser.visit(hemisphere_url)
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Get title for image
        title = soup.find('h2', class_='title').text
        title = title.rsplit(' ', 1)[0]
        
        # Get url for image
        downloads = soup.find('div', class_='downloads')
        list_tag = downloads.find('li')
        anchor_tag = list_tag.find('a')
        img_url = anchor_tag['href']

        mars_img_dict ={}
        mars_img_dict['title'] = title
        mars_img_dict['img_url'] = img_url
        hemisphere_image_urls.append(mars_img_dict)

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_fact_html_table": mars_fact_html_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

# Jeff Added Code:  ALWAYS TEST!!!
if __name__ == "__main__":
    print("\nTesting Data Retrieval...\n")
    print(scrape())
    print("\nProcess Complete!\n")