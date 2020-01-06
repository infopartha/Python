"""ezhuthu = {
'அ':{'ezhuthu':'அ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'அ','thaniEzhuthu':True}
,'ஆ':{'ezhuthu':'ஆ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஆ','thaniEzhuthu':True}
,'இ':{'ezhuthu':'இ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'இ','thaniEzhuthu':True}
,'ஈ':{'ezhuthu':'ஈ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஈ','thaniEzhuthu':True}
,'உ':{'ezhuthu':'உ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'உ','thaniEzhuthu':True}
,'ஊ':{'ezhuthu':'ஊ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஊ','thaniEzhuthu':True}
,'எ':{'ezhuthu':'எ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'எ','thaniEzhuthu':True}
,'ஏ':{'ezhuthu':'ஏ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஏ','thaniEzhuthu':True}
,'ஐ':{'ezhuthu':'ஐ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஐ','thaniEzhuthu':True}
,'ஒ':{'ezhuthu':'ஒ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'ஒ','thaniEzhuthu':True}
,'ஓ':{'ezhuthu':'ஓ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஓ','thaniEzhuthu':True}
,'ஔ':{'ezhuthu':'ஔ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஔ','thaniEzhuthu':True}
,'க':{'ezhuthu':'க','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ங':{'ezhuthu':'ங','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ச':{'ezhuthu':'ச','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ஞ':{'ezhuthu':'ஞ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ட':{'ezhuthu':'ட','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ண':{'ezhuthu':'ண','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'த':{'ezhuthu':'த','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ந':{'ezhuthu':'ந','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ப':{'ezhuthu':'ப','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ம':{'ezhuthu':'ம','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ய':{'ezhuthu':'ய','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ','thaniEzhuthu':True}
,'ர':{'ezhuthu':'ர','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ','thaniEzhuthu':True}
,'ல':{'ezhuthu':'ல','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ','thaniEzhuthu':True}
,'வ':{'ezhuthu':'வ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ','thaniEzhuthu':True}
,'ழ':{'ezhuthu':'ழ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ','thaniEzhuthu':True}
,'ள':{'ezhuthu':'ள','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ','thaniEzhuthu':True}
,'ற':{'ezhuthu':'ற','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'ன':{'ezhuthu':'ன','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ','thaniEzhuthu':True}
,'்':{'ezhuthu':'்','vagai':'ஒற்று','alavu':'ஒற்று','inam':'','uyir':'','thaniEzhuthu':False}
,'ா':{'ezhuthu':'ா','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஆ','thaniEzhuthu':False}
,'ி':{'ezhuthu':'ி','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'','uyir':'இ','thaniEzhuthu':False}
,'ீ':{'ezhuthu':'ீ','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஈ','thaniEzhuthu':False}
,'ு':{'ezhuthu':'ு','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'','uyir':'உ','thaniEzhuthu':False}
,'ூ':{'ezhuthu':'ூ','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஊ','thaniEzhuthu':False}
,'ெ':{'ezhuthu':'ெ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'','uyir':'எ','thaniEzhuthu':False}
,'ே':{'ezhuthu':'ே','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஏ','thaniEzhuthu':False}
,'ை':{'ezhuthu':'ை','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஐ','thaniEzhuthu':False}
,'ொ':{'ezhuthu':'ொ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'','uyir':'ஒ','thaniEzhuthu':False}
,'ோ':{'ezhuthu':'ோ','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஓ','thaniEzhuthu':False}
,'ௌ':{'ezhuthu':'ௌ','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஔ','thaniEzhuthu':False}
,'ஃ':{'ezhuthu':'ஃ','vagai':'ஆய்தம்','alavu':'நெடில்','inam':'','uyir':'','thaniEzhuthu':True}
,'':{'ezhuthu':'','vagai':'','alavu':'','inam':'','uyir':'','thaniEzhuthu':None}
}
"""

ezhuthu = {
    'அ': {'ezhuthu': 'அ', 'vagai': 'உயிர்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2949},
    'ஆ': {'ezhuthu': 'ஆ', 'vagai': 'உயிர்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஆ', 'thaniEzhuthu': True, 'ucode': 2950},
    'இ': {'ezhuthu': 'இ', 'vagai': 'உயிர்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'இ', 'thaniEzhuthu': True, 'ucode': 2951},
    'ஈ': {'ezhuthu': 'ஈ', 'vagai': 'உயிர்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஈ', 'thaniEzhuthu': True, 'ucode': 2952},
    'உ': {'ezhuthu': 'உ', 'vagai': 'உயிர்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'உ', 'thaniEzhuthu': True, 'ucode': 2953},
    'ஊ': {'ezhuthu': 'ஊ', 'vagai': 'உயிர்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஊ', 'thaniEzhuthu': True, 'ucode': 2954},
    'எ': {'ezhuthu': 'எ', 'vagai': 'உயிர்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'எ', 'thaniEzhuthu': True, 'ucode': 2958},
    'ஏ': {'ezhuthu': 'ஏ', 'vagai': 'உயிர்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஏ', 'thaniEzhuthu': True, 'ucode': 2959},
    'ஐ': {'ezhuthu': 'ஐ', 'vagai': 'உயிர்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஐ', 'thaniEzhuthu': True, 'ucode': 2960},
    'ஒ': {'ezhuthu': 'ஒ', 'vagai': 'உயிர்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'ஒ', 'thaniEzhuthu': True, 'ucode': 2962},
    'ஓ': {'ezhuthu': 'ஓ', 'vagai': 'உயிர்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஓ', 'thaniEzhuthu': True, 'ucode': 2963},
    'ஔ': {'ezhuthu': 'ஔ', 'vagai': 'உயிர்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஔ', 'thaniEzhuthu': True, 'ucode': 2964},
    'க': {'ezhuthu': 'க', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'வல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2965},
    'ங': {'ezhuthu': 'ங', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'மெல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2969},
    'ச': {'ezhuthu': 'ச', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'வல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2970},
    'ஞ': {'ezhuthu': 'ஞ', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'மெல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2974},
    'ட': {'ezhuthu': 'ட', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'வல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2975},
    'ண': {'ezhuthu': 'ண', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'மெல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2979},
    'த': {'ezhuthu': 'த', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'வல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2980},
    'ந': {'ezhuthu': 'ந', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'மெல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2984},
    'ப': {'ezhuthu': 'ப', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'வல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2986},
    'ம': {'ezhuthu': 'ம', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'மெல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2990},
    'ய': {'ezhuthu': 'ய', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'இடையினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2991},
    'ர': {'ezhuthu': 'ர', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'இடையினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2992},
    'ல': {'ezhuthu': 'ல', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'இடையினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2994},
    'வ': {'ezhuthu': 'வ', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'இடையினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2997},
    'ழ': {'ezhuthu': 'ழ', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'இடையினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2996},
    'ள': {'ezhuthu': 'ள', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'இடையினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2995},
    'ற': {'ezhuthu': 'ற', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'வல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2993},
    'ன': {'ezhuthu': 'ன', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': 'மெல்லினம்', 'uyir': 'அ', 'thaniEzhuthu': True, 'ucode': 2985},
    '்': {'ezhuthu': '்', 'vagai': 'ஒற்று', 'alavu': 'ஒற்று', 'inam': '', 'uyir': '', 'thaniEzhuthu': False, 'ucode': 3021},
    'ா': {'ezhuthu': 'ா', 'vagai': 'உயிர்மெய்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஆ', 'thaniEzhuthu': False, 'ucode': 3006},
    'ி': {'ezhuthu': 'ி', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'இ', 'thaniEzhuthu': False, 'ucode': 3007},
    'ீ': {'ezhuthu': 'ீ', 'vagai': 'உயிர்மெய்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஈ', 'thaniEzhuthu': False, 'ucode': 3008},
    'ு': {'ezhuthu': 'ு', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'உ', 'thaniEzhuthu': False, 'ucode': 3009},
    'ூ': {'ezhuthu': 'ூ', 'vagai': 'உயிர்மெய்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஊ', 'thaniEzhuthu': False, 'ucode': 3010},
    'ெ': {'ezhuthu': 'ெ', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'எ', 'thaniEzhuthu': False, 'ucode': 3014},
    'ே': {'ezhuthu': 'ே', 'vagai': 'உயிர்மெய்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஏ', 'thaniEzhuthu': False, 'ucode': 3015},
    'ை': {'ezhuthu': 'ை', 'vagai': 'உயிர்மெய்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஐ', 'thaniEzhuthu': False, 'ucode': 3016},
    'ொ': {'ezhuthu': 'ொ', 'vagai': 'உயிர்மெய்', 'alavu': 'குறில்', 'inam': '', 'uyir': 'ஒ', 'thaniEzhuthu': False, 'ucode': 3018},
    'ோ': {'ezhuthu': 'ோ', 'vagai': 'உயிர்மெய்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஓ', 'thaniEzhuthu': False, 'ucode': 3019},
    'ௌ': {'ezhuthu': 'ௌ', 'vagai': 'உயிர்மெய்', 'alavu': 'நெடில்', 'inam': '', 'uyir': 'ஔ', 'thaniEzhuthu': False, 'ucode': 3020},
    'ஃ': {'ezhuthu': 'ஃ', 'vagai': 'ஆய்தம்', 'alavu': 'நெடில்', 'inam': '', 'uyir': '', 'thaniEzhuthu': True, 'ucode': 2947},
    '': {'ezhuthu': '', 'vagai': '', 'alavu': '', 'inam': '', 'uyir': '', 'thaniEzhuthu': None, 'ucode': None},
}

def vagai(Ezhuthu):
    return ezhuthu.get(Ezhuthu,ezhuthu.get(''))['vagai']

def inam(Ezhuthu):
    return ezhuthu.get(Ezhuthu,ezhuthu.get(''))['inam']

def uyir(Ezhuthu):
    return ezhuthu.get(Ezhuthu,ezhuthu.get(''))['uyir']

def thaniEzhuthu(Ezhuthu):
    return ezhuthu.get(Ezhuthu,ezhuthu.get(''))['thaniEzhuthu']

def ucode(Ezhuthu):
    return ezhuthu.get(Ezhuthu,ezhuthu.get(''))['ucode']