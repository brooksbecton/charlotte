from CharlotteKnn import CharlotteKnn

def main():
    msC = CharlotteKnn()

    test_data = {"http_^^www.cs.cornell.edu^Info^People^lucy^lucy.html": {
        "words": {
            "multimedia": {
                "stemmed": "multimedia"
            },
            "university": {
                "stemmed": "univers"
            },
            "security": {
                "stemmed": "secur"
            },
            "connections": {
                "stemmed": "connect"
            },
            "nov": {
                "stemmed": "nov"
            },
            "archive": {
                "stemmed": "archiv"
            },
            "java": {
                "stemmed": "java"
            },
            "wus": {
                "stemmed": "wus"
            },
            "taichi": {
                "stemmed": "taichi"
            },
            "mail": {
                "stemmed": "mail"
            },
            "interested": {
                "stemmed": "interest"
            },
            "hot": {
                "stemmed": "hot"
            },
            "cornell": {
                "stemmed": "cornel"
            },
            "cnn": {
                "stemmed": "cnn"
            },
            "engineering": {
                "stemmed": "engin"
            },
            "reading": {
                "stemmed": "read"
            },
            "web": {
                "stemmed": "web"
            },
            "www": {
                "stemmed": "www"
            },
            "company": {
                "stemmed": "compani"
            },
            "internet": {
                "stemmed": "internet"
            },
            "programming": {
                "stemmed": "program"
            },
            "misc": {
                "stemmed": "misc"
            },
            "novell": {
                "stemmed": "novel"
            },
            "microsoft": {
                "stemmed": "microsoft"
            },
            "object": {
                "stemmed": "object"
            },
            "bay": {
                "stemmed": "bay"
            },
            "computer": {
                "stemmed": "comput"
            },
            "vrml": {
                "stemmed": "vrml"
            },
            "database": {
                "stemmed": "databas"
            },
            "networks": {
                "stemmed": "network"
            },
            "classes": {
                "stemmed": "class"
            },
            "gui": {
                "stemmed": "gui"
            },
            "software": {
                "stemmed": "softwar"
            },
            "server": {
                "stemmed": "server"
            },
            "tune": {
                "stemmed": "tune"
            },
            "whiz": {
                "stemmed": "whiz"
            },
            "date": {
                "stemmed": "date"
            },
            "stuff": {
                "stemmed": "stuff"
            },
            "practicum": {
                "stemmed": "practicum"
            },
            "hobbies": {
                "stemmed": "hobbi"
            },
            "html": {
                "stemmed": "html"
            },
            "practical": {
                "stemmed": "practic"
            },
            "fall": {
                "stemmed": "fall"
            },
            "wednesday": {
                "stemmed": "wednesday"
            },
            "ithaca": {
                "stemmed": "ithaca"
            },
            "icube": {
                "stemmed": "icub"
            },
            "lucy": {
                "stemmed": "luci"
            },
            "mtv": {
                "stemmed": "mtv"
            },
            "chinachineserelated": {
                "stemmed": "chinachineserel"
            },
            "management": {
                "stemmed": "manag"
            },
            "page": {
                "stemmed": "page"
            },
            "applications": {
                "stemmed": "applic"
            },
            "pc": {
                "stemmed": "pc"
            },
            "oriented": {
                "stemmed": "orient"
            },
            "computing": {
                "stemmed": "comput"
            },
            "businessweb": {
                "stemmed": "businessweb"
            },
            "caltech": {
                "stemmed": "caltech"
            },
            "search": {
                "stemmed": "search"
            },
            "travelers": {
                "stemmed": "travel"
            },
            "pingpong": {
                "stemmed": "pingpong"
            },
            "yuwucscornelledu": {
                "stemmed": "yuwucscornelledu"
            },
            "yulucy": {
                "stemmed": "yuluci"
            },
            "netscape": {
                "stemmed": "netscap"
            },
            "systems": {
                "stemmed": "system"
            },
            "products": {
                "stemmed": "product"
            },
            "project": {
                "stemmed": "project"
            },
            "chinese": {
                "stemmed": "chines"
            },
            "science": {
                "stemmed": "scienc"
            },
            "cgi": {
                "stemmed": "cgi"
            },
            "underground": {
                "stemmed": "underground"
            },
            "sco": {
                "stemmed": "sco"
            },
            "operating": {
                "stemmed": "oper"
            },
            "contact": {
                "stemmed": "contact"
            },
            "welcome": {
                "stemmed": "welcom"
            },
            "corba": {
                "stemmed": "corba"
            },
            "jobtrack": {
                "stemmed": "jobtrack"
            },
            "travel": {
                "stemmed": "travel"
            },
            "wu": {
                "stemmed": "wu"
            },
            "ipatm": {
                "stemmed": "ipatm"
            },
            "music": {
                "stemmed": "music"
            },
            "etc": {
                "stemmed": "etc"
            },
            "artvark": {
                "stemmed": "artvark"
            },
            "badminton": {
                "stemmed": "badminton"
            },
            "sites": {
                "stemmed": "site"
            },
            "sunlab": {
                "stemmed": "sunlab"
            },
            "cco": {
                "stemmed": "cco"
            },
            "department": {
                "stemmed": "depart"
            },
            "analysis": {
                "stemmed": "analysi"
            },
            "sapient": {
                "stemmed": "sapient"
            },
            "aug": {
                "stemmed": "aug"
            },
            "toolsmeng": {
                "stemmed": "toolsmeng"
            },
            "home": {
                "stemmed": "home"
            },
            "irs": {
                "stemmed": "ir"
            },
            "gallery": {
                "stemmed": "galleri"
            },
            "language": {
                "stemmed": "languag"
            },
            "news": {
                "stemmed": "news"
            },
            "lube": {
                "stemmed": "lube"
            },
            "omg": {
                "stemmed": "omg"
            },
            "topics": {
                "stemmed": "topic"
            },
            "meng": {
                "stemmed": "meng"
            },
            "sunday": {
                "stemmed": "sunday"
            },
            "nba": {
                "stemmed": "nba"
            },
            "degree": {
                "stemmed": "degre"
            },
            "tcltk": {
                "stemmed": "tcltk"
            },
            "swimming": {
                "stemmed": "swim"
            },
            "china": {
                "stemmed": "china"
            },
            "cs": {
                "stemmed": "cs"
            },
            "ny": {
                "stemmed": "ny"
            },
            "spring": {
                "stemmed": "spring"
            },
            "library": {
                "stemmed": "librari"
            },
            "system": {
                "stemmed": "system"
            },
            "resume": {
                "stemmed": "resum"
            },
            "silvano": {
                "stemmed": "silvano"
            },
            "sap": {
                "stemmed": "sap"
            },
            "favorite": {
                "stemmed": "favorit"
            },
            "student": {
                "stemmed": "student"
            },
            "network": {
                "stemmed": "network"
            },
            "personal": {
                "stemmed": "person"
            },
            "ipng": {
                "stemmed": "ipng"
            },
            "stock": {
                "stemmed": "stock"
            },
            "sun": {
                "stemmed": "sun"
            },
            "photograph": {
                "stemmed": "photograph"
            },
            "distributed": {
                "stemmed": "distribut"
            },
            "catalog": {
                "stemmed": "catalog"
            }
        },
        "stemmed_words": {
            "multimedia": {
                "occurrences": 1
            },
            "sap": {
                "occurrences": 1
            },
            "nov": {
                "occurrences": 1
            },
            "program": {
                "occurrences": 1
            },
            "secur": {
                "occurrences": 1
            },
            "java": {
                "occurrences": 1
            },
            "wus": {
                "occurrences": 1
            },
            "taichi": {
                "occurrences": 1
            },
            "mail": {
                "occurrences": 1
            },
            "hot": {
                "occurrences": 1
            },
            "comput": {
                "occurrences": 4
            },
            "cnn": {
                "occurrences": 1
            },
            "welcom": {
                "occurrences": 1
            },
            "ir": {
                "occurrences": 1
            },
            "www": {
                "occurrences": 1
            },
            "degre": {
                "occurrences": 1
            },
            "chines": {
                "occurrences": 1
            },
            "internet": {
                "occurrences": 3
            },
            "sapient": {
                "occurrences": 1
            },
            "misc": {
                "occurrences": 1
            },
            "oper": {
                "occurrences": 2
            },
            "microsoft": {
                "occurrences": 1
            },
            "object": {
                "occurrences": 1
            },
            "bay": {
                "occurrences": 1
            },
            "vrml": {
                "occurrences": 1
            },
            "cgi": {
                "occurrences": 1
            },
            "gui": {
                "occurrences": 1
            },
            "icub": {
                "occurrences": 1
            },
            "depart": {
                "occurrences": 1
            },
            "tune": {
                "occurrences": 1
            },
            "whiz": {
                "occurrences": 1
            },
            "date": {
                "occurrences": 1
            },
            "stuff": {
                "occurrences": 2
            },
            "scienc": {
                "occurrences": 1
            },
            "silvano": {
                "occurrences": 1
            },
            "practic": {
                "occurrences": 1
            },
            "favorit": {
                "occurrences": 1
            },
            "html": {
                "occurrences": 1
            },
            "chinachineserel": {
                "occurrences": 1
            },
            "fall": {
                "occurrences": 1
            },
            "wednesday": {
                "occurrences": 1
            },
            "ithaca": {
                "occurrences": 1
            },
            "underground": {
                "occurrences": 1
            },
            "page": {
                "occurrences": 3
            },
            "businessweb": {
                "occurrences": 1
            },
            "pc": {
                "occurrences": 1
            },
            "cornel": {
                "occurrences": 2
            },
            "caltech": {
                "occurrences": 1
            },
            "search": {
                "occurrences": 1
            },
            "pingpong": {
                "occurrences": 1
            },
            "orient": {
                "occurrences": 1
            },
            "yuwucscornelledu": {
                "occurrences": 1
            },
            "hobbi": {
                "occurrences": 1
            },
            "librari": {
                "occurrences": 1
            },
            "read": {
                "occurrences": 1
            },
            "distribut": {
                "occurrences": 3
            },
            "swim": {
                "occurrences": 1
            },
            "engin": {
                "occurrences": 1
            },
            "languag": {
                "occurrences": 3
            },
            "galleri": {
                "occurrences": 1
            },
            "topic": {
                "occurrences": 1
            },
            "databas": {
                "occurrences": 3
            },
            "connect": {
                "occurrences": 1
            },
            "sco": {
                "occurrences": 1
            },
            "contact": {
                "occurrences": 1
            },
            "corba": {
                "occurrences": 1
            },
            "applic": {
                "occurrences": 1
            },
            "travel": {
                "occurrences": 2
            },
            "network": {
                "occurrences": 4
            },
            "ipatm": {
                "occurrences": 1
            },
            "music": {
                "occurrences": 2
            },
            "etc": {
                "occurrences": 1
            },
            "artvark": {
                "occurrences": 1
            },
            "badminton": {
                "occurrences": 1
            },
            "sunlab": {
                "occurrences": 1
            },
            "ipng": {
                "occurrences": 1
            },
            "cco": {
                "occurrences": 1
            },
            "web": {
                "occurrences": 2
            },
            "stock": {
                "occurrences": 1
            },
            "manag": {
                "occurrences": 2
            },
            "toolsmeng": {
                "occurrences": 1
            },
            "home": {
                "occurrences": 3
            },
            "news": {
                "occurrences": 1
            },
            "site": {
                "occurrences": 2
            },
            "product": {
                "occurrences": 1
            },
            "interest": {
                "occurrences": 1
            },
            "univers": {
                "occurrences": 1
            },
            "meng": {
                "occurrences": 1
            },
            "sunday": {
                "occurrences": 1
            },
            "nba": {
                "occurrences": 1
            },
            "compani": {
                "occurrences": 1
            },
            "analysi": {
                "occurrences": 1
            },
            "jobtrack": {
                "occurrences": 1
            },
            "tcltk": {
                "occurrences": 1
            },
            "mtv": {
                "occurrences": 1
            },
            "china": {
                "occurrences": 1
            },
            "project": {
                "occurrences": 1
            },
            "archiv": {
                "occurrences": 1
            },
            "novel": {
                "occurrences": 1
            },
            "cs": {
                "occurrences": 6
            },
            "ny": {
                "occurrences": 1
            },
            "server": {
                "occurrences": 2
            },
            "spring": {
                "occurrences": 2
            },
            "softwar": {
                "occurrences": 2
            },
            "system": {
                "occurrences": 7
            },
            "practicum": {
                "occurrences": 1
            },
            "resum": {
                "occurrences": 1
            },
            "lube": {
                "occurrences": 1
            },
            "student": {
                "occurrences": 1
            },
            "luci": {
                "occurrences": 1
            },
            "wu": {
                "occurrences": 1
            },
            "aug": {
                "occurrences": 1
            },
            "yuluci": {
                "occurrences": 1
            },
            "sun": {
                "occurrences": 2
            },
            "omg": {
                "occurrences": 1
            },
            "person": {
                "occurrences": 1
            },
            "photograph": {
                "occurrences": 1
            },
            "class": {
                "occurrences": 2
            },
            "netscap": {
                "occurrences": 1
            },
            "catalog": {
                "occurrences": 1
            }
        },
        "category": "student"
    }}
    predictions=[]
    k = 3
    for key in test_data:

        # Returns K number of nearest neighbors
        neighbors = msC.getNeighbors(test_data[key]['stemmed_words'], k)
        
        # Gets the classification of the the surrounding neighbors with the most members present
        classification = msC.getNeighborsVotes(neighbors)


main()