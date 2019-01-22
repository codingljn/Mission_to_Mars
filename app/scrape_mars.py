
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def scrape():
    # # NASA

    # In[2]:
    scrape_mars_dict = {}

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'


    # In[3]:


    # Retrieve page with the requests module
    response = requests.get(url)


    # In[4]:


    # Create BeautifulSoup object; parse with 'html.parser'
    soup =bs(response.text, 'html.parser')


    # In[5]:


    # Examine the results, then determine element that contains sought info
    print(soup.prettify())


    # In[9]:


    # results are returned as an iterable list
    results = soup.find("div", class_="features")


    # In[13]:


    article_title = results.find("div", class_="content_title").text
    asumm = results.find("div", class_="rollover_description").text
    print("Title: "+str(article_title))
    print("Summary: "+str(asumm))

     # Store scraped data into dictionary
    scrape_mars_dict['article_title'] = article_title
    scrape_mars_dict['asumm'] = asumm


    # # JPL

    # In[ ]:


    # This portion of the homework uses Splinter, which we were asked not to use. I have added the link to the featured image after searching for it manually.
    featured_image_url: "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA14924_ip.jpg"

    # Store url to dictionary
    scrape_mars_dict['featured_image_url'] = featured_image_url


    # # Mars Weather

    # In[30]:


    # Visit Mars Weather Twitter account and scrape the latest Mars weather tweet from the page.
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    twitter_response = requests.get(twitter_url)
    twitter_bsoup = bs(twitter_response.text, "html.parser")


    # In[31]:


    # Examine the results, then determine element that contains sought info
    print(soup.prettify())


    # In[32]:


    twitter_result = twitter_bsoup.find("div", class_="js-tweet-text-container")
    mars_weather = twitter_result.find("p", class_="js-tweet-text").text
    print(mars_weather)

    # Store scraped data into dictionary
    scrape_mars_dict['mars_weather'] = mars_weather

    # # Mars Facts 

    # In[22]:


    # Scrape space-facts.com for mars fact using Pandas read_html function
    mars_facts_url = "https://space-facts.com/mars/"
    result = pd.read_html(mars_facts_url)
    # Check output
    print(result)


    # In[24]:


    # Use Pandas to convert the data to a table
    result_df = result[0]
    result_df.columns = ["Parameter", "Value"]
    # Reset index
    result_df.set_index("Parameter", inplace=True)
    result_df


    # In[25]:


    # Use Pandas to convert the data to a HTML table string
    result_df = result_df.to_html()


    # In[26]:


    # Check HTML output
    result_df

    # Store html file to dictionary
    scrape_mars_dict['mars_facts'] = result_df

    # # Mars Hemispheres

    # In[ ]:


    # hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    #Error due to temporary government shutdown: "The requested service is temporarily unavailable. Please try later."


    # In[ ]:


    # However, thanks to the HW instructions we can find these images somewhere else on the Internet


    # In[ ]:


    # Valles Marineris Hemisphere Enhanced
    url1 = "https://mars.nasa.gov/system/resources/detail_files/6453_mars-globe-valles-marineris-enhanced-full2.jpg"
    # Cerberus Hemisphere Enhanced
    url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cerberus_Hemisphere_Enhanced.jpg/600px-Cerberus_Hemisphere_Enhanced.jpg"
    # Schiaparelli Hemisphere Enhanced
    url3 = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Schiaparelli_Hemisphere_Enhanced.jpg/600px-Schiaparelli_Hemisphere_Enhanced.jpg"
    # Syrtis Major Hemisphere Enhanced
    url4 = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/PlanetMars-SyrtisMajor-VikingOrbiter-1980.jpg/600px-PlanetMars-SyrtisMajor-VikingOrbiter-1980.jpg"

    scrape_mars_dict['hemisphere_1'] = url1
    scrape_mars_dict['hemisphere_2'] = url2
    scrape_mars_dict['hemisphere_3'] = url3
    scrape_mars_dict['hemisphere_4'] = url4


    return scrape_mars_dict