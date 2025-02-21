#alias
from day2 import Human
from day2 import sayHello
from matematik import topla as toplamaIslemi
#built-in modules
import random
from selenium import webDriver
#selenium u yüklememe rağmen hata verdi orda ctrl shift p ile doğru python ortamıma girdim yani seleniumu yüklediğim ortama sanal!

#package
 
print(toplamaIslemi(10,20))

print(random.randint(0,100))

human1 = Human("Mirza")
human1.talk("Merhaba")

chromeDriver = webDriver.Chrome()
#packages
