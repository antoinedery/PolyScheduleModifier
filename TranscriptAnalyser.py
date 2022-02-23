import time
import PyPDF2
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageScraper import createCoursesDictionary
from EmailSender import sendEmailTranscriptAnalyser
from User import User

class TranscriptAnalyser:
    driver:webdriver
    courses = []
    user = User()

    def runTranscriptAnalyser(self, user):
        self.user = user
        createCoursesDictionary()
        while(len(self.courses) > 0):
            print("Program is running...")
            self.openBrowser()
            self.logIntoStudentAccount()
            self.downloadPDF()
            time.sleep(30)

    def openBrowser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        prefs = {"plugins.always_open_pdf_externally": True,
                "download.default_directory": dir_path}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=chrome_options)
        url = 'https://dossieretudiant.polymtl.ca/WebEtudiant7/poly.html'
        self.driver.get(url)


    def logIntoStudentAccount(self):
        self.driver.find_element(By.ID, "code").send_keys(self.user.username)
        self.driver.find_element(By.ID, "nip").send_keys(self.user.password)
        self.driver.find_element(By.ID, "naissance").send_keys(self.user.dob)
        self.driver.find_element(
            By.XPATH, "//input[@type='submit' and @value='Connexion']").click()

    def downloadPDF(self):
        self.driver.find_element(By.NAME, "btnBulCumul").click()
        time.sleep(5)
        self.parsePDF()

    def parsePDF(self):
        fileName = [filename for filename in os.listdir(
            '.') if filename.startswith("bulletin_cumulatif-")]
        pdfFile = open(fileName[0], 'rb')
        pdfReaderObj = PyPDF2.PdfFileReader(pdfFile)
        content = ''
        for page in range(0, pdfReaderObj.numPages):
            content += (pdfReaderObj.getPage(page).extractText())

        contentList = content.split()
        foundGrades = {}
        courseCopy = self.courses.copy()
        for course in courseCopy:
            if(course not in createCoursesDictionary.courses):
                print("The course " + course + " does not exist.")
                self.courses.remove(course)
            index = 0
            index = contentList.index(course)
            while(contentList[index] != str(createCoursesDictionary.courses[course])):
                index += 1

            possibleGrades = {'A*', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D'}
            if(contentList[index+1] in possibleGrades):
                foundGrades[course] = contentList[index+1]
                self.courses.remove(course)
            else:
                print("No grade for " + course + '.')

        if(len(foundGrades) > 0):
            sendEmailTranscriptAnalyser(self.user.email, foundGrades)
