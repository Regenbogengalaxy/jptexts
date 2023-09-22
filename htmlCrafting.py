#for testing purposes it just colors adjacent morphemes differently for now.

def craftHTMLmorphemeText(morphemelist):

    outputStr = ""
    cnt = 0
    for morpheme in morphemelist:

        if cnt % 2 == 0:
            outputStr = outputStr + f'<div class ="morphemeA">{morpheme}</div>'
        else:
            outputStr = outputStr + f'<div class ="morphemeB">{morpheme}</div>'
        cnt += 1
    return outputStr

def craftHTML(morphemelist):
    str_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
            background-color: linen;
            }

            .morphemeA {
                background-color: cyan;
                white-space: nowrap;

            }
            .morphemeB {
                background-color: pink;
                white-space: nowrap;
            }
            
            .flex-container {
            display: flex;
            flex-wrap: wrap;
            } 

        </style>
    </head>
    <body>
    <div class="flex-container">
    """
    str_html = str_html + craftHTMLmorphemeText(morphemelist)

    str_html = str_html + """
    </div>
    </body>
    </html>
    """
    with open("./index.html", "w", encoding="utf-8") as f:
        f.write(str_html)