digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

lang_trans = {}
i = len(digits)
for i in range(len(digits)):
    lang_trans[digits[i]] = {'french': fr[i], 'english': en[i]}
print(lang_trans)    
