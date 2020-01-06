# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 02:40:47 2020

@author: MAGIZHINI
"""

from ezhuthu import ezhuthu, vagai, inam, uyir, thaniEzhuthu, ucode

word = 'தமிழ்'
print(len(word))

lstuni=list()
for lt in word:
    print('%s : %s ~ %s ~%s' % (lt, vagai(lt), inam(lt), uyir(lt)))
    lstuni.append(ucode(lt))

print(''.join(list(map(chr,lstuni))))

print(len(list(filter(thaniEzhuthu,word))))

ord('மி'[0]), ord('மி'[1])
chr(2990) + chr(3007)

#print('{')
#for lt in ezhuthu:
#    print("    '%s': {'ezhuthu': '%s', 'vagai': '%s', 'alavu': '%s', 'inam': '%s', 'uyir': '%s', 'thaniEzhuthu': %s, 'ucode': %s}," % tuple([lt] + list(ezhuthu[lt].values()) + [None if lt=='' else ord(lt)]))
#print('}')
