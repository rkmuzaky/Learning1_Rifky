def Camel_case(kalimat, delimiter=" ", ignore_words=[]):
    words = kalimat.split(delimiter)
    cc_words = []
    
    for word in  words:
        if word in ignore_words:
            cc_words.append(word)
        else:
            cc_words.append(word.capitalize())
            
    cc_string = ' '.join(cc_words)
    return cc_string

kalimat = "saya adalah seorang pengusaha sukses"
ignore_list = ["adalah"]
cc_result = Camel_case(kalimat, delimiter=" ", ignore_words=ignore_list)

print(kalimat)
print(kalimat.split(" "))
print(cc_result.split(" "))
print(cc_result)