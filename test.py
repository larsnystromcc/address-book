#!/usr/bin/python

## variables
instance="cc-usw2b-dmz01-apache"

## output html function
def output_html():
    print("Content-type: text/html")
    print("")
    print("<html><head>")
    print("")
    print("</head><body>")
    print("CloudCoders.guru")
    print("<p>")
    print(instance)
    print("</body></html>")

## main function
def main():

    output_html()

if __name__ == "__main__":
    main()