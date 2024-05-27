>>> from seminar_14.task1 import validate_str_only_lat

>>> validate_str_only_lat('this string return without changes')
'this string return without changes'

>>> validate_str_only_lat('This String RetUrn witHout chanGeS')
'this string return without changes'

>>> validate_str_only_lat('this. string, return! without? changes')
'this string return without changes'

>>> validate_str_only_lat('thрорваis strinоажыg reываturn ываwithout changesыва')
'this string return without changes'

>>> validate_str_only_lat('tHрорваiS! stRinоажыg? r.eываTurn ыва,withOut Chan:gesыва')
'this string return without changes'