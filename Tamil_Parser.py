# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 08:02:59 2019

@author: Parthasarathy R
"""

ezhuthu = {
'அ':{'ezhuthu':'அ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'அ'}
,'ஆ':{'ezhuthu':'ஆ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஆ'}
,'இ':{'ezhuthu':'இ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'இ'}
,'ஈ':{'ezhuthu':'ஈ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஈ'}
,'உ':{'ezhuthu':'உ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'உ'}
,'ஊ':{'ezhuthu':'ஊ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஊ'}
,'எ':{'ezhuthu':'எ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'எ'}
,'ஏ':{'ezhuthu':'ஏ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஏ'}
,'ஐ':{'ezhuthu':'ஐ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஐ'}
,'ஒ':{'ezhuthu':'ஒ','vagai':'உயிர்','alavu':'குறில்','inam':'','uyir':'ஒ'}
,'ஓ':{'ezhuthu':'ஓ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஓ'}
,'ஔ':{'ezhuthu':'ஔ','vagai':'உயிர்','alavu':'நெடில்','inam':'','uyir':'ஔ'}
,'க':{'ezhuthu':'க','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ'}
,'ங':{'ezhuthu':'ங','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ'}
,'ச':{'ezhuthu':'ச','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ'}
,'ஞ':{'ezhuthu':'ஞ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ'}
,'ட':{'ezhuthu':'ட','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ'}
,'ண':{'ezhuthu':'ண','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ'}
,'த':{'ezhuthu':'த','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ'}
,'ந':{'ezhuthu':'ந','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ'}
,'ப':{'ezhuthu':'ப','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ'}
,'ம':{'ezhuthu':'ம','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ'}
,'ய':{'ezhuthu':'ய','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ'}
,'ர':{'ezhuthu':'ர','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ'}
,'ல':{'ezhuthu':'ல','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ'}
,'வ':{'ezhuthu':'வ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ'}
,'ழ':{'ezhuthu':'ழ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ'}
,'ள':{'ezhuthu':'ள','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'இடையினம்','uyir':'அ'}
,'ற':{'ezhuthu':'ற','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'வல்லினம்','uyir':'அ'}
,'ன':{'ezhuthu':'ன','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'மெல்லினம்','uyir':'அ'}
,'்':{'ezhuthu':'்','vagai':'ஒற்று','alavu':'ஒற்று','inam':'','uyir':''}
,'ா':{'ezhuthu':'ா','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஆ'}
,'ி':{'ezhuthu':'ி','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'','uyir':'இ'}
,'ீ':{'ezhuthu':'ீ','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஈ'}
,'ு':{'ezhuthu':'ு','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'','uyir':'உ'}
,'ூ':{'ezhuthu':'ூ','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஊ'}
,'ெ':{'ezhuthu':'ெ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'','uyir':'எ'}
,'ே':{'ezhuthu':'ே','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஏ'}
,'ை':{'ezhuthu':'ை','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஐ'}
,'ொ':{'ezhuthu':'ொ','vagai':'உயிர்மெய்','alavu':'குறில்','inam':'','uyir':'ஒ'}
,'ோ':{'ezhuthu':'ோ','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஓ'}
,'ௌ':{'ezhuthu':'ௌ','vagai':'உயிர்மெய்','alavu':'நெடில்','inam':'','uyir':'ஔ'}
,'ஃ':{'ezhuthu':'ஃ','vagai':'ஆய்தம்','alavu':'நெடில்','inam':'','uyir':''}
}

word = 'தமிழ்'
print(ezhuthu[word[0]])
