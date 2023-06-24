from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import bs4 as bs
import re
from urllib.request import Request, urlopen
import nltk
import heapq #heapq
import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 1141, 731))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.text_tab = QtWidgets.QWidget()
        self.text_tab.setObjectName("text_tab")
        self.tInputText = QtWidgets.QTextEdit(self.text_tab)
        self.tInputText.setGeometry(QtCore.QRect(10, 30, 561, 471))
        self.tInputText.setFrameShape(QtWidgets.QFrame.Box)
        self.tInputText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tInputText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tInputText.setObjectName("tInputText")
        self.label_2 = QtWidgets.QLabel(self.text_tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.text_tab)
        self.label_3.setGeometry(QtCore.QRect(10, 530, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.text_tab)
        self.label_4.setGeometry(QtCore.QRect(590, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tSummerizeBT = QtWidgets.QPushButton(self.text_tab, clicked = lambda: self.btPressed("tSummerizeBT"))
        self.tSummerizeBT.setGeometry(QtCore.QRect(320, 510, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tSummerizeBT.setFont(font)
        self.tSummerizeBT.setObjectName("tSummerizeBT")
        self.tNOS = QtWidgets.QLineEdit(self.text_tab)
        self.tNOS.setGeometry(QtCore.QRect(180, 520, 113, 31))
        self.tNOS.setObjectName("tNOS")
        self.tResult = QtWidgets.QTextBrowser(self.text_tab)
        self.tResult.setGeometry(QtCore.QRect(590, 30, 541, 661))
        self.tResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tResult.setObjectName("tResult")
        self.tAudioBT = QtWidgets.QPushButton(self.text_tab, clicked = lambda: self.btPressed("tAudioBT"))
        self.tAudioBT.setGeometry(QtCore.QRect(20, 600, 111, 51))
        self.tAudioBT.setAutoFillBackground(False)
        self.tAudioBT.setObjectName("tAudioBT")
        self.tabWidget.addTab(self.text_tab, "")
        self.file_tab = QtWidgets.QWidget()
        self.file_tab.setObjectName("file_tab")
        self.label_6 = QtWidgets.QLabel(self.file_tab)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.file_tab)
        self.label_7.setGeometry(QtCore.QRect(480, 20, 161, 16))
        self.label_7.setObjectName("label_7")
        self.fSummerizeBT = QtWidgets.QPushButton(self.file_tab, clicked = lambda: self.btPressed("fSummerizeBT"))
        self.fSummerizeBT.setGeometry(QtCore.QRect(870, 0, 141, 51))
        self.fSummerizeBT.setObjectName("fSummerizeBT")
        self.label_12 = QtWidgets.QLabel(self.file_tab)
        self.label_12.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.label_12.setObjectName("label_12")
        self.fBrowseBT = QtWidgets.QPushButton(self.file_tab, clicked = lambda: self.btPressed("fBrowseBT"))
        self.fBrowseBT.setGeometry(QtCore.QRect(350, 10, 101, 41))
        self.fBrowseBT.setObjectName("fBrowseBT")
        self.fNOS = QtWidgets.QLineEdit(self.file_tab)
        self.fNOS.setGeometry(QtCore.QRect(670, 10, 113, 31))
        self.fNOS.setObjectName("fNOS")
        self.fResult = QtWidgets.QTextBrowser(self.file_tab)
        self.fResult.setGeometry(QtCore.QRect(10, 130, 1121, 551))
        self.fResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fResult.setObjectName("fResult")
        self.fileName = QtWidgets.QLabel(self.file_tab)
        self.fileName.setGeometry(QtCore.QRect(94, 20, 241, 21))
        self.fileName.setText("")
        self.fileName.setObjectName("fileName")
        self.fAudioBT = QtWidgets.QPushButton(self.file_tab, clicked = lambda: self.btPressed("fAudioBT"))
        self.fAudioBT.setGeometry(QtCore.QRect(870, 60, 141, 51))
        self.fAudioBT.setObjectName("fAudioBT")
        self.tabWidget.addTab(self.file_tab, "")
        self.url_tab = QtWidgets.QWidget()
        self.url_tab.setObjectName("url_tab")
        self.label_8 = QtWidgets.QLabel(self.url_tab)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.url_tab)
        self.label_9.setGeometry(QtCore.QRect(420, 30, 171, 16))
        self.label_9.setObjectName("label_9")
        self.uSummerizeBT = QtWidgets.QPushButton(self.url_tab, clicked = lambda: self.btPressed("uSummerizeBT"))
        self.uSummerizeBT.setGeometry(QtCore.QRect(780, 10, 131, 51))
        self.uSummerizeBT.setObjectName("uSummerizeBT")
        self.label_10 = QtWidgets.QLabel(self.url_tab)
        self.label_10.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.label_10.setObjectName("label_10")
        self.uInputURL = QtWidgets.QLineEdit(self.url_tab)
        self.uInputURL.setGeometry(QtCore.QRect(100, 20, 291, 31))
        self.uInputURL.setObjectName("uInputURL")
        self.uNOS = QtWidgets.QLineEdit(self.url_tab)
        self.uNOS.setGeometry(QtCore.QRect(600, 20, 113, 31))
        self.uNOS.setObjectName("uNOS")
        self.uResult = QtWidgets.QTextBrowser(self.url_tab)
        self.uResult.setGeometry(QtCore.QRect(10, 120, 1121, 581))
        self.uResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.uResult.setObjectName("uResult")
        self.uAudioBT = QtWidgets.QPushButton(self.url_tab, clicked = lambda: self.btPressed("uAudioBT"))
        self.uAudioBT.setGeometry(QtCore.QRect(970, 10, 121, 51))
        self.uAudioBT.setObjectName("uAudioBT")
        self.tabWidget.addTab(self.url_tab, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 1121, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft Himalaya")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fpath = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEXT SUMMARIZER"))
        self.label_2.setText(_translate("MainWindow", "Input Text"))
        self.label_3.setText(_translate("MainWindow", "Number of sentences"))
        self.label_4.setText(_translate("MainWindow", "Summarized Text"))
        self.tSummerizeBT.setText(_translate("MainWindow", "Summarize"))
        self.tAudioBT.setText(_translate("MainWindow", "Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.text_tab), _translate("MainWindow", "TEXT"))
        self.label_6.setText(_translate("MainWindow", "Input File"))
        self.label_7.setText(_translate("MainWindow", "number of sentences"))
        self.fSummerizeBT.setText(_translate("MainWindow", "Summarize"))
        self.label_12.setText(_translate("MainWindow", "Summarized Text"))
        self.fBrowseBT.setText(_translate("MainWindow", "Browse"))
        self.fAudioBT.setText(_translate("MainWindow", "Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.file_tab), _translate("MainWindow", "FILE"))
        self.label_8.setText(_translate("MainWindow", "Enter URL"))
        self.label_9.setText(_translate("MainWindow", "Number of Sentences"))
        self.uSummerizeBT.setText(_translate("MainWindow", "Summarize"))
        self.label_10.setText(_translate("MainWindow", "Summarized Text"))
        self.uAudioBT.setText(_translate("MainWindow", "Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.url_tab), _translate("MainWindow", "URL"))
        self.label.setText(_translate("MainWindow", "Text Summarizer"))

    def btPressed(self, button):
        
        if button == "tSummerizeBT":
            fullText = self.tInputText.toPlainText()
            tnos = self.tNOS.text()
            if fullText == "" and tnos == "":     
                self.showPopup("Enter Text and Number of Sentences")
            elif fullText == "" and tnos != "":     
                self.showPopup("Enter Text")
            elif fullText != "" and tnos == "":     
                self.showPopup("Enter Number of Sentences")
            elif not tnos.isnumeric():
                self.showPopup("Number of Sentences should be NUMERIC")
            else:
                self.textSum(fullText, tnos)

        elif button == "tAudioBT":
            try:
                self.audio(self.tTextSummerised)
            except:
                self.showPopup("Summerized data unavailable")

        elif button == "fAudioBT":
            try:
                self.audio(self.fTextSummerised)
            except:
                self.showPopup("Summerized data unavailable")

        elif button == "fBrowseBT":
            self.browseFile()

        elif button == "fSummerizeBT":
            fnos = self.fNOS.text()
            if self.fpath == "" and fnos == "":     
                self.showPopup("Enter File and Number of Sentences")
            elif self.fpath == "" and fnos != "":     
                self.showPopup("Enter File")
            elif self.fpath != "" and fnos == "":     
                self.showPopup("Enter Number of Sentences")
            elif not fnos.isnumeric():
                self.showPopup("Number of Sentences should be NUMERIC")
            else:
                self.fileSum(self.fpath, fnos)

        elif button == "uAudioBT":
            try:
                self.audio(self.uTextSummerised)
            except:
                self.showPopup("Summerized data unavailable")

        elif button == "uSummerizeBT":
            url = self.uInputURL.text()
            unos = self.uNOS.text()
            if url == "" and unos == "":     
                self.showPopup("Enter URL and Number of Sentences")
            elif url == "" and unos != "":     
                self.showPopup("Enter URL")
            elif url != "" and unos == "":     
                self.showPopup("Enter Number of Sentences")
            elif not unos.isnumeric():
                self.showPopup("Number of Sentences should be NUMERIC")
            else:
                self.urlSum(url, unos)

    def browseFile(self):
        self.fpath = QFileDialog.getOpenFileName(None, "Open File", "", "*.txt")
        fname = self.fpath[0].split("/")
        fname = fname[len(fname)-1]
        if fname:
            self.fileName.setText(fname)

    def showPopup(self, msg):
        popupBox = QMessageBox()
        popupBox.setWindowTitle("ERROR")
        popupBox.setText(msg)
        popupBox.setIcon(QMessageBox.Critical)
        popupBox.exec_()

    def infoPopup(self, msg):
        popupBox = QMessageBox()
        popupBox.setWindowTitle("ERROR")
        popupBox.setText(msg)
        popupBox.setIcon(QMessageBox.Information)
        popupBox.exec_()

    def Summerizer(self, text, n):
        text = re.sub(r'\[[0-9]*\]'," ",text)
        text = re.sub(r'\s+'," ",text)
        sentences = nltk.sent_tokenize(text)
        cleanText = text.lower()
        cleanText = re.sub(r'\W',' ',cleanText)
        cleanText = re.sub(r'\d',' ',cleanText)
        cleanText = re.sub(r'\s+',' ',cleanText)

        stopWords = nltk.corpus.stopwords.words("english")
        word2count = {}
        for word in nltk.word_tokenize(cleanText):
            if word not in stopWords:
                if word not in word2count.keys():
                    word2count[word] = 1
                else:
                    word2count[word] += 1
        maxCount = max(word2count.values())
        for key in word2count.keys():
            word2count[key] = word2count[key]/maxCount

        sent2score = {}
        for sentence in sentences:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word2count.keys():
                    if len(sentence.split(" "))<25:
                        if sentence not in sent2score.keys():
                            sent2score[sentence] = word2count[word]
                        else:
                            sent2score[sentence] += word2count[word]

        bestSentences = heapq.nlargest(n,sent2score,key = sent2score.get)
        return bestSentences

    def urlSum(self, url, unos):
        req = Request(url, headers = {"User-Agent": 'Mozilla/5.0'})
        source = urlopen(req,timeout = 10).read()
        soup = bs.BeautifulSoup(source,"lxml")
        text = ""
        for paragraph in soup.find_all('p'):
            text += paragraph.text
        data = self.Summerizer(text,int(unos))
        self.uTextSummerised = ""
        count = 0
        for sentence in data:
            self.uTextSummerised += sentence
            count += 1
        if count<int(unos):
            self.infoPopup("There are only " + str(count) + " summerized sentences")
        self.uResult.setText(self.uTextSummerised)

    def textSum(self, fullText, tnos):
        text = ""
        for sentence in fullText.split("."):
            text += sentence + ". "
        data = self.Summerizer(text,int(tnos))
        self.tTextSummerised = ""
        count = 0
        for sentence in data:
            self.tTextSummerised += sentence
            count += 1
        if count<int(tnos):
            self.infoPopup("There are only " + str(count) + " summerized sentences")
        self.tResult.setText(self.tTextSummerised)

    def fileSum(self, path, fnos):
        file = open(path[0], "r")
        fullText = file.read()
        text = ""
        for sentence in fullText.split("."):
            text += sentence + ". "
        data = self.Summerizer(text,int(fnos))
        self.fTextSummerised = ""
        count = 0
        for sentence in data:
            self.fTextSummerised += sentence
            count += 1
        if count<int(fnos):
            self.infoPopup("There are only " + str(count) + " summerized sentences")
        self.fResult.setText(self.fTextSummerised)

    def audio(self, data):
        if data == None or data =="":
            self.showPopup("Summerized data unavailable")
        else:
            data = data.replace("."," ")
            engine.say(data)
            engine.runAndWait()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
