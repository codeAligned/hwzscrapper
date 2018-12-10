# Scrape any HWZ post!

Simply input any valid HWZ forum thread into the CLI tool and you will get back a CSV file containing:
- username
- date posted
- post content
- sentiment subjectivity
- sentiment polarity

## Requirements
1. Python 3.x
2. python in PATH

## How to use

Type the following into your command-line (e.g. bash,cmd)

### Example
```bash
python hwzscrape.py "https://forums.hardwarezone.com.sg/eat-drink-man-woman-16/shocking-guardian-tampines-mart-closed-shop-5861249.html"
```

Find more options by typing
```bash
python hwz_scrape.py --help
```