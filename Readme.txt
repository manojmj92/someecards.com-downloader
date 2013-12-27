Multi threaded python program to download all pictures from someecards.com,category wise.

Download pictures in each category to a seperate folder.
Incase the script is run again, it does not download duplicates.

If the program finds 40 duplicate files in a row, it assumes that all the comics are downloaded
and stops downloading that specific category.

Each thread is used to parse and download data from each page of a single category.

Usage:

Just run the python script and input the number of the category you want to download.
Enter 0 to download all categories.

Dependencies:

BeautifulSoup 4

Note:

I had to include time.sleep(2) so that the CDN does not block the IP when continous
requests are given.