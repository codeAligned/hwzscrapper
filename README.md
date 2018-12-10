# Scrape any HWZ post!

Simply input any valid HWZ forum thread into the CLI tool and you will get back a CSV file containing:
- username
- date posted
- post content
- sentiment subjectivity
- sentiment polarity

### Requirements
1. Python 3.x

### How to use

1. `git clone https://github.com/jaabberwocky/hwzscrapper.git`
2. Install requirements: `pip install -r requirements.txt`
3. Use it! `python hwzscrape.py <url>`

### Example
```
python hwzscrape.py 'https://forums.hardwarezone.com.sg/eat-drink-man-woman-16/what-wrong-my-bf-teo-kb-he-only-likes-women-big-boops-sluts-5952396.html'
```
![command-line](https://s3-ap-southeast-1.amazonaws.com/tobiasleong/Screenshot+2018-12-10+at+23.43.20.png)

Contents of CSV:
![csv-file](https://s3-ap-southeast-1.amazonaws.com/tobiasleong/Screenshot+2018-12-10+at+23.43.05.png)

Find more options by typing
```bash
python hwzscrape.py --help
```
