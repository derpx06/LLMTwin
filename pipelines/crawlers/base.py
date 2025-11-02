from abc import ABC, abstractmethod
from tempfile import mkdtemp
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()
class BaseCrawler(ABC):
    model