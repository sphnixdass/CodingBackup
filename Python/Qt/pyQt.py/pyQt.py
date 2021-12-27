from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/usr/local/share/gecko_driver/geckodriver")
driver.get("file:///data/Backup/ebooks/50-Tips-and-Tricks-for-MongoDB-Developers_001.pdf#page=10")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


# import sys
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWebEngine import *
# from PySide2.QtWebEngineWidgets import *

# from PySide2.QtWidgets import *
# import PySide2

# app = QApplication(sys.argv)
# web = QWebEngineView()
# web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
# web.load(QUrl('/data/Backup/ebooks/50-Tips-and-Tricks-for-MongoDB-Developers_001.pdf'))
# web.show()
# app.exec_()


# # import PyQt5
# # from PyQt5.QtCore import QUrl
# # from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# # from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage

# # from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
# # # from PyQt5.QtWidgets import QApplication, QWidget
# # # from PyQt5.QtWebKitWidgets import QWebView , QWebPage
# # # from PyQt5.QtWebKit import QWebSettings
# # from PyQt5.QtNetwork import *
# # import sys
# # from optparse import OptionParser


# # app = QApplication(sys.argv)
# # web = QWebView()
# # settings = QWebSettings.globalSettings()
# # settings.setAttribute(QWebSettings.PluginsEnabled, True)
# # web.load((QUrl("/data/Backup/ebooks/50-Tips-and-Tricks-for-MongoDB-Developers_001.pdf")))
# # web.show()
# # sys.exit(app.exec())


# # class MyBrowser(QWebPage):
# #     ''' Settings for the browser.'''
    
# #     def userAgentForUrl(self, url):
# #         ''' Returns a User Agent that will be seen by the website. '''
# #         return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

# # class Browser(QWebView):
# #     def __init__(self):
# #         # QWebView
# #         self.view = QWebView.__init__(self)
# #         #self.view.setPage(MyBrowser())
# #         self.setWindowTitle('Loading...')
# #         self.titleChanged.connect(self.adjustTitle)
# #         #super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&amp;)"), self.adjustTitle)

# #     def load(self,url):
# #         self.setUrl(QUrl(url))
    
# #     def adjustTitle(self):
# #         self.setWindowTitle(self.title())
    
# #     def disableJS(self):
# #         settings = QWebSettings.globalSettings()
# #         settings.setAttribute(QWebSettings.JavascriptEnabled, False)

# # app = QApplication(sys.argv)
# # view = Browser()
# # view.showMaximized()
# # view.load("www.google.com")
# # app.exec_()


# # import sys
# # from PyQt5 import QtWidgets
# # from PyQt5.QtCore import QUrl
# # from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# # from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
# # from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings


# # #from PyQt5.QtWebKitWidgets import QWebView, QWebPage
# # #from PyQt5.QtWebKit import QWebSettings
# # from PyQt5.QtNetwork import *


# # app = QApplication(sys.argv)

# # web = QWebView()
# # settings = QWebSettings.globalSettings()
# # settings.setAttribute(QWebSettings.PluginsEnabled, True)

# # # web.settings.setAttribute(QWebSettings.PluginsEnabled, True)
# # web.load(QUrl('/data/Backup/ebooks/50-Tips-and-Tricks-for-MongoDB-Developers_001.pdf'))
# # web.show()
# # # win = QMainWindow()
# # # win.setGeometry(10,10,500,500)
# # # win.setWindowTitle("Hi Dass")
# # # win.show()
# # sys.exit(app.exec_())

