from CharlotteKnn import CharlotteKnn

def main():
    msC = CharlotteKnn()

    test_data = {
        "http_^^www.cs.utexas.edu^users^dwip^cs304p^cs304p.html": {
            "words": {
                "server": {
                    "stemmed": "server"
                },
                "date": {
                    "stemmed": "date"
                },
                "monday": {
                    "stemmed": "monday"
                },
                "jan": {
                    "stemmed": "jan"
                },
                "wednesday": {
                    "stemmed": "wednesday"
                },
                "dec": {
                    "stemmed": "dec"
                },
                "cspporter": {
                    "stemmed": "cspporter"
                },
                "homepage": {
                    "stemmed": "homepag"
                },
                "important": {
                    "stemmed": "import"
                },
                "announcements": {
                    "stemmed": "announc"
                },
                "taking": {
                    "stemmed": "take"
                },
                "today": {
                    "stemmed": "today"
                },
                "home": {
                    "stemmed": "home"
                },
                "unable": {
                    "stemmed": "unabl"
                },
                "maintain": {
                    "stemmed": "maintain"
                },
                "page": {
                    "stemmed": "page"
                },
                "last": {
                    "stemmed": "last"
                },
                "couple": {
                    "stemmed": "coupl"
                },
                "days": {
                    "stemmed": "day"
                },
                "however": {
                    "stemmed": "howev"
                },
                "putting": {
                    "stemmed": "put"
                },
                "link": {
                    "stemmed": "link"
                },
                "dr": {
                    "stemmed": "dr"
                },
                "porters": {
                    "stemmed": "porter"
                },
                "class": {
                    "stemmed": "class"
                },
                "related": {
                    "stemmed": "relat"
                },
                "announcement": {
                    "stemmed": "announc"
                },
                "available": {
                    "stemmed": "avail"
                },
                "following": {
                    "stemmed": "follow"
                },
                "good": {
                    "stemmed": "good"
                },
                "luck": {
                    "stemmed": "luck"
                },
                "finals": {
                    "stemmed": "final"
                },
                "next": {
                    "stemmed": "next"
                },
                "week": {
                    "stemmed": "week"
                },
                "special": {
                    "stemmed": "special"
                },
                "classes": {
                    "stemmed": "class"
                },
                "reviewing": {
                    "stemmed": "review"
                },
                "topics": {
                    "stemmed": "topic"
                },
                "covered": {
                    "stemmed": "cover"
                },
                "held": {
                    "stemmed": "held"
                },
                "painter": {
                    "stemmed": "painter"
                },
                "hall": {
                    "stemmed": "hall"
                },
                "exact": {
                    "stemmed": "exact"
                },
                "location": {
                    "stemmed": "locat"
                },
                "depend": {
                    "stemmed": "depend"
                },
                "room": {
                    "stemmed": "room"
                },
                "availibity": {
                    "stemmed": "availib"
                },
                "notes": {
                    "stemmed": "note"
                },
                "posted": {
                    "stemmed": "post"
                },
                "doors": {
                    "stemmed": "door"
                },
                "office": {
                    "stemmed": "offic"
                },
                "someone": {
                    "stemmed": "someon"
                },
                "pai": {
                    "stemmed": "pai"
                },
                "inform": {
                    "stemmed": "inform"
                },
                "timing": {
                    "stemmed": "time"
                },
                "moreover": {
                    "stemmed": "moreov"
                },
                "almost": {
                    "stemmed": "almost"
                },
                "total": {
                    "stemmed": "total"
                },
                "coverage": {
                    "stemmed": "coverag"
                },
                "hrs": {
                    "stemmed": "hrs"
                },
                "tas": {
                    "stemmed": "tas"
                },
                "porter": {
                    "stemmed": "porter"
                },
                "right": {
                    "stemmed": "right"
                },
                "upto": {
                    "stemmed": "upto"
                },
                "time": {
                    "stemmed": "time"
                },
                "final": {
                    "stemmed": "final"
                },
                "exam": {
                    "stemmed": "exam"
                },
                "need": {
                    "stemmed": "need"
                },
                "help": {
                    "stemmed": "help"
                },
                "feel": {
                    "stemmed": "feel"
                },
                "free": {
                    "stemmed": "free"
                },
                "come": {
                    "stemmed": "come"
                },
                "ask": {
                    "stemmed": "ask"
                },
                "one": {
                    "stemmed": "one"
                },
                "us": {
                    "stemmed": "us"
                },
                "glad": {
                    "stemmed": "glad"
                },
                "review": {
                    "stemmed": "review"
                },
                "mon": {
                    "stemmed": "mon"
                },
                "ai": {
                    "stemmed": "ai"
                },
                "resolutio": {
                    "stemmed": "resolutio"
                },
                "bruce": {
                    "stemmed": "bruce"
                },
                "complexity": {
                    "stemmed": "complex"
                },
                "theory": {
                    "stemmed": "theori"
                },
                "nimar": {
                    "stemmed": "nimar"
                },
                "arora": {
                    "stemmed": "arora"
                },
                "tue": {
                    "stemmed": "tue"
                },
                "parallel": {
                    "stemmed": "parallel"
                },
                "processing": {
                    "stemmed": "process"
                },
                "dwip": {
                    "stemmed": "dwip"
                },
                "banerjee": {
                    "stemmed": "banerje"
                },
                "boolean": {
                    "stemmed": "boolean"
                },
                "circuits": {
                    "stemmed": "circuit"
                },
                "question": {
                    "stemmed": "question"
                },
                "sheet": {
                    "stemmed": "sheet"
                },
                "rotating": {
                    "stemmed": "rotat"
                },
                "bits": {
                    "stemmed": "bit"
                },
                "disregarded": {
                    "stemmed": "disregard"
                },
                "somewhat": {
                    "stemmed": "somewhat"
                },
                "beyond": {
                    "stemmed": "beyond"
                },
                "scope": {
                    "stemmed": "scope"
                },
                "slides": {
                    "stemmed": "slide"
                },
                "presented": {
                    "stemmed": "present"
                },
                "lecture": {
                    "stemmed": "lectur"
                },
                "december": {
                    "stemmed": "decemb"
                },
                "th": {
                    "stemmed": "th"
                },
                "summarizing": {
                    "stemmed": "summar"
                },
                "contents": {
                    "stemmed": "content"
                },
                "whole": {
                    "stemmed": "whole"
                },
                "semester": {
                    "stemmed": "semest"
                },
                "reserve": {
                    "stemmed": "reserv"
                },
                "desk": {
                    "stemmed": "desk"
                },
                "ugl": {
                    "stemmed": "ugl"
                },
                "hope": {
                    "stemmed": "hope"
                },
                "post": {
                    "stemmed": "post"
                },
                "webpage": {
                    "stemmed": "webpag"
                },
                "soon": {
                    "stemmed": "soon"
                },
                "experiencing": {
                    "stemmed": "experienc"
                },
                "technical": {
                    "stemmed": "technic"
                },
                "difficulties": {
                    "stemmed": "difficulti"
                },
                "caused": {
                    "stemmed": "caus"
                },
                "length": {
                    "stemmed": "length"
                },
                "file": {
                    "stemmed": "file"
                },
                "click": {
                    "stemmed": "click"
                },
                "schedule": {
                    "stemmed": "schedul"
                },
                "also": {
                    "stemmed": "also"
                },
                "please": {
                    "stemmed": "pleas"
                },
                "check": {
                    "stemmed": "check"
                },
                "assignment": {
                    "stemmed": "assign"
                },
                "addendum": {
                    "stemmed": "addendum"
                },
                "questions": {
                    "stemmed": "question"
                },
                "html": {
                    "stemmed": "html"
                },
                "version": {
                    "stemmed": "version"
                },
                "postscript": {
                    "stemmed": "postscript"
                },
                "added": {
                    "stemmed": "ad"
                },
                "set": {
                    "stemmed": "set"
                },
                "stay": {
                    "stemmed": "stay"
                },
                "tuned": {
                    "stemmed": "tune"
                },
                "programming": {
                    "stemmed": "program"
                },
                "download": {
                    "stemmed": "download"
                },
                "tutorial": {
                    "stemmed": "tutori"
                },
                "prolog": {
                    "stemmed": "prolog"
                },
                "nov": {
                    "stemmed": "nov"
                },
                "computer": {
                    "stemmed": "comput"
                },
                "science": {
                    "stemmed": "scienc"
                },
                "instructor": {
                    "stemmed": "instructor"
                },
                "portercsutexasedu": {
                    "stemmed": "portercsutexasedu"
                },
                "pm": {
                    "stemmed": "pm"
                },
                "taylor": {
                    "stemmed": "taylor"
                },
                "phone": {
                    "stemmed": "phone"
                },
                "email": {
                    "stemmed": "email"
                },
                "hours": {
                    "stemmed": "hour"
                },
                "lab": {
                    "stemmed": "lab"
                },
                "discussion": {
                    "stemmed": "discuss"
                },
                "section": {
                    "stemmed": "section"
                },
                "cs": {
                    "stemmed": "cs"
                },
                "p": {
                    "stemmed": "p"
                },
                "thursday": {
                    "stemmed": "thursday"
                },
                "assignments": {
                    "stemmed": "assign"
                },
                "unique": {
                    "stemmed": "uniqu"
                },
                "number": {
                    "stemmed": "number"
                },
                "welch": {
                    "stemmed": "welch"
                },
                "course": {
                    "stemmed": "cours"
                },
                "description": {
                    "stemmed": "descript"
                },
                "lectures": {
                    "stemmed": "lectur"
                },
                "sessions": {
                    "stemmed": "session"
                },
                "includes": {
                    "stemmed": "includ"
                },
                "labdiscussion": {
                    "stemmed": "labdiscuss"
                },
                "news": {
                    "stemmed": "news"
                },
                "articles": {
                    "stemmed": "articl"
                },
                "newsgroup": {
                    "stemmed": "newsgroup"
                },
                "midterm": {
                    "stemmed": "midterm"
                },
                "test": {
                    "stemmed": "test"
                },
                "solution": {
                    "stemmed": "solut"
                },
                "ii": {
                    "stemmed": "ii"
                },
                "useful": {
                    "stemmed": "use"
                },
                "links": {
                    "stemmed": "link"
                },
                "pascal": {
                    "stemmed": "pascal"
                },
                "text": {
                    "stemmed": "text"
                },
                "format": {
                    "stemmed": "format"
                },
                "ansiiso": {
                    "stemmed": "ansiiso"
                },
                "faq": {
                    "stemmed": "faq"
                },
                "get": {
                    "stemmed": "get"
                },
                "sample": {
                    "stemmed": "sampl"
                },
                "programs": {
                    "stemmed": "program"
                },
                "tp": {
                    "stemmed": "tp"
                },
                "programmers": {
                    "stemmed": "programm"
                },
                "generic": {
                    "stemmed": "generic"
                },
                "turbo": {
                    "stemmed": "turbo"
                },
                "language": {
                    "stemmed": "languag"
                },
                "material": {
                    "stemmed": "materi"
                },
                "frequently": {
                    "stemmed": "frequent"
                },
                "asked": {
                    "stemmed": "ask"
                },
                "ziped": {
                    "stemmed": "zipe"
                },
                "pascaltp": {
                    "stemmed": "pascaltp"
                },
                "concepts": {
                    "stemmed": "concept"
                },
                "structures": {
                    "stemmed": "structur"
                },
                "based": {
                    "stemmed": "base"
                },
                "newsgroups": {
                    "stemmed": "newsgroup"
                },
                "newgroups": {
                    "stemmed": "newgroup"
                },
                "might": {
                    "stemmed": "might"
                },
                "interested": {
                    "stemmed": "interest"
                },
                "complangpascalansiiso": {
                    "stemmed": "complangpascalansiiso"
                },
                "complangpascalmac": {
                    "stemmed": "complangpascalmac"
                },
                "complangpascalborland": {
                    "stemmed": "complangpascalborland"
                },
                "complangpascalmisc": {
                    "stemmed": "complangpascalmisc"
                },
                "complangpascaldelphimisc": {
                    "stemmed": "complangpascaldelphimisc"
                },
                "fjlangpascal": {
                    "stemmed": "fjlangpasc"
                },
                "remember": {
                    "stemmed": "rememb"
                },
                "access": {
                    "stemmed": "access"
                },
                "dell": {
                    "stemmed": "dell"
                },
                "newsccutexasedu": {
                    "stemmed": "newsccutexasedu"
                },
                "mail": {
                    "stemmed": "mail"
                },
                "preferences": {
                    "stemmed": "prefer"
                },
                "item": {
                    "stemmed": "item"
                },
                "options": {
                    "stemmed": "option"
                },
                "menu": {
                    "stemmed": "menu"
                },
                "take": {
                    "stemmed": "take"
                },
                "look": {
                    "stemmed": "look"
                },
                "usually": {
                    "stemmed": "usual"
                },
                "lead": {
                    "stemmed": "lead"
                },
                "impor": {
                    "stemmed": "impor"
                },
                "tant": {
                    "stemmed": "tant"
                },
                "stuff": {
                    "stemmed": "stuff"
                },
                "send": {
                    "stemmed": "send"
                },
                "comments": {
                    "stemmed": "comment"
                },
                "criticisms": {
                    "stemmed": "critic"
                },
                "suggestions": {
                    "stemmed": "suggest"
                },
                "additions": {
                    "stemmed": "addit"
                },
                "dwipcsutexasedu": {
                    "stemmed": "dwipcsutexasedu"
                }
            },
            "stemmed_words": {
                "server": {
                    "occurrences": 2
                },
                "date": {
                    "occurrences": 1
                },
                "monday": {
                    "occurrences": 2
                },
                "jan": {
                    "occurrences": 1
                },
                "wednesday": {
                    "occurrences": 2
                },
                "dec": {
                    "occurrences": 1
                },
                "cspporter": {
                    "occurrences": 2
                },
                "homepag": {
                    "occurrences": 1
                },
                "import": {
                    "occurrences": 4
                },
                "announc": {
                    "occurrences": 2
                },
                "take": {
                    "occurrences": 2
                },
                "today": {
                    "occurrences": 1
                },
                "home": {
                    "occurrences": 2
                },
                "unabl": {
                    "occurrences": 1
                },
                "maintain": {
                    "occurrences": 1
                },
                "page": {
                    "occurrences": 3
                },
                "last": {
                    "occurrences": 2
                },
                "coupl": {
                    "occurrences": 1
                },
                "day": {
                    "occurrences": 1
                },
                "howev": {
                    "occurrences": 2
                },
                "put": {
                    "occurrences": 1
                },
                "link": {
                    "occurrences": 4
                },
                "dr": {
                    "occurrences": 4
                },
                "porter": {
                    "occurrences": 8
                },
                "class": {
                    "occurrences": 9
                },
                "relat": {
                    "occurrences": 2
                },
                "avail": {
                    "occurrences": 4
                },
                "follow": {
                    "occurrences": 1
                },
                "good": {
                    "occurrences": 2
                },
                "luck": {
                    "occurrences": 2
                },
                "final": {
                    "occurrences": 8
                },
                "next": {
                    "occurrences": 3
                },
                "week": {
                    "occurrences": 5
                },
                "special": {
                    "occurrences": 2
                },
                "review": {
                    "occurrences": 7
                },
                "topic": {
                    "occurrences": 2
                },
                "cover": {
                    "occurrences": 2
                },
                "held": {
                    "occurrences": 1
                },
                "painter": {
                    "occurrences": 1
                },
                "hall": {
                    "occurrences": 2
                },
                "exact": {
                    "occurrences": 1
                },
                "locat": {
                    "occurrences": 1
                },
                "depend": {
                    "occurrences": 1
                },
                "room": {
                    "occurrences": 5
                },
                "availib": {
                    "occurrences": 1
                },
                "note": {
                    "occurrences": 3
                },
                "post": {
                    "occurrences": 4
                },
                "door": {
                    "occurrences": 1
                },
                "offic": {
                    "occurrences": 6
                },
                "someon": {
                    "occurrences": 1
                },
                "pai": {
                    "occurrences": 1
                },
                "inform": {
                    "occurrences": 1
                },
                "time": {
                    "occurrences": 2
                },
                "moreov": {
                    "occurrences": 1
                },
                "almost": {
                    "occurrences": 1
                },
                "total": {
                    "occurrences": 1
                },
                "coverag": {
                    "occurrences": 1
                },
                "hrs": {
                    "occurrences": 3
                },
                "tas": {
                    "occurrences": 3
                },
                "right": {
                    "occurrences": 1
                },
                "upto": {
                    "occurrences": 1
                },
                "exam": {
                    "occurrences": 5
                },
                "need": {
                    "occurrences": 2
                },
                "help": {
                    "occurrences": 2
                },
                "feel": {
                    "occurrences": 1
                },
                "free": {
                    "occurrences": 1
                },
                "come": {
                    "occurrences": 1
                },
                "ask": {
                    "occurrences": 2
                },
                "one": {
                    "occurrences": 2
                },
                "us": {
                    "occurrences": 1
                },
                "glad": {
                    "occurrences": 1
                },
                "mon": {
                    "occurrences": 1
                },
                "ai": {
                    "occurrences": 2
                },
                "resolutio": {
                    "occurrences": 1
                },
                "bruce": {
                    "occurrences": 3
                },
                "complex": {
                    "occurrences": 1
                },
                "theori": {
                    "occurrences": 1
                },
                "nimar": {
                    "occurrences": 1
                },
                "arora": {
                    "occurrences": 1
                },
                "tue": {
                    "occurrences": 1
                },
                "parallel": {
                    "occurrences": 1
                },
                "process": {
                    "occurrences": 1
                },
                "dwip": {
                    "occurrences": 2
                },
                "banerje": {
                    "occurrences": 1
                },
                "boolean": {
                    "occurrences": 1
                },
                "circuit": {
                    "occurrences": 1
                },
                "question": {
                    "occurrences": 8
                },
                "sheet": {
                    "occurrences": 1
                },
                "rotat": {
                    "occurrences": 1
                },
                "bit": {
                    "occurrences": 1
                },
                "disregard": {
                    "occurrences": 1
                },
                "somewhat": {
                    "occurrences": 1
                },
                "beyond": {
                    "occurrences": 1
                },
                "scope": {
                    "occurrences": 1
                },
                "slide": {
                    "occurrences": 1
                },
                "present": {
                    "occurrences": 1
                },
                "lectur": {
                    "occurrences": 3
                },
                "decemb": {
                    "occurrences": 2
                },
                "th": {
                    "occurrences": 1
                },
                "summar": {
                    "occurrences": 1
                },
                "content": {
                    "occurrences": 1
                },
                "whole": {
                    "occurrences": 1
                },
                "semest": {
                    "occurrences": 1
                },
                "reserv": {
                    "occurrences": 1
                },
                "desk": {
                    "occurrences": 1
                },
                "ugl": {
                    "occurrences": 1
                },
                "hope": {
                    "occurrences": 1
                },
                "webpag": {
                    "occurrences": 1
                },
                "soon": {
                    "occurrences": 1
                },
                "experienc": {
                    "occurrences": 1
                },
                "technic": {
                    "occurrences": 1
                },
                "difficulti": {
                    "occurrences": 1
                },
                "caus": {
                    "occurrences": 1
                },
                "length": {
                    "occurrences": 1
                },
                "file": {
                    "occurrences": 1
                },
                "click": {
                    "occurrences": 2
                },
                "schedul": {
                    "occurrences": 3
                },
                "also": {
                    "occurrences": 2
                },
                "pleas": {
                    "occurrences": 1
                },
                "check": {
                    "occurrences": 1
                },
                "assign": {
                    "occurrences": 5
                },
                "addendum": {
                    "occurrences": 2
                },
                "html": {
                    "occurrences": 3
                },
                "version": {
                    "occurrences": 6
                },
                "postscript": {
                    "occurrences": 3
                },
                "ad": {
                    "occurrences": 1
                },
                "set": {
                    "occurrences": 2
                },
                "stay": {
                    "occurrences": 1
                },
                "tune": {
                    "occurrences": 1
                },
                "program": {
                    "occurrences": 7
                },
                "download": {
                    "occurrences": 1
                },
                "tutori": {
                    "occurrences": 3
                },
                "prolog": {
                    "occurrences": 1
                },
                "nov": {
                    "occurrences": 1
                },
                "comput": {
                    "occurrences": 1
                },
                "scienc": {
                    "occurrences": 1
                },
                "instructor": {
                    "occurrences": 1
                },
                "portercsutexasedu": {
                    "occurrences": 2
                },
                "pm": {
                    "occurrences": 3
                },
                "taylor": {
                    "occurrences": 1
                },
                "phone": {
                    "occurrences": 1
                },
                "email": {
                    "occurrences": 1
                },
                "hour": {
                    "occurrences": 1
                },
                "lab": {
                    "occurrences": 2
                },
                "discuss": {
                    "occurrences": 3
                },
                "section": {
                    "occurrences": 1
                },
                "cs": {
                    "occurrences": 1
                },
                "p": {
                    "occurrences": 1
                },
                "thursday": {
                    "occurrences": 1
                },
                "uniqu": {
                    "occurrences": 1
                },
                "number": {
                    "occurrences": 1
                },
                "welch": {
                    "occurrences": 3
                },
                "cours": {
                    "occurrences": 1
                },
                "descript": {
                    "occurrences": 2
                },
                "session": {
                    "occurrences": 2
                },
                "includ": {
                    "occurrences": 1
                },
                "labdiscuss": {
                    "occurrences": 1
                },
                "news": {
                    "occurrences": 5
                },
                "articl": {
                    "occurrences": 3
                },
                "newsgroup": {
                    "occurrences": 4
                },
                "midterm": {
                    "occurrences": 4
                },
                "test": {
                    "occurrences": 2
                },
                "solut": {
                    "occurrences": 1
                },
                "ii": {
                    "occurrences": 2
                },
                "use": {
                    "occurrences": 2
                },
                "pascal": {
                    "occurrences": 9
                },
                "text": {
                    "occurrences": 1
                },
                "format": {
                    "occurrences": 1
                },
                "ansiiso": {
                    "occurrences": 1
                },
                "faq": {
                    "occurrences": 1
                },
                "get": {
                    "occurrences": 2
                },
                "sampl": {
                    "occurrences": 1
                },
                "tp": {
                    "occurrences": 1
                },
                "programm": {
                    "occurrences": 1
                },
                "generic": {
                    "occurrences": 1
                },
                "turbo": {
                    "occurrences": 4
                },
                "languag": {
                    "occurrences": 1
                },
                "materi": {
                    "occurrences": 1
                },
                "frequent": {
                    "occurrences": 1
                },
                "zipe": {
                    "occurrences": 1
                },
                "pascaltp": {
                    "occurrences": 1
                },
                "concept": {
                    "occurrences": 1
                },
                "structur": {
                    "occurrences": 1
                },
                "base": {
                    "occurrences": 1
                },
                "newgroup": {
                    "occurrences": 1
                },
                "might": {
                    "occurrences": 1
                },
                "interest": {
                    "occurrences": 1
                },
                "complangpascalansiiso": {
                    "occurrences": 1
                },
                "complangpascalmac": {
                    "occurrences": 1
                },
                "complangpascalborland": {
                    "occurrences": 1
                },
                "complangpascalmisc": {
                    "occurrences": 1
                },
                "complangpascaldelphimisc": {
                    "occurrences": 1
                },
                "fjlangpasc": {
                    "occurrences": 1
                },
                "rememb": {
                    "occurrences": 1
                },
                "access": {
                    "occurrences": 1
                },
                "dell": {
                    "occurrences": 1
                },
                "newsccutexasedu": {
                    "occurrences": 1
                },
                "mail": {
                    "occurrences": 1
                },
                "prefer": {
                    "occurrences": 1
                },
                "item": {
                    "occurrences": 1
                },
                "option": {
                    "occurrences": 1
                },
                "menu": {
                    "occurrences": 1
                },
                "look": {
                    "occurrences": 1
                },
                "usual": {
                    "occurrences": 1
                },
                "lead": {
                    "occurrences": 1
                },
                "impor": {
                    "occurrences": 1
                },
                "tant": {
                    "occurrences": 1
                },
                "stuff": {
                    "occurrences": 1
                },
                "send": {
                    "occurrences": 1
                },
                "comment": {
                    "occurrences": 1
                },
                "critic": {
                    "occurrences": 1
                },
                "suggest": {
                    "occurrences": 1
                },
                "addit": {
                    "occurrences": 1
                },
                "dwipcsutexasedu": {
                    "occurrences": 1
                }
            },
            "category": "course"
        },
        "http_^^www.cs.utexas.edu^users^almstrum^welcome.html": {
            "words": {
                "server": {
                    "stemmed": "server"
                },
                "date": {
                    "stemmed": "date"
                },
                "monday": {
                    "stemmed": "monday"
                },
                "jan": {
                    "stemmed": "jan"
                },
                "sep": {
                    "stemmed": "sep"
                },
                "vicki": {
                    "stemmed": "vicki"
                },
                "l": {
                    "stemmed": "l"
                },
                "almstrum": {
                    "stemmed": "almstrum"
                },
                "utcs": {
                    "stemmed": "utc"
                },
                "home": {
                    "stemmed": "home"
                },
                "page": {
                    "stemmed": "page"
                },
                "educator": {
                    "stemmed": "educ"
                },
                "computer": {
                    "stemmed": "comput"
                },
                "scientist": {
                    "stemmed": "scientist"
                },
                "interested": {
                    "stemmed": "interest"
                },
                "understanding": {
                    "stemmed": "understand"
                },
                "people": {
                    "stemmed": "peopl"
                },
                "learn": {
                    "stemmed": "learn"
                },
                "particularly": {
                    "stemmed": "particular"
                },
                "learning": {
                    "stemmed": "learn"
                },
                "mathematical": {
                    "stemmed": "mathemat"
                },
                "logic": {
                    "stemmed": "logic"
                },
                "formal": {
                    "stemmed": "formal"
                },
                "methods": {
                    "stemmed": "method"
                },
                "doctoral": {
                    "stemmed": "doctor"
                },
                "research": {
                    "stemmed": "research"
                },
                "topic": {
                    "stemmed": "topic"
                },
                "limitations": {
                    "stemmed": "limit"
                },
                "novice": {
                    "stemmed": "novic"
                },
                "science": {
                    "stemmed": "scienc"
                },
                "students": {
                    "stemmed": "student"
                },
                "lecturer": {
                    "stemmed": "lectur"
                },
                "university": {
                    "stemmed": "univers"
                },
                "texas": {
                    "stemmed": "texa"
                },
                "austin": {
                    "stemmed": "austin"
                },
                "addition": {
                    "stemmed": "addit"
                },
                "spent": {
                    "stemmed": "spent"
                },
                "fall": {
                    "stemmed": "fall"
                },
                "semester": {
                    "stemmed": "semest"
                },
                "teaching": {
                    "stemmed": "teach"
                },
                "uppsala": {
                    "stemmed": "uppsala"
                },
                "sweden": {
                    "stemmed": "sweden"
                },
                "link": {
                    "stemmed": "link"
                },
                "interests": {
                    "stemmed": "interest"
                },
                "include": {
                    "stemmed": "includ"
                },
                "encouraging": {
                    "stemmed": "encourag"
                },
                "others": {
                    "stemmed": "other"
                },
                "excel": {
                    "stemmed": "excel"
                },
                "mathematics": {
                    "stemmed": "mathemat"
                },
                "gardening": {
                    "stemmed": "garden"
                },
                "travel": {
                    "stemmed": "travel"
                },
                "crafts": {
                    "stemmed": "craft"
                },
                "sewing": {
                    "stemmed": "sew"
                },
                "woodworking": {
                    "stemmed": "woodwork"
                },
                "etc": {
                    "stemmed": "etc"
                },
                "heres": {
                    "stemmed": "here"
                },
                "picture": {
                    "stemmed": "pictur"
                },
                "hubby": {
                    "stemmed": "hubbi"
                },
                "torgny": {
                    "stemmed": "torgni"
                },
                "stadler": {
                    "stemmed": "stadler"
                },
                "check": {
                    "stemmed": "check"
                },
                "sites": {
                    "stemmed": "site"
                },
                "iticse": {
                    "stemmed": "itics"
                },
                "conference": {
                    "stemmed": "confer"
                },
                "integrating": {
                    "stemmed": "integr"
                },
                "technology": {
                    "stemmed": "technolog"
                },
                "education": {
                    "stemmed": "educ"
                },
                "june": {
                    "stemmed": "june"
                },
                "working": {
                    "stemmed": "work"
                },
                "groups": {
                    "stemmed": "group"
                },
                "pages": {
                    "stemmed": "page"
                },
                "maintain": {
                    "stemmed": "maintain"
                },
                "classes": {
                    "stemmed": "class"
                },
                "teach": {
                    "stemmed": "teach"
                },
                "ut": {
                    "stemmed": "ut"
                },
                "field": {
                    "stemmed": "field"
                },
                "includes": {
                    "stemmed": "includ"
                },
                "evaluation": {
                    "stemmed": "evalu"
                },
                "mentoring": {
                    "stemmed": "mentor"
                },
                "issues": {
                    "stemmed": "issu"
                },
                "interesting": {
                    "stemmed": "interest"
                },
                "jumpingoff": {
                    "stemmed": "jumpingoff"
                },
                "points": {
                    "stemmed": "point"
                },
                "area": {
                    "stemmed": "area"
                },
                "suffers": {
                    "stemmed": "suffer"
                },
                "spurts": {
                    "stemmed": "spurt"
                },
                "construction": {
                    "stemmed": "construct"
                },
                "frenzy": {
                    "stemmed": "frenzi"
                },
                "organizations": {
                    "stemmed": "organ"
                },
                "belong": {
                    "stemmed": "belong"
                },
                "sigcse": {
                    "stemmed": "sigcs"
                },
                "acms": {
                    "stemmed": "acm"
                },
                "special": {
                    "stemmed": "special"
                },
                "interest": {
                    "stemmed": "interest"
                },
                "group": {
                    "stemmed": "group"
                },
                "sigsoft": {
                    "stemmed": "sigsoft"
                },
                "software": {
                    "stemmed": "softwar"
                },
                "engineering": {
                    "stemmed": "engin"
                },
                "acm": {
                    "stemmed": "acm"
                },
                "association": {
                    "stemmed": "associ"
                },
                "computing": {
                    "stemmed": "comput"
                },
                "machinery": {
                    "stemmed": "machineri"
                },
                "ieee": {
                    "stemmed": "ieee"
                },
                "institute": {
                    "stemmed": "institut"
                },
                "electrical": {
                    "stemmed": "electr"
                },
                "electronics": {
                    "stemmed": "electron"
                },
                "engineers": {
                    "stemmed": "engin"
                },
                "cpsr": {
                    "stemmed": "cpsr"
                },
                "professionals": {
                    "stemmed": "profession"
                },
                "social": {
                    "stemmed": "social"
                },
                "responsibility": {
                    "stemmed": "respons"
                },
                "connections": {
                    "stemmed": "connect"
                },
                "sciences": {
                    "stemmed": "scienc"
                },
                "web": {
                    "stemmed": "web"
                },
                "elsewhere": {
                    "stemmed": "elsewher"
                },
                "contact": {
                    "stemmed": "contact"
                },
                "office": {
                    "stemmed": "offic"
                },
                "department": {
                    "stemmed": "depart"
                },
                "c": {
                    "stemmed": "c"
                },
                "tay": {
                    "stemmed": "tay"
                },
                "tx": {
                    "stemmed": "tx"
                },
                "usa": {
                    "stemmed": "usa"
                },
                "cs": {
                    "stemmed": "cs"
                },
                "main": {
                    "stemmed": "main"
                },
                "direct": {
                    "stemmed": "direct"
                },
                "seldom": {
                    "stemmed": "seldom"
                },
                "fax": {
                    "stemmed": "fax"
                },
                "always": {
                    "stemmed": "alway"
                },
                "connected": {
                    "stemmed": "connect"
                },
                "need": {
                    "stemmed": "need"
                },
                "forewarn": {
                    "stemmed": "forewarn"
                },
                "leave": {
                    "stemmed": "leav"
                },
                "plenty": {
                    "stemmed": "plenti"
                },
                "time": {
                    "stemmed": "time"
                },
                "email": {
                    "stemmed": "email"
                },
                "address": {
                    "stemmed": "address"
                },
                "almstrumcsutexasedu": {
                    "stemmed": "almstrumcsutexasedu"
                }
            },
            "stemmed_words": {
                "server": {
                    "occurrences": 1
                },
                "date": {
                    "occurrences": 1
                },
                "monday": {
                    "occurrences": 2
                },
                "jan": {
                    "occurrences": 1
                },
                "sep": {
                    "occurrences": 1
                },
                "vicki": {
                    "occurrences": 2
                },
                "l": {
                    "occurrences": 2
                },
                "almstrum": {
                    "occurrences": 2
                },
                "utc": {
                    "occurrences": 1
                },
                "home": {
                    "occurrences": 5
                },
                "page": {
                    "occurrences": 5
                },
                "educ": {
                    "occurrences": 4
                },
                "comput": {
                    "occurrences": 10
                },
                "scientist": {
                    "occurrences": 1
                },
                "interest": {
                    "occurrences": 6
                },
                "understand": {
                    "occurrences": 2
                },
                "peopl": {
                    "occurrences": 1
                },
                "learn": {
                    "occurrences": 3
                },
                "particular": {
                    "occurrences": 1
                },
                "mathemat": {
                    "occurrences": 3
                },
                "logic": {
                    "occurrences": 2
                },
                "formal": {
                    "occurrences": 1
                },
                "method": {
                    "occurrences": 2
                },
                "doctor": {
                    "occurrences": 1
                },
                "research": {
                    "occurrences": 2
                },
                "topic": {
                    "occurrences": 1
                },
                "limit": {
                    "occurrences": 1
                },
                "novic": {
                    "occurrences": 1
                },
                "scienc": {
                    "occurrences": 7
                },
                "student": {
                    "occurrences": 1
                },
                "lectur": {
                    "occurrences": 1
                },
                "univers": {
                    "occurrences": 3
                },
                "texa": {
                    "occurrences": 3
                },
                "austin": {
                    "occurrences": 6
                },
                "addit": {
                    "occurrences": 1
                },
                "spent": {
                    "occurrences": 1
                },
                "fall": {
                    "occurrences": 1
                },
                "semest": {
                    "occurrences": 1
                },
                "teach": {
                    "occurrences": 2
                },
                "uppsala": {
                    "occurrences": 2
                },
                "sweden": {
                    "occurrences": 2
                },
                "link": {
                    "occurrences": 1
                },
                "includ": {
                    "occurrences": 2
                },
                "encourag": {
                    "occurrences": 1
                },
                "other": {
                    "occurrences": 1
                },
                "excel": {
                    "occurrences": 1
                },
                "garden": {
                    "occurrences": 1
                },
                "travel": {
                    "occurrences": 1
                },
                "craft": {
                    "occurrences": 1
                },
                "sew": {
                    "occurrences": 1
                },
                "woodwork": {
                    "occurrences": 1
                },
                "etc": {
                    "occurrences": 1
                },
                "here": {
                    "occurrences": 1
                },
                "pictur": {
                    "occurrences": 1
                },
                "hubbi": {
                    "occurrences": 1
                },
                "torgni": {
                    "occurrences": 1
                },
                "stadler": {
                    "occurrences": 1
                },
                "check": {
                    "occurrences": 1
                },
                "site": {
                    "occurrences": 1
                },
                "itics": {
                    "occurrences": 1
                },
                "confer": {
                    "occurrences": 1
                },
                "integr": {
                    "occurrences": 1
                },
                "technolog": {
                    "occurrences": 1
                },
                "june": {
                    "occurrences": 2
                },
                "work": {
                    "occurrences": 1
                },
                "group": {
                    "occurrences": 3
                },
                "maintain": {
                    "occurrences": 1
                },
                "class": {
                    "occurrences": 1
                },
                "ut": {
                    "occurrences": 3
                },
                "field": {
                    "occurrences": 1
                },
                "evalu": {
                    "occurrences": 1
                },
                "mentor": {
                    "occurrences": 1
                },
                "issu": {
                    "occurrences": 1
                },
                "jumpingoff": {
                    "occurrences": 1
                },
                "point": {
                    "occurrences": 1
                },
                "area": {
                    "occurrences": 1
                },
                "suffer": {
                    "occurrences": 1
                },
                "spurt": {
                    "occurrences": 1
                },
                "construct": {
                    "occurrences": 1
                },
                "frenzi": {
                    "occurrences": 1
                },
                "organ": {
                    "occurrences": 1
                },
                "belong": {
                    "occurrences": 1
                },
                "sigcs": {
                    "occurrences": 1
                },
                "acm": {
                    "occurrences": 3
                },
                "special": {
                    "occurrences": 2
                },
                "sigsoft": {
                    "occurrences": 1
                },
                "softwar": {
                    "occurrences": 1
                },
                "engin": {
                    "occurrences": 2
                },
                "associ": {
                    "occurrences": 1
                },
                "machineri": {
                    "occurrences": 1
                },
                "ieee": {
                    "occurrences": 1
                },
                "institut": {
                    "occurrences": 1
                },
                "electr": {
                    "occurrences": 1
                },
                "electron": {
                    "occurrences": 1
                },
                "cpsr": {
                    "occurrences": 1
                },
                "profession": {
                    "occurrences": 1
                },
                "social": {
                    "occurrences": 1
                },
                "respons": {
                    "occurrences": 1
                },
                "connect": {
                    "occurrences": 2
                },
                "web": {
                    "occurrences": 1
                },
                "elsewher": {
                    "occurrences": 1
                },
                "contact": {
                    "occurrences": 1
                },
                "offic": {
                    "occurrences": 2
                },
                "depart": {
                    "occurrences": 1
                },
                "c": {
                    "occurrences": 1
                },
                "tay": {
                    "occurrences": 1
                },
                "tx": {
                    "occurrences": 1
                },
                "usa": {
                    "occurrences": 1
                },
                "cs": {
                    "occurrences": 1
                },
                "main": {
                    "occurrences": 1
                },
                "direct": {
                    "occurrences": 1
                },
                "seldom": {
                    "occurrences": 1
                },
                "fax": {
                    "occurrences": 2
                },
                "alway": {
                    "occurrences": 1
                },
                "need": {
                    "occurrences": 1
                },
                "forewarn": {
                    "occurrences": 1
                },
                "leav": {
                    "occurrences": 1
                },
                "plenti": {
                    "occurrences": 1
                },
                "time": {
                    "occurrences": 1
                },
                "email": {
                    "occurrences": 1
                },
                "address": {
                    "occurrences": 1
                },
                "almstrumcsutexasedu": {
                    "occurrences": 2
                }
            },
            "category": "faculty"
        },
        "http_^^www.cs.washington.edu^homes^dfasulo^": {
            "words": {
                "date": {
                    "stemmed": "date"
                },
                "thu": {
                    "stemmed": "thu"
                },
                "nov": {
                    "stemmed": "nov"
                },
                "server": {
                    "stemmed": "server"
                },
                "ncsa": {
                    "stemmed": "ncsa"
                },
                "wed": {
                    "stemmed": "wed"
                },
                "oct": {
                    "stemmed": "oct"
                },
                "dans": {
                    "stemmed": "dan"
                },
                "home": {
                    "stemmed": "home"
                },
                "page": {
                    "stemmed": "page"
                },
                "welcome": {
                    "stemmed": "welcom"
                },
                "dan": {
                    "stemmed": "dan"
                },
                "fasulos": {
                    "stemmed": "fasulo"
                },
                "dfasulocswashingtonedu": {
                    "stemmed": "dfasulocswashingtonedu"
                },
                "thirdyear": {
                    "stemmed": "thirdyear"
                },
                "graduate": {
                    "stemmed": "graduat"
                },
                "student": {
                    "stemmed": "student"
                },
                "department": {
                    "stemmed": "depart"
                },
                "computer": {
                    "stemmed": "comput"
                },
                "science": {
                    "stemmed": "scienc"
                },
                "university": {
                    "stemmed": "univers"
                },
                "washington": {
                    "stemmed": "washington"
                },
                "ba": {
                    "stemmed": "ba"
                },
                "williams": {
                    "stemmed": "william"
                },
                "college": {
                    "stemmed": "colleg"
                },
                "applied": {
                    "stemmed": "appli"
                },
                "mathematics": {
                    "stemmed": "mathemat"
                },
                "class": {
                    "stemmed": "class"
                },
                "note": {
                    "stemmed": "note"
                },
                "portrait": {
                    "stemmed": "portrait"
                },
                "may": {
                    "stemmed": "may"
                },
                "contain": {
                    "stemmed": "contain"
                },
                "slight": {
                    "stemmed": "slight"
                },
                "inaccuracies": {
                    "stemmed": "inaccuraci"
                },
                "finding": {
                    "stemmed": "find"
                },
                "eastlake": {
                    "stemmed": "eastlak"
                },
                "ave": {
                    "stemmed": "ave"
                },
                "e": {
                    "stemmed": "e"
                },
                "seattle": {
                    "stemmed": "seattl"
                },
                "wa": {
                    "stemmed": "wa"
                },
                "work": {
                    "stemmed": "work"
                },
                "engineering": {
                    "stemmed": "engin"
                },
                "fr": {
                    "stemmed": "fr"
                },
                "usa": {
                    "stemmed": "usa"
                },
                "office": {
                    "stemmed": "offic"
                },
                "chateau": {
                    "stemmed": "chateau"
                },
                "email": {
                    "stemmed": "email"
                },
                "academic": {
                    "stemmed": "academ"
                },
                "interests": {
                    "stemmed": "interest"
                },
                "graphics": {
                    "stemmed": "graphic"
                },
                "computational": {
                    "stemmed": "comput"
                },
                "biology": {
                    "stemmed": "biolog"
                },
                "personal": {
                    "stemmed": "person"
                },
                "fiction": {
                    "stemmed": "fiction"
                },
                "fantasy": {
                    "stemmed": "fantasi"
                },
                "written": {
                    "stemmed": "written"
                },
                "otherwise": {
                    "stemmed": "otherwis"
                },
                "fact": {
                    "stemmed": "fact"
                },
                "probably": {
                    "stemmed": "probabl"
                },
                "honest": {
                    "stemmed": "honest"
                },
                "identify": {
                    "stemmed": "identifi"
                },
                "illustration": {
                    "stemmed": "illustr"
                },
                "merlin": {
                    "stemmed": "merlin"
                },
                "son": {
                    "stemmed": "son"
                },
                "corwin": {
                    "stemmed": "corwin"
                },
                "pictured": {
                    "stemmed": "pictur"
                },
                "favorite": {
                    "stemmed": "favorit"
                },
                "fictional": {
                    "stemmed": "fiction"
                },
                "character": {
                    "stemmed": "charact"
                },
                "mine": {
                    "stemmed": "mine"
                },
                "roger": {
                    "stemmed": "roger"
                },
                "zelaznys": {
                    "stemmed": "zelazni"
                },
                "chronicles": {
                    "stemmed": "chronicl"
                },
                "amber": {
                    "stemmed": "amber"
                },
                "image": {
                    "stemmed": "imag"
                },
                "taken": {
                    "stemmed": "taken"
                },
                "drpg": {
                    "stemmed": "drpg"
                },
                "published": {
                    "stemmed": "publish"
                },
                "phage": {
                    "stemmed": "phage"
                },
                "press": {
                    "stemmed": "press"
                },
                "would": {
                    "stemmed": "would"
                },
                "recommend": {
                    "stemmed": "recommend"
                },
                "anyone": {
                    "stemmed": "anyon"
                },
                "likes": {
                    "stemmed": "like"
                },
                "books": {
                    "stemmed": "book"
                },
                "also": {
                    "stemmed": "also"
                },
                "tv": {
                    "stemmed": "tv"
                },
                "series": {
                    "stemmed": "seri"
                },
                "babylon": {
                    "stemmed": "babylon"
                },
                "creative": {
                    "stemmed": "creativ"
                },
                "writing": {
                    "stemmed": "write"
                },
                "poetry": {
                    "stemmed": "poetri"
                },
                "absolutely": {
                    "stemmed": "absolut"
                },
                "links": {
                    "stemmed": "link"
                },
                "athletics": {
                    "stemmed": "athlet"
                },
                "particular": {
                    "stemmed": "particular"
                },
                "order": {
                    "stemmed": "order"
                },
                "tennis": {
                    "stemmed": "tenni"
                },
                "tae": {
                    "stemmed": "tae"
                },
                "kwon": {
                    "stemmed": "kwon"
                },
                "distance": {
                    "stemmed": "distanc"
                },
                "running": {
                    "stemmed": "run"
                },
                "roleplaying": {
                    "stemmed": "roleplay"
                },
                "random": {
                    "stemmed": "random"
                },
                "things": {
                    "stemmed": "thing"
                },
                "depending": {
                    "stemmed": "depend"
                },
                "day": {
                    "stemmed": "day"
                },
                "cats": {
                    "stemmed": "cat"
                },
                "go": {
                    "stemmed": "go"
                },
                "homepage": {
                    "stemmed": "homepag"
                },
                "friend": {
                    "stemmed": "friend"
                },
                "fellow": {
                    "stemmed": "fellow"
                },
                "alumnus": {
                    "stemmed": "alumnus"
                },
                "sean": {
                    "stemmed": "sean"
                },
                "sandys": {
                    "stemmed": "sandi"
                },
                "look": {
                    "stemmed": "look"
                },
                "web": {
                    "stemmed": "web"
                },
                "woman": {
                    "stemmed": "woman"
                },
                "dog": {
                    "stemmed": "dog"
                },
                "former": {
                    "stemmed": "former"
                },
                "cse": {
                    "stemmed": "cse"
                },
                "grad": {
                    "stemmed": "grad"
                },
                "wendy": {
                    "stemmed": "wendi"
                },
                "belluomini": {
                    "stemmed": "belluomini"
                },
                "dressed": {
                    "stemmed": "dress"
                },
                "dogbert": {
                    "stemmed": "dogbert"
                },
                "lot": {
                    "stemmed": "lot"
                },
                "people": {
                    "stemmed": "peopl"
                },
                "asked": {
                    "stemmed": "ask"
                },
                "theory": {
                    "stemmed": "theori"
                },
                "worthwhile": {
                    "stemmed": "worthwhil"
                },
                "area": {
                    "stemmed": "area"
                },
                "research": {
                    "stemmed": "research"
                },
                "whether": {
                    "stemmed": "whether"
                },
                "abstract": {
                    "stemmed": "abstract"
                },
                "useful": {
                    "stemmed": "use"
                },
                "better": {
                    "stemmed": "better"
                },
                "explanation": {
                    "stemmed": "explan"
                },
                "goals": {
                    "stemmed": "goal"
                },
                "future": {
                    "stemmed": "futur"
                },
                "ive": {
                    "stemmed": "ive"
                },
                "ever": {
                    "stemmed": "ever"
                },
                "given": {
                    "stemmed": "given"
                }
            },
            "stemmed_words": {
                "date": {
                    "occurrences": 1
                },
                "thu": {
                    "occurrences": 1
                },
                "nov": {
                    "occurrences": 1
                },
                "server": {
                    "occurrences": 1
                },
                "ncsa": {
                    "occurrences": 1
                },
                "wed": {
                    "occurrences": 1
                },
                "oct": {
                    "occurrences": 1
                },
                "dan": {
                    "occurrences": 3
                },
                "home": {
                    "occurrences": 3
                },
                "page": {
                    "occurrences": 2
                },
                "welcom": {
                    "occurrences": 1
                },
                "fasulo": {
                    "occurrences": 1
                },
                "dfasulocswashingtonedu": {
                    "occurrences": 3
                },
                "thirdyear": {
                    "occurrences": 1
                },
                "graduat": {
                    "occurrences": 2
                },
                "student": {
                    "occurrences": 2
                },
                "depart": {
                    "occurrences": 2
                },
                "comput": {
                    "occurrences": 5
                },
                "scienc": {
                    "occurrences": 4
                },
                "univers": {
                    "occurrences": 2
                },
                "washington": {
                    "occurrences": 2
                },
                "ba": {
                    "occurrences": 1
                },
                "william": {
                    "occurrences": 2
                },
                "colleg": {
                    "occurrences": 1
                },
                "appli": {
                    "occurrences": 1
                },
                "mathemat": {
                    "occurrences": 1
                },
                "class": {
                    "occurrences": 1
                },
                "note": {
                    "occurrences": 1
                },
                "portrait": {
                    "occurrences": 1
                },
                "may": {
                    "occurrences": 1
                },
                "contain": {
                    "occurrences": 1
                },
                "slight": {
                    "occurrences": 1
                },
                "inaccuraci": {
                    "occurrences": 1
                },
                "find": {
                    "occurrences": 1
                },
                "eastlak": {
                    "occurrences": 1
                },
                "ave": {
                    "occurrences": 1
                },
                "e": {
                    "occurrences": 1
                },
                "seattl": {
                    "occurrences": 2
                },
                "wa": {
                    "occurrences": 2
                },
                "work": {
                    "occurrences": 2
                },
                "engin": {
                    "occurrences": 1
                },
                "fr": {
                    "occurrences": 1
                },
                "usa": {
                    "occurrences": 1
                },
                "offic": {
                    "occurrences": 1
                },
                "chateau": {
                    "occurrences": 1
                },
                "email": {
                    "occurrences": 1
                },
                "academ": {
                    "occurrences": 1
                },
                "interest": {
                    "occurrences": 2
                },
                "graphic": {
                    "occurrences": 1
                },
                "biolog": {
                    "occurrences": 1
                },
                "person": {
                    "occurrences": 1
                },
                "fiction": {
                    "occurrences": 3
                },
                "fantasi": {
                    "occurrences": 1
                },
                "written": {
                    "occurrences": 1
                },
                "otherwis": {
                    "occurrences": 1
                },
                "fact": {
                    "occurrences": 1
                },
                "probabl": {
                    "occurrences": 1
                },
                "honest": {
                    "occurrences": 1
                },
                "identifi": {
                    "occurrences": 1
                },
                "illustr": {
                    "occurrences": 1
                },
                "merlin": {
                    "occurrences": 1
                },
                "son": {
                    "occurrences": 1
                },
                "corwin": {
                    "occurrences": 1
                },
                "pictur": {
                    "occurrences": 1
                },
                "favorit": {
                    "occurrences": 1
                },
                "charact": {
                    "occurrences": 1
                },
                "mine": {
                    "occurrences": 1
                },
                "roger": {
                    "occurrences": 1
                },
                "zelazni": {
                    "occurrences": 1
                },
                "chronicl": {
                    "occurrences": 1
                },
                "amber": {
                    "occurrences": 2
                },
                "imag": {
                    "occurrences": 1
                },
                "taken": {
                    "occurrences": 1
                },
                "drpg": {
                    "occurrences": 1
                },
                "publish": {
                    "occurrences": 1
                },
                "phage": {
                    "occurrences": 1
                },
                "press": {
                    "occurrences": 1
                },
                "would": {
                    "occurrences": 1
                },
                "recommend": {
                    "occurrences": 2
                },
                "anyon": {
                    "occurrences": 1
                },
                "like": {
                    "occurrences": 1
                },
                "book": {
                    "occurrences": 1
                },
                "also": {
                    "occurrences": 1
                },
                "tv": {
                    "occurrences": 1
                },
                "seri": {
                    "occurrences": 1
                },
                "babylon": {
                    "occurrences": 1
                },
                "creativ": {
                    "occurrences": 1
                },
                "write": {
                    "occurrences": 1
                },
                "poetri": {
                    "occurrences": 1
                },
                "absolut": {
                    "occurrences": 1
                },
                "link": {
                    "occurrences": 1
                },
                "athlet": {
                    "occurrences": 1
                },
                "particular": {
                    "occurrences": 1
                },
                "order": {
                    "occurrences": 1
                },
                "tenni": {
                    "occurrences": 1
                },
                "tae": {
                    "occurrences": 1
                },
                "kwon": {
                    "occurrences": 1
                },
                "distanc": {
                    "occurrences": 1
                },
                "run": {
                    "occurrences": 1
                },
                "roleplay": {
                    "occurrences": 1
                },
                "random": {
                    "occurrences": 2
                },
                "thing": {
                    "occurrences": 2
                },
                "depend": {
                    "occurrences": 1
                },
                "day": {
                    "occurrences": 1
                },
                "cat": {
                    "occurrences": 1
                },
                "go": {
                    "occurrences": 1
                },
                "homepag": {
                    "occurrences": 1
                },
                "friend": {
                    "occurrences": 1
                },
                "fellow": {
                    "occurrences": 1
                },
                "alumnus": {
                    "occurrences": 1
                },
                "sean": {
                    "occurrences": 1
                },
                "sandi": {
                    "occurrences": 1
                },
                "look": {
                    "occurrences": 1
                },
                "web": {
                    "occurrences": 1
                },
                "woman": {
                    "occurrences": 1
                },
                "dog": {
                    "occurrences": 1
                },
                "former": {
                    "occurrences": 1
                },
                "cse": {
                    "occurrences": 1
                },
                "grad": {
                    "occurrences": 1
                },
                "wendi": {
                    "occurrences": 1
                },
                "belluomini": {
                    "occurrences": 1
                },
                "dress": {
                    "occurrences": 1
                },
                "dogbert": {
                    "occurrences": 1
                },
                "lot": {
                    "occurrences": 1
                },
                "peopl": {
                    "occurrences": 1
                },
                "ask": {
                    "occurrences": 1
                },
                "theori": {
                    "occurrences": 2
                },
                "worthwhil": {
                    "occurrences": 1
                },
                "area": {
                    "occurrences": 1
                },
                "research": {
                    "occurrences": 1
                },
                "whether": {
                    "occurrences": 1
                },
                "abstract": {
                    "occurrences": 1
                },
                "use": {
                    "occurrences": 1
                },
                "better": {
                    "occurrences": 1
                },
                "explan": {
                    "occurrences": 1
                },
                "goal": {
                    "occurrences": 1
                },
                "futur": {
                    "occurrences": 1
                },
                "ive": {
                    "occurrences": 1
                },
                "ever": {
                    "occurrences": 1
                },
                "given": {
                    "occurrences": 1
                }
            },
            "category": "student"
        }   
    }
    predictions=[]

    # Typically k = N^(1/2) where N is the number of attributes
    # Attributes being each word found
    k = 150

    correctClassification = 0

    # The number of pages processed
    pageCount = 0

    for key in test_data:
        expected_classification = test_data[key]["category"]
        # Returns K number of nearest neighbors
        neighbors = msC.getNeighbors(test_data[key]['stemmed_words'], k)
        
        # Gets the classification of the the surrounding neighbors with the most members present
        classification = msC.getNeighborsVotes(neighbors)

        if classification == expected_classification:
            correctClassification += 1

        pageCount += 1

    print("Accuracy:  " + str(correctClassification / pageCount))

        


main()