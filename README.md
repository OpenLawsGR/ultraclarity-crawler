# ultraclarity-crawler
A scrapy crawler that allows for downloading greek laws from yperdiavgeia.gr. Laws (pdf files of the Government Gazzette) are downladed from the National Printing Service, however the crawler depends on the yperdiavgeia.gr law search page structure.

## Dependencies
The crawler depends on the popular python framework scrapy (tested with version 1.0.3). Installation instructions can be found [here](http://doc.scrapy.org/en/1.0/intro/install.html)

## Usage Example
Move into the "crawler" directory and use one of the following syntax patterns:

> scrapy crawl ultraclarity

to download laws published the current year

> scrapy crawl ultraclarity -a year=2010,2011

to download laws published within a range (from 2010 to 2011 in this example)

> scrapy crawl ultraclarity -a year=2014

to download laws published a specific year (2014 in this example)
