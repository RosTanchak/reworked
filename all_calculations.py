import sys
from itertools import izip, islice, tee
import math
import time
import textwrap

from nltk import ngrams


class All_calculations():
    def __init__(self, text):
        self.readyText = text

    def splitText(self, n):
        # if self.isSliced:
        #     slicedtext = self.readyText[self.startIn:self.startIn + self.finishIn]
        # else:
        splittedText = []
        n_grams = ngrams(list(self.readyText), n)
        for gram in n_grams:
            splittedText.append(gram[0]+gram[1]+gram[2]+gram[3])
        return splittedText

    #this func is for calc f value particular/general
    def calcf(self, valuesF):
        values_f = []
        for item in range(len(valuesF)):
            values_f.append(valuesF[item]/len(self.originalText))
        #values_f = [item / len(valuesF) for item in valuesF]
        return values_f

    #NEW SYMBOLS TAB(4th tab)
    #this function run into text and match all first time userd symbols or
    #ngramms as 1 and already seen as 0
    def calcNewSymbols(self, text):
        #In this loop, finally all matched indexes is set to 1 other is 0
        #check whether firs tTimeM atchedItems index = index of readyText and set 1
        #or 0
        readyItems = []
        binaryItems = []
        # binaryItems.append(1)
        # item = 1
        #for item in range(1, len( self.readyText)):
        # while item < len(text):
        #     try:
        #         result = text[:item].index(text[item])
        #         item+=1
        #         binaryItems.append(0)
        #     except ValueError:
        #         item+=1
        #         binaryItems.append(1)
        for item in text:
            try:
                result = readyItems.index(item)
                binaryItems.append(0)
                readyItems.append(item)
            except ValueError:
                binaryItems.append(1)
                readyItems.append(item)
        self.newWordsText = binaryItems
        return self.newWordsText

    #this function is copy pasted from parent projecs as it is
    #it shoul count P(x) in interval from [1;0], so be attentive
    def calculate_P_tab4(self):
        result = []
        summary = 0
        for item in self.newWordsText:
            if item:
                summary += 1
        value = 1 / summary
        current = 0
        for item in self.newWordsText:
            if item:
                current += value
            result.append(current)
        return result

    #this function chunks readyText for intervals(which value we get from  input)
    def chunksIntervals(self):
        self.getFromLineEdit()
        self.chunkedText = zip(*[iter(self.newWordsText)] * self.NumberOfIntervalsItems)
        self.get_p_tab3()

    #this function is copied from c# parent. No matter how it works
    def get_p_tab3(self):
        result = []
        for index in range(len(self.chunkedText)):
            summary = 0
            for item in self.chunkedText[index]:
                if item:
                    summary+=1
            result.append(summary)
        for item in range(len(result)):
            result[item] = result[item]/sum(self.newWordsText)
        self.p_pad3 = sorted(result, reverse = True)
        self.get_P_tab3()

    #this function is copied from c# parent. No metter how it works(on previous interval get value)
    #takes sum of new words from previous intervals and get 1 - sum  new words on  prev intervals / general_summary
    def get_P_tab3(self):
        result = []
        current_p = 1.0
        for index in range(len(self.chunkedText)):
            summary = 0
            for item in self.chunkedText[index]:
                if item:
                    summary+=1
            result.append(summary)
        new_result = []
        new_result.append(current_p)
        general_summary = sum(result)
        for item in range(1, len(result)):
            new_result.append( current_p - (sum(result[0:item])/general_summary))
        self.P_pad3 = new_result
        self.calcAverage()

    #this function calculate average items
    def calcAverage(self):
        self.listOfAverages = []
        average = int(self.NumberOfIntervalsItems)
        for item in range(len(self.chunkedText)):
            self.listOfAverages.append(average)
            average += self.NumberOfIntervalsItems
        self.fillTableTab3()

    #LAst tab(2, second Dti)
    #this function make chunks depent on smth
    def calcSecTab (self):
        fn = 1
        st = 0
        dti = {}
        #calc dti
        for item in range(1, len(self.newWordsText)):
            fn = item
            if self.newWordsText[item]:
                dti[item]= (fn - st - 1)
                st = item
        autoChunk = []
    #set intervals
        for item in dti:
            if item in autoChunk:
                autoChunk[item] += 1
            else:
                autoChunk.append(item)
        self.result_tap_2 = sorted(autoChunk, reverse = True)
        self.calc_Big_P_tab2()
        self.fillTableTab2()

    #this func calc P(x) for tab2
    def calc_Big_P_tab2(self):
        current = 1
        summary = sum(self.result_tap_2)
        result = []
        for item in self.result_tap_2:
            result.append(current)
            current = current - (item / summary)
        #self.result_P_tap_2 = result[::1]
        self.result_P_tap_2 = result
