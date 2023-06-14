## Web scrapping using scrappy

## 1. Create a virtual environment:
```
py -3 -m venv .venv
.venv\scripts\activate
```
## 2. Install requirements:
```
pip install -r requirements.txt
```
or
```
pip install scrapy
```
## 3. Create A Scrapy Project :
```
scrapy startproject <project_name>
```

## 4. cd into the root folder where spiders folder is located:
```
├── scrapy.cfg
└── bookscraper
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        └── __init__.py
```

## 5. Using scrapy shell to create CSS selectors:
```
pip3 install ipython
```

To open Scrapy shell use this command:
```
scrapy shell
```
## 6. Edit your scrapy.cfg file like so:
```
[settings]
default = chocolatescraper.settings
shell = ipython
```
## 7. Running scrapy spider:
```
scrapy crawl <project_name>
```
Saving the data to a JSON file we can use the -O option, followed by the name of the file:
```
scrapy crawl <project_name> -O myscrapeddata.json
```
CSV format:
```
scrapy crawl <project_name> -O myscrapeddata.csv
```

## Technologies & Tools Used

<li>Python</li>
<li>scrapy</li>

## References
Various sources which I have seek guidance from:
</li>
<li><a href=https://www.youtube.com/watch?v=mBoX_JCKZTE>Scrapy Course</a>
</li>
<li><a href=https://thepythonscrapyplaybook.com/freecodecamp-beginner-course>Scrapy Playbook</a>
</li>
<li><a href=https://docs.scrapy.org/en/latest/intro/tutorial.html>Scrapy documentation</a>
</li>
