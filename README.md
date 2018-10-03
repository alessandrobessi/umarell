# umarell

umarell is a lightweight decorator that can be seamlessly integrated in all your Python projects to
 log
 the performance of your functions.
 
 ### Usage
 
Its usage is straightforward. You just need to:
 1. include the umarell module in your project folder
 2. import the module
 3. apply the decorator on top of functions' definition

```python
from umarell import umarell

@umarell
def my_function():
    ...
``` 

Each time a function gets called, umarell logs its execution time leveraging the built-in `logging`
 module. Try to run `example.py` to get a gist of it.
 
### What the heck umarell means?
_Umarell (Italian pronunciation: [umaˈrɛlː]; modern rivisitation of the Bolognese dialect word 
umarèl [umaˈrɛːl]) is a term popular in Bologna referring specifically to men of retirement age 
who pass the time watching construction sites, especially roadworks – stereotypically with hands clasped behind their back and offering unwanted advice._

![Umarell](https://commons.wikimedia.org/wiki/File:Umarells.jpg#/media/File:Umarells.jpg 
"Wild Umarells in Bologna")

Source: [Wikipedia](https://en.wikipedia.org/wiki/Umarell)
 
 
 
 
