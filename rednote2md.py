# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:50:33 2022

@author: Lu Haitao

rednotebook格式转换为markdown
"""



import re
import os
import shutil

os.chdir(os.getcwd())


def lis_ext(ext):
    """"

    """
    lis = os.listdir()
    lisext = []
    for i in lis:
        if os.path.splitext(i)[1] == '.' + ext:
            lisext.append(i)
            pass
        else:
            # lis.remove(i)
            pass
    return lisext


def to_md(lis):
    for i in lis:
        date = os.path.splitext(i)[0]
        try:
            os.remove(date + '.md')
        except BaseException:
            pass
        finally:

            with open(i, 'r', encoding="u8") as f, open(date + '.md', 'w', encoding="u8") as fo:
                fl = f.read()
                sc = re.findall(r'(\d+:)\s({[\s\S]*?})', fl)
                for i in sc:
                    # 判断是''还是""开头
                    blocktype = re.findall('("[\s\S]*?")',i[1])
                    if blocktype:
                        scy = i[1].replace('"', "'")
                        scy = scy.replace('\n    ','')
                        scy = scy.replace('\\n', "\n")
                    else:
                        scy = i[1]
                        scy = scy.replace('\n    ', "\n")
                    scx = re.findall(r'(\'[\s\S]*?\')', scy)
                       
# =============================================================================
#                     scy = i[1].replace('"', "'")
#                     scy = scy.replace('\\n', "\n")
#                     scy = scy.replace('\n    ', "\n")
#                     scx = re.findall(r'(\'[\s\S]*?\')', scy)
# =============================================================================
                    #                    print(scx,i)
                    if scx:
                        fo.write('# ' + date + '-' + i[0].rstrip(':') + ' \n\n' + scx[0].replace("'", '') + '\n\n')


def mdtitle(string):
    # 标题修改
    s = re.findall('(^=+(.*?)=+$)',string)
    if s:
        dengji = int(s[0][0].count('=')/2)
        print(s)
        out = '#'*dengji+' '+s[0][1]
    else:
        out = string
    # 删除单独空行上的四个空格
    if out.startswith("    "):
        out = out.lstrip("    ")
                
    if len(out)>1 and out.startswith('\\'):
        out = out.lstrip("\\")
    if out.endswith("+\n") or out.endswith("-\n"):
        out = out.rstrip("\n")
        out = out+" "
        
    if out.startswith("+") or out.startswith("-"):
        if out.startswith("+ ") or out.startswith("- "):
            pass
        else:
            if out.startswith("-"):
                out = '- '+out.lstrip('-')
            else:
                out = '+ '+out.lstrip('+')
    if re.match('(^\s+-\S)',out):
        out = out.replace('-','- ')
    if re.match('(^\s+\+\S)',out):
        out = out.replace('+','+ ')
                

    return out

def mdopt(lis):
    for i in lis:
# =============================================================================
#         with open(i, 'w+') as f,open(i, 'w+') as fo:
#             fl = f.readline()
#             while fl:
#                 fo.write(mdtitle(fl))
#                 f = f.readline()
# =============================================================================
        shutil.copyfile(i,'temp'+i)
        with open('temp'+i, 'r', encoding="u8") as f, open( i, 'w', encoding="u8") as fo:
            fl = f.readline()
            while fl:
                fo.write(mdtitle(fl))
                fl = f.readline()
        os.remove('temp'+i)

if __name__ == "__main__":
    to_md(lis_ext('txt'))
    mdopt(lis_ext('md'))
    pass

# print(lis_ext('txt'))

# =============================================================================
# 
# with open('2020-09.txt','r', encoding="u8") as f:
#     fl = f.read()
#     
# s = re.findall(r'({.*?})',fl)
# sa = 'sdf{wef}dd{fse}d'
# sb = re.findall(r'({[\s\S]*?})',fl)
# sc = re.findall(r'(\d+:)\s({[\s\S]*?})',fl)
# scc = sc[0][1]
# scx = re.findall(r'(\'[\s\S]*?\')',scc)
# 
# =============================================================================
