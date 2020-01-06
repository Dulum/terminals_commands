from sys import argv

ENG_QWERTY = "`qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./"
HEB_QWERTY = ";/\'קראטוןםפ][\\שדגכעיחלךף,זסבהנמצתץ."

ENG_TO_HEB = dict(zip(list(ENG_QWERTY), list(HEB_QWERTY)))
HEB_TO_ENG = dict(zip(list(HEB_QWERTY), list(ENG_QWERTY)))
TRANSLATION_DICS_DIC = {'eng': ENG_TO_HEB, 'heb': HEB_TO_ENG}

def translate_string(st):
    cur_lan = evaluate_language(st)
    return translate_from(st, cur_lan)

def evaluate_language(st): # only works for hebrew/english
    lan = ''
    for c in st:
        if c in ENG_QWERTY and not c in HEB_QWERTY:
            if not lan:
                lan = 'eng'
                
            elif lan == 'eng':
                pass
            
            else:
                return ''
        
        elif c in HEB_QWERTY and not c in ENG_QWERTY:
            if not lan:
                lan = 'heb'
            elif lan == 'heb':
                pass
            else:
                return ''
    
    return lan

def translate_from(st, cur_lan):
    if cur_lan == 'Undefined':
        return
    
    translation_dic = TRANSLATION_DICS_DIC[cur_lan]
    translated_st = ''
    for c in st:
        if c in translation_dic:
            translated_st += translation_dic[c]
        else:
            translated_st += c
    
    return translated_st

def main():
    print(translate_string(argv[1]))

if __name__ == "__main__":
    main()