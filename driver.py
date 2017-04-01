from CharlotteKnn import CharlotteKnn

def main():
    msC = CharlotteKnn()

    test_data = {
        "http_^^cs.cornell.edu^Info^Courses^Current^CS415^CS414.html": {
            "words": {
                "server": {
                    "stemmed": "server"
                },
                "date": {
                    "stemmed": "date"
                },
                "sunday": {
                    "stemmed": "sunday"
                },
                "dec": {
                    "stemmed": "dec"
                },
                "tuesday": {
                    "stemmed": "tuesday"
                },
                "nov": {
                    "stemmed": "nov"
                },
                "cs": {
                    "stemmed": "cs"
                },
                "home": {
                    "stemmed": "home"
                },
                "page": {
                    "stemmed": "page"
                },
                "systems": {
                    "stemmed": "system"
                },
                "programming": {
                    "stemmed": "program"
                },
                "operating": {
                    "stemmed": "oper"
                },
                "practicum": {
                    "stemmed": "practicum"
                },
                "system": {
                    "stemmed": "system"
                },
                "kenneth": {
                    "stemmed": "kenneth"
                },
                "p": {
                    "stemmed": "p"
                },
                "birman": {
                    "stemmed": "birman"
                },
                "news": {
                    "stemmed": "news"
                },
                "group": {
                    "stemmed": "group"
                },
                "course": {
                    "stemmed": "cours"
                },
                "syllabus": {
                    "stemmed": "syllabus"
                },
                "lecture": {
                    "stemmed": "lectur"
                },
                "notes": {
                    "stemmed": "note"
                },
                "unix": {
                    "stemmed": "unix"
                },
                "filesystem": {
                    "stemmed": "filesystem"
                },
                "structure": {
                    "stemmed": "structur"
                },
                "linking": {
                    "stemmed": "link"
                },
                "static": {
                    "stemmed": "static"
                },
                "dynamic": {
                    "stemmed": "dynam"
                },
                "assignments": {
                    "stemmed": "assign"
                },
                "homework": {
                    "stemmed": "homework"
                },
                "assignment": {
                    "stemmed": "assign"
                },
                "solutions": {
                    "stemmed": "solut"
                },
                "solution": {
                    "stemmed": "solut"
                },
                "prelim": {
                    "stemmed": "prelim"
                },
                "tas": {
                    "stemmed": "tas"
                },
                "lili": {
                    "stemmed": "lili"
                },
                "upson": {
                    "stemmed": "upson"
                },
                "hall": {
                    "stemmed": "hall"
                },
                "phone": {
                    "stemmed": "phone"
                },
                "email": {
                    "stemmed": "email"
                },
                "lilicscornelledu": {
                    "stemmed": "lilicscornelledu"
                },
                "office": {
                    "stemmed": "offic"
                },
                "hours": {
                    "stemmed": "hour"
                },
                "wednesday": {
                    "stemmed": "wednesday"
                },
                "friday": {
                    "stemmed": "friday"
                },
                "yicheng": {
                    "stemmed": "yicheng"
                },
                "huang": {
                    "stemmed": "huang"
                },
                "ychuangcscornelledu": {
                    "stemmed": "ychuangcscornelledu"
                },
                "thursday": {
                    "stemmed": "thursday"
                },
                "mihai": {
                    "stemmed": "mihai"
                },
                "budiu": {
                    "stemmed": "budiu"
                },
                "budiucscornelledu": {
                    "stemmed": "budiucscornelledu"
                },
                "last": {
                    "stemmed": "last"
                },
                "modified": {
                    "stemmed": "modifi"
                },
                "tue": {
                    "stemmed": "tue"
                }
            },
            "stemmed_words": {
                "server": {
                    "occurrences": 1
                },
                "date": {
                    "occurrences": 1
                },
                "sunday": {
                    "occurrences": 1
                },
                "dec": {
                    "occurrences": 1
                },
                "tuesday": {
                    "occurrences": 2
                },
                "nov": {
                    "occurrences": 2
                },
                "cs": {
                    "occurrences": 4
                },
                "home": {
                    "occurrences": 1
                },
                "page": {
                    "occurrences": 1
                },
                "system": {
                    "occurrences": 3
                },
                "program": {
                    "occurrences": 1
                },
                "oper": {
                    "occurrences": 2
                },
                "practicum": {
                    "occurrences": 1
                },
                "kenneth": {
                    "occurrences": 1
                },
                "p": {
                    "occurrences": 1
                },
                "birman": {
                    "occurrences": 1
                },
                "news": {
                    "occurrences": 1
                },
                "group": {
                    "occurrences": 1
                },
                "cours": {
                    "occurrences": 1
                },
                "syllabus": {
                    "occurrences": 1
                },
                "lectur": {
                    "occurrences": 1
                },
                "note": {
                    "occurrences": 1
                },
                "unix": {
                    "occurrences": 1
                },
                "filesystem": {
                    "occurrences": 1
                },
                "structur": {
                    "occurrences": 1
                },
                "link": {
                    "occurrences": 1
                },
                "static": {
                    "occurrences": 1
                },
                "dynam": {
                    "occurrences": 1
                },
                "assign": {
                    "occurrences": 2
                },
                "homework": {
                    "occurrences": 5
                },
                "solut": {
                    "occurrences": 6
                },
                "prelim": {
                    "occurrences": 1
                },
                "tas": {
                    "occurrences": 1
                },
                "lili": {
                    "occurrences": 1
                },
                "upson": {
                    "occurrences": 3
                },
                "hall": {
                    "occurrences": 3
                },
                "phone": {
                    "occurrences": 3
                },
                "email": {
                    "occurrences": 3
                },
                "lilicscornelledu": {
                    "occurrences": 1
                },
                "offic": {
                    "occurrences": 3
                },
                "hour": {
                    "occurrences": 3
                },
                "wednesday": {
                    "occurrences": 2
                },
                "friday": {
                    "occurrences": 1
                },
                "yicheng": {
                    "occurrences": 1
                },
                "huang": {
                    "occurrences": 1
                },
                "ychuangcscornelledu": {
                    "occurrences": 1
                },
                "thursday": {
                    "occurrences": 2
                },
                "mihai": {
                    "occurrences": 1
                },
                "budiu": {
                    "occurrences": 1
                },
                "budiucscornelledu": {
                    "occurrences": 1
                },
                "last": {
                    "occurrences": 1
                },
                "modifi": {
                    "occurrences": 1
                },
                "tue": {
                    "occurrences": 1
                }
            },
            "category": "course"
        },
        "http_^^www.cs.utexas.edu^users^almstrum^classes^cs336^fall96^": {
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
                "cs": {
                    "stemmed": "cs"
                },
                "analysis": {
                    "stemmed": "analysi"
                },
                "programs": {
                    "stemmed": "program"
                },
                "fall": {
                    "stemmed": "fall"
                },
                "instructor": {
                    "stemmed": "instructor"
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
                "ta": {
                    "stemmed": "ta"
                },
                "linyuan": {
                    "stemmed": "linyuan"
                },
                "yang": {
                    "stemmed": "yang"
                },
                "syllabus": {
                    "stemmed": "syllabus"
                },
                "announcements": {
                    "stemmed": "announc"
                },
                "homework": {
                    "stemmed": "homework"
                },
                "assignments": {
                    "stemmed": "assign"
                },
                "handouts": {
                    "stemmed": "handout"
                },
                "interesting": {
                    "stemmed": "interest"
                },
                "tutorials": {
                    "stemmed": "tutori"
                },
                "news": {
                    "stemmed": "news"
                },
                "utexasclasscsa": {
                    "stemmed": "utexasclasscsa"
                },
                "almstrums": {
                    "stemmed": "almstrum"
                },
                "homepage": {
                    "stemmed": "homepag"
                },
                "last": {
                    "stemmed": "last"
                },
                "updated": {
                    "stemmed": "updat"
                },
                "page": {
                    "stemmed": "page"
                },
                "prepared": {
                    "stemmed": "prepar"
                },
                "suggestions": {
                    "stemmed": "suggest"
                },
                "comments": {
                    "stemmed": "comment"
                },
                "welcome": {
                    "stemmed": "welcom"
                },
                "click": {
                    "stemmed": "click"
                },
                "send": {
                    "stemmed": "send"
                },
                "email": {
                    "stemmed": "email"
                },
                "almstrumcsutexasedu": {
                    "stemmed": "almstrumcsutexasedu"
                },
                "linyuancsutexasedu": {
                    "stemmed": "linyuancsutexasedu"
                },
                "department": {
                    "stemmed": "depart"
                },
                "computer": {
                    "stemmed": "comput"
                },
                "sciences": {
                    "stemmed": "scienc"
                },
                "ut": {
                    "stemmed": "ut"
                },
                "austin": {
                    "stemmed": "austin"
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
                "cs": {
                    "occurrences": 2
                },
                "analysi": {
                    "occurrences": 2
                },
                "program": {
                    "occurrences": 2
                },
                "fall": {
                    "occurrences": 1
                },
                "instructor": {
                    "occurrences": 2
                },
                "vicki": {
                    "occurrences": 2
                },
                "l": {
                    "occurrences": 2
                },
                "almstrum": {
                    "occurrences": 3
                },
                "ta": {
                    "occurrences": 1
                },
                "linyuan": {
                    "occurrences": 1
                },
                "yang": {
                    "occurrences": 1
                },
                "syllabus": {
                    "occurrences": 1
                },
                "announc": {
                    "occurrences": 1
                },
                "homework": {
                    "occurrences": 1
                },
                "assign": {
                    "occurrences": 1
                },
                "handout": {
                    "occurrences": 1
                },
                "interest": {
                    "occurrences": 1
                },
                "tutori": {
                    "occurrences": 1
                },
                "news": {
                    "occurrences": 1
                },
                "utexasclasscsa": {
                    "occurrences": 1
                },
                "homepag": {
                    "occurrences": 1
                },
                "last": {
                    "occurrences": 1
                },
                "updat": {
                    "occurrences": 1
                },
                "page": {
                    "occurrences": 1
                },
                "prepar": {
                    "occurrences": 1
                },
                "suggest": {
                    "occurrences": 1
                },
                "comment": {
                    "occurrences": 1
                },
                "welcom": {
                    "occurrences": 1
                },
                "click": {
                    "occurrences": 1
                },
                "send": {
                    "occurrences": 1
                },
                "email": {
                    "occurrences": 1
                },
                "almstrumcsutexasedu": {
                    "occurrences": 1
                },
                "linyuancsutexasedu": {
                    "occurrences": 1
                },
                "depart": {
                    "occurrences": 1
                },
                "comput": {
                    "occurrences": 1
                },
                "scienc": {
                    "occurrences": 1
                },
                "ut": {
                    "occurrences": 1
                },
                "austin": {
                    "occurrences": 1
                }
            },
            "category": "course"
    },       
    }
    predictions=[]
    k = 3
    for key in test_data:
        print(key)
        # Returns K number of nearest neighbors
        neighbors = msC.getNeighbors(test_data[key]['stemmed_words'], k)
        
        # Gets the classification of the the surrounding neighbors with the most members present
        classification = msC.getNeighborsVotes(neighbors)


main()