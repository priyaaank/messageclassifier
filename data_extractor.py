# -*- coding: utf-8 -*-
import re
import io

class DataExtractor:

    def __init__(self, filename="./data/SahajChat.txt"):
        self.filename = filename
        self.sender_list = UniqueSenders()
        self.msg_regex = "\d{2}/\d{2}/\d{2},\s+\d{1,2}:\d{1,2}\s(A|P)M"
        self.messages = []

    def extract(self):
        f = io.open(self.filename, 'r')
        curr_message = ""
        for line in f:
            if len(curr_message) > 0 and re.search(self.msg_regex, line):
                m = Message(curr_message).process()
                id = self.sender_list.add_sender_if_missing(m.sender_name())
                m.update_sender_id(id)
                self.messages.append(m)
                curr_message = ""
            curr_message += line
        #self.sender_list.show()
        #[msg.show() for msg in self.messages]

class WordList:

    def __initialize__(self):
        self.unq_word_list = {}

    def add_words(self):
        pass

class UniqueSenders:

    def __init__(self):
        self.senders = {}

    def add_sender_if_missing(self, sender):
        if sender not in self.senders.keys():
            self.senders[sender] = len(self.senders.keys())+1
        return self.senders[sender]

    def show(self):
        for key in self.senders.keys():
            print "%s - [%s]"%(key, self.senders[key])

class Message:

    def __init__(self, message_string):
        self.message_string = message_string
        self.sender = ""
        self.time = ""
        self.txt_msg = ""
        self.sender_id = -1

    def process(self):
        if self.message_string.find("-") != -1 and self.message_string.split("-")[1].find(":") != -1:
            self.time, self.sender = self.message_string.split("-",1)
            self.sender, self.txt_msg = self.sender.split(":",1)
        return self

    def sender_name(self):
        return self.sender.replace(" ","").replace(u"\u202C","").replace(u"\u202A","")

    def update_sender_id(self, id):
        self.id = id

    def show(self):
        print ("--------------------------")
        print self.time
        print self.sender
        print self.txt_msg
        print ("--------------------------")


if __name__ == "__main__":
    DataExtractor().extract()
