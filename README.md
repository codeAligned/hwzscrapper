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
This is the thread we want to scrape.

![hwz-thread](https://s3-ap-southeast-1.amazonaws.com/tobiasleong/hwzthread.png)

```
python hwzscrape.py 'https://forums.hardwarezone.com.sg/eat-drink-man-woman-16/do-u-mind-ur-gf-earn-2-times-ur-salary-but-everything-u-paid-during-dating-5951889.html'
```
![command-line](https://s3-ap-southeast-1.amazonaws.com/tobiasleong/commandline.png)

Contents of CSV:
![csv-file](https://s3-ap-southeast-1.amazonaws.com/tobiasleong/csv.png)

Find more options by typing
```bash
python hwzscrape.py --help
```
