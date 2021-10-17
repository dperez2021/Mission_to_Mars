# Mission_to_Mars
## Overview

The mission with this project is to learn web scraping methods in order to extract data from the NASA Science Mars Exploriation website using 'Chrome Developer' tools to identify the HTML Components, 'Beautiful Soup/Splinter' to automate a web browser and perform the scrape, 'MongoDB' to store the data, and finally 'Flask' to create a web application to display the data. Through the process, the goal was to develop an app to scrape the following information about the planet Mars:
  - Latest News
  - Featured Image
  - Facts about the planet
  - Images of the Hemispheres

## Deliverable 1
### Scrape High-Resolution Mars Hemisphere Images and Titles

This deliverbale was done by creating a file in jupyter notebook to perform the scraping activity and pull the requested information needed to build the app.
  
![Deliverable1](https://user-images.githubusercontent.com/88256967/137648068-63c74764-7ed0-4bc9-90c1-f64eeeed97c6.PNG)

## Deliverable 2 
### Update the Web App with Mars Hemisphere Images and Titles

The next deliverable required us to export our Jupyter Notebook file into a Python scrpt. Using this script as the starting point, we started to define the scraping process using Visual Studo Code to edit our Python script. We added functions to scrape through the website and loop through the HTML tags to return the information used to create a database to be stored in MongoDB.

![Deliverable2](https://user-images.githubusercontent.com/88256967/137648174-afa50992-5b42-42cd-b345-23a7c59aebec.PNG)

Using the database in Mongo, we create a Flask app to connect to the information and create our app routes. These routes help to display the information on the homepage and will perform the scraping of new data using the codes that we wrote in the Python script.

Next, we integrate Mongo into the web app so that the data stored is updated every time the script, "scraping.py" is run.

After we create an HTML template to customize the web app and use Bootstrap components to enhance the HTML and CSS in the file.

## Deliverable 3:
### Add Bootstrap 3 Components

To finalize this project the final requirement is to make the following changes through Bootstrap components to customize the view of the page:

(1 & 2) Update the color of the header by adding a gradient color shading and changing the color of the scrape button. In addition on the same line of code we can change the background color of the entire webpage by modifiying the <body> tage with <body style="background-color: rgba(143, 137, 135, 0.945); color:black">.
This resulted in a grey background and black text.

Orginal Header:

![Original_Header](https://user-images.githubusercontent.com/88256967/137648387-12a2f271-46c0-430f-b3f8-1ac2a9402795.png)

After Bootstap Customization:

![revised_header](https://user-images.githubusercontent.com/88256967/137648408-7a1ca833-3177-4548-a09c-786aea0abda9.PNG)

See code updated below:

![CustomizingD3A](https://user-images.githubusercontent.com/88256967/137648371-7ffbb820-1783-499e-82bf-13335cbc7eec.PNG)

(3) Change the orientation of the hemispher images to a single ribbon by changing the grid from col-md-6 to col-md-3

![Mars Hemisphere](https://user-images.githubusercontent.com/88256967/137648470-929105a5-ec0f-43d4-81d6-03a0f1efec44.PNG)

(4) Confirm the website is responsive through mobile devices. I checked using IPAD PRO device.
 
  ![IPAD_PRO_COMPATABLE](https://user-images.githubusercontent.com/88256967/137648574-7e31d979-8d31-4ded-ad79-313a975c33b7.PNG)


## Summary

Complete scrape result once the pythong app.py is run, then the http://127.0.0.1:5000/ site is searched in the URL this will bring up the code we completed in index.html saved in template folder.
  
![MISSION_TO_MARS_WEBSITE](https://user-images.githubusercontent.com/88256967/137648625-4807dae0-9553-458c-be48-f3f17c53e0e4.PNG)






