
# import the HTMLParsermodule
from html.parser import HTMLParser

class htmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global metacount
        print("Start tag: ", tag)

        if tag == 'meta':
            metacount += 1

        pos = self.getpos()
        print("At line: ", pos[0], " position ",pos[1])


        print("\tAttributes:")
        for attr in attrs:
            print("\t", attr)


    def handle_endtag(self, tag):
        print("End tag: ", tag)
        pos = self.getpos()
        print("At line: ", pos[0], " position ",pos[1])

    def handle_data(self, data):
        print("Data: ", data)
        pos = self.getpos()
        print("At line: ", pos[0], " position ",pos[1])

    def handle_comment(self, data):
        print("Comment: ", data)
        pos = self.getpos()
        print("At line: ", pos[0], " position ", pos[1])




metacount = 0

def main():

    # instantiate the parser and feed it some HTML file
    parser = htmlParser()

    with open("samplehtml.html", 'r') as f:
        contents = f.read()
        parser.feed(contents)

    print(metacount)

if __name__ == "__main__":
    main()