# YoutubeRecommendedScraper
A simple YouTube "recommended videos" scraper built to try out BeautifulSoup4 and Urllib3.

In its current form, the app will select a video on YouTube's homepage, and then navigate
to random recommended videos in the sidebar repeatedly. The title of the video is printed
out. Originally I had hopes that this would be a prototype for a larger program used to
analyze YouTube's recommendation algorithm, but running this program indicates that the 
page-loading time would be a significant bottleneck. I have some interest in understanding
the Selenium toolset as well, so writing a similar program with Selenium is a likely 
follow-up.
