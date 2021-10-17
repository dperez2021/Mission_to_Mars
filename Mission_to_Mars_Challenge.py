#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import pymongo


# In[20]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[21]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[22]:


#10.3.3 Set Up HTMP Parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[23]:


slide_elem.find('div', class_='content_title')


# In[24]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[25]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images
# 

# In[26]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[27]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[28]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[29]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[30]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[31]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[32]:


df.to_html()


# ### Visit the NASA Mars News Site

# In[33]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[34]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[35]:


slide_elem.find('div', class_='content_title')


# In[36]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[37]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[38]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[39]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[40]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[41]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[42]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[43]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[44]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[45]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[46]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[47]:


# Parse the data
hemi_html = browser.html
hemi_soup = soup(hemi_html, 'html.parser')

# Retrieve all items for hemispheres information
items = hemi_soup.find_all('div', class_='item')


# In[48]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []



# In[49]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
main_url = "https://astrogeology.usgs.gov/"

# Create loop to scrape through all hemisphere information
for x in items:
    hemisphere = {}
    titles = x.find('h3').text
    # create link for full image
    link_ref = x.find('a', class_='itemLink product-item')['href']
    # Use the base URL to create an absolute URL and browser visit
    browser.visit(main_url + link_ref)
    # parse the data
    image_html = browser.html
    image_soup = soup(image_html, 'html.parser')
    download = image_soup.find('div', class_= 'downloads')
    img_url = download.find('a')['href']
    
    print(titles)
    print(img_url)
    
    # append list
    hemisphere['img_url'] = img_url
    hemisphere['title'] = titles
    hemisphere_image_urls.append(hemisphere)
    browser.back()


# In[50]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[51]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




