Program: LinkedIn Search Simplifer 
Version: 1.0
By: Hamid Badamgul


UPDATE: 3/24/2020
LinkedIn has implemented the infinite scroll; therefore, I adjusted the TitleParser.py file to make it work with the current LinkedIn scroll method.
Also modified code on bottom of README to make it work with LinkedIn's infinite scroll. 


BACKSTORY: 

Using LinkedIn for my job search was a great option and it gave good results; HOWEVER, it was still lacking something in the given results. 
If I searched for a software engineer job and selected 'entry' level experience I would still get titles with Senior or Lead jobs or the description included 1-10 years of experience in the certain fields. 
So, an idea came to me and I decided to see if I can simplify the results even further. That's where I got into Web Scrapping using Python. 
It was really fun, and many obstacles got in the way, but I didn't quit and overcame them. Now, I finally got a GUI version and a Command Line version that users can use. It's still lacking in some tests, but I'll get on them eventually. 
The idea was to use Web Scrapping library like BeautifulSoup4, and Selenium to get a URL and open chrome driver and start my scrapping by first loading all the pages, in this case pressing "Click More" button until we get all the results. 
Then, I grabbed the data and stored the info that I needed, which were the Title, Company name, and their Description. Applying a certain keyword to omit from the data, I managed to output my results in a text file, which contained the data I wanted. Therefore, if I had 200 results, I would get 70 results that match my requirements. Then, I used that file to scroll past the unnecessary titles and look at the ones provided in my text file. 
This simplified and reduced my job search.

 
-------------------------------------------------------------------------------
NOTICE: As of now, this works when you are NOT signed in LinkedIn. If you are signed out, then you should be fine. 
-------------------------------------------------------------------------------

Usage with GUI:

If you download the application, make sure the folder(dist) contains the two things, 1.) chromedriver, and 2.) the App. 
Now, you can launch it and get the URL from LinkedIn, and perform your search on their site, for example: Enter the job in the search field and then the city, state, and the country in their respective fields.
Once, you get those results go ahead and chose your "Date Posted" option, and "Experience Level". 
After you do all of that, copy the URL and paste it on the "URL" field of the program. 
Then specify the necessary keyword that you do not want results to contain, for instance, if I did not want to see the titles with "Lead", "Senior", or "Manager", I would input these keywords like so: Lead|Senior|Manager

Similarly with the next two input fields, if the description contains "2+ years" or 2-4 years", I would then input them like so: 2\+ years|2-4 years. Yes, include a backslash on the plus sign.

Then, some companies I do not like seeing when I do my search are 'Revature' and 'The Job Network', so I include them in the company input field like so: The Job Network|Revature


NOTE: No need for periods at the end of the keywords, and most importantly don't leave any of the fields blank, instead, type in those blank fields "None" if you do not want to omit any title, company, or description.


After the green progress bar loads, you can then exit out of the program and the "Results.txt" should appear in the same folder. 
Open it, and you will get your desired outcome.

IMPORTANT: As of now, since I manually implemented a progress bar for the first time in GUI, it can handle about 300 search results. Also, sometimes it freezes, just restart the app. 

Of course, you can tweak the keyword further if some things managed to slip past. Then, you can have them side by side with the LinkedIn open one one side and your text open on the other.
Then, you can use ctrl-f to find the desire names from your 
"Results.txt" file. Tip: on the website of LinkedIn, make sure to load all the "more button" first, before using ctrl-f.  
That's it!


-------------------------------------------------------------------------------

UPDATE: Commented out the GUI, you can use more search results (ex. 1000) with the command line only.

Usage with the command line:

ONLY If you can read and write Python code, then you could modify the code to be able to make it work on the command line, which shouldn't be too hard. 


You may need to install BeautifulSoup4, Selenium and download chromedriver. I used: pip install <name>, and downloaded chromedriver from its website: https://chromedriver.chromium.org/downloads


NOTE: There might be some libraries not included with your Python version, go ahead and install them too if required.


Open AppName.py in your IDE, there you can modify the path to your correct paths, and modify the searches that you want to omit from the results.


Once you get the paths set up and input the necessary search keyword to omit, you should be able to run: python AppName.py 


Then, the loading will complete and you should see the "Results.txt" in the same folder. 


FINAL NOTES:

-You can provide your own regex in the input fields, if you have some knowledge with them. 
-After getting the Results.txt, when you go back to the LinkedIn page to start searching for you matches, and don't want to keep pressing "See More Jobs" button, I have a simple solution for you that can help. On the page, open "Developer Tools" located at the far top right corner of Chrome, click the three dots and you should find the dev tools under "More Tools" area. Then go to the console and past this code and hit enter. 

UPDATE: 3/24/2020 - This won't work on the current LinkedIn scroll method, as they changed it to infinite scrolling. Therefore, the new code is below the current code.  

[BEGIN CODE] //WON'T WORK 
//This function helps us get all the elements, in order to click on them after certain intervals, this case being every 1 second. 
function clickMore()
 
{
	
	var c = document.getElementsByClassName('see-more-jobs'); 
    
	for(var i = 0; i < c.length; i++)
	{
        
		c[i].click();      
    
	}       

}


setInterval(clickMore, 1000); 

[END CODE]   

UPDATED CODE - Infinite Scrolling

[BEGIN CODE]

var Scroll = function scrollDown() 
{

    
	window.scrollTo(0,document.body.scrollHeight);


}

var Interval = setInterval(Scroll, 1000);

//To STOP the scroll once it reached the end of the infinite scroll, type this in the dev tool:
window.clearInterval(Interval);

[END CODE]

This code loads all of the contents of the page, by clicking on the "See More Jobs" (NEW: Infinite Scrolling) button, this way you can easily use Ctrl-F to locate your matches from the .txt file. 
 
---------------------
| HAPPY SEARCHING!  |
---------------------