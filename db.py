#from tinymongo import TinyMongoClient
from tinydb import TinyDB, Query
import pandas as pd
import excel
import openpyxl
import xlrd

#!pip install xlrd==1.2.0
db = TinyDB('DB_JSON/db.json')

#===============================
#Cadastro Usuários
#===============================

def registerDB(firstname, lastname, email1, password1):
    return db.insert({'FIRST_NAME':firstname,'LAST_NAME':lastname,'EMAIL':email1,'PASSWORD':password1})


def readDB(email, password):
    result = False
    for i in db.all():
        print('-------------', i['EMAIL'], email.upper())
        if i['EMAIL'] == email.upper():
            if i['PASSWORD'] == password:
                result = [True, i['FIRST_NAME']]
                print('entrou!!!')
                return result
            else:
                return [False, 'FIRST_NAME']
        else:
            result = [True, 'FIRST_NAME']

    return result

Ft = Query()

def query_email_confere(email, password):
    new_db = db.search(Ft.EMAIL == email and Ft.PASSWORD == password)
  
    return new_db


#===================
## DONWLOAD
#==================

def create_list():
    export = pd.read_excel('static/mask_extratoIMZCOS.xlsx')
    meta = pd.read_excel('static/INT_DELNT_CRTL_META_REV.xlsx')
    extrato = pd.read_excel('static/EXTRATO_RAI.xlsx', 'RAIs')

    rai = extrato[['RAI','STATUS']]
    RAI = rai[rai['STATUS'] == 'Em Delineamento | Analisado']

    meta = meta[['CC','REV','NCR_RAI','STATUS']]
    meta.fillna('-', inplace=True)
    meta = meta[meta['CC'] != '-']
    meta = meta[meta['STATUS'] == 'Publicado']
    meta = meta.sort_values(['CC','REV','NCR_RAI','STATUS'], ascending=False)

    old_name = ['Rev  CC  ', 'Numero Caderno','Status']
    new_name = ['REV_CC','NUMERO_CADERNO','STATUS']

    for i in range(len(old_name)):
        print(old_name[i], new_name[i])
        export.rename(columns={old_name[i]:new_name[i]}, inplace=True)

    export = export[export['STATUS'] == 'Publicado']
    export = export[['NUMERO_CADERNO','REV_CC','STATUS']]
    export = export.sort_values(['NUMERO_CADERNO','REV_CC','STATUS'], ascending=False)

    m = meta.groupby(['CC','REV','NCR_RAI','STATUS']).count().sort_values(['CC','REV'], ascending=False)

    test = ''
    cc_base = []
    for a in m.index:
        if test != a[0]:
            cc_base.append([a[0], a[1], a[2], a[3]])
            test = a[0]

    df = pd.DataFrame(data=cc_base, columns=['CC', 'REV','NCR_RAI','STATUS'])
    df.rename(columns={'NCR_RAI': 'RAI'}, inplace=True)
    df = df.fillna('-')
    df['STATUS_LIBERA'] = '-'

    lista = []
    for a in range(len(df)):
        x = df['RAI'][a]
        y = x.split('/')
        if len(y) > 1:
            for b in y:
                lista.append([df['CC'][a], b, df['STATUS'][a], df['STATUS_LIBERA'][a]])
        else:
            lista.append([df['CC'][a], x, df['STATUS'][a], df['STATUS_LIBERA'][a]])

    new_df = pd.DataFrame(data=lista, columns=['CC', 'NCR_RAI', 'STATUS', 'STATUS_LIBERA'])
    new_df.sort_values(by=['NCR_RAI'], inplace=True)

    for i in range(len(new_df)):
        a = new_df['NCR_RAI'].loc[i]
        if a != '-':
            b = new_df[new_df['NCR_RAI'] == new_df['NCR_RAI'].loc[i]]
            e = []
            for c in b['STATUS']:
                if c == 'Publicado':
                    e.append(c)
                if len(e) == len(b['STATUS']):
                    new_df['STATUS_LIBERA'].loc[i] = 'Todos Cadernos Publicados'

    new_df.sort_values(by=['NCR_RAI'], inplace=True)
    #df2 = RAI[['RAI', 'DISCIPLINA', 'COS', 'STATUS', 'ACAO_DELINEAMENTO']]
    df2 = RAI[['RAI','STATUS']]

    df2 = df2[df2['STATUS'] == 'Em Delineamento | Analisado']

    analize_rai = new_df[new_df['STATUS_LIBERA'] == 'Todos Cadernos Publicados'][['NCR_RAI', 'STATUS_LIBERA']]
    analize_rai = analize_rai[analize_rai['NCR_RAI'] != '']

    cont = 0
    for a in analize_rai.index:
        cont += 1
        analize_rai.rename(index={a: cont}, inplace=True)

    lista = []
    cont = 0
    for a in analize_rai['NCR_RAI']:
        for b in df2['RAI']:
            if a == b:
                cont += 1
                lista.append([b, 'Liberar RAI_NCR'])

    NCR_RAI_LIBERAR = pd.DataFrame(data=lista, columns=['NCR_RAI', 'STATUS'])

    LIBERAR = NCR_RAI_LIBERAR[NCR_RAI_LIBERAR['NCR_RAI'] != '']
    NCR_RAI_Libera = LIBERAR.groupby(['NCR_RAI', 'STATUS']).count()

    if len(NCR_RAI_Libera) == 0:
        print('OPS')
        NCR_RAI = pd.DataFrame(data=[[0,'Vazio']], columns=['NCR_RAI','STATUS'])
        msg_df = 'Não Foram Encontradas RAIs para Deliberação!'
        print([NCR_RAI, msg_df])
        return [NCR_RAI, msg_df]
        

    else:
        NCR_RAI_Libera.to_excel('static/NCR_RAI_LIBERAR.xlsx', 'NCR_RAI_LIBERAR')
        msg_df = 'RAIs Encontradas!'
        print([NCR_RAI_Libera, msg_df])
        return [NCR_RAI_Libera, msg_df]
        














    # cc = pd.read_excel('static/INT_DELNT_CRTL_META_REV.xlsx')
    # RAI = pd.read_excel('static/rai.xlsx')

    # df = cc[['CC', 'NCR_RAI', 'STATUS']]
    # df.rename(columns={'NCR_RAI': 'RAI'}, inplace=True)

    # df = df.fillna('-')

    # df['STATUS_LIBERA'] = '-'

    # lista = []
    # for a in range(len(df)):
    #     x = df['RAI'][a]
    #     y = x.split('/')
    #     if len(y) > 1:
    #         for b in y:
    #             lista.append([df['CC'][a], b, df['STATUS'][a], df['STATUS_LIBERA'][a]])
    #     else:
    #         lista.append([df['CC'][a], x, df['STATUS'][a], df['STATUS_LIBERA'][a]])

    # new_df = pd.DataFrame(data=lista, columns=['CC', 'NCR_RAI', 'STATUS', 'STATUS_LIBERA'])
    # new_df.sort_values(by=['NCR_RAI'], inplace=True)

    # for i in range(len(new_df)):
    #     a = new_df['NCR_RAI'].loc[i]
    #     if a != '-':
    #         b = new_df[new_df['NCR_RAI'] == new_df['NCR_RAI'].loc[i]]
    #         e = []
    #         for c in b['STATUS']:
    #             if c == 'Publicado':
    #                 e.append(c)
    #             if len(e) == len(b['STATUS']):
    #                 new_df['STATUS_LIBERA'].loc[i] = 'Todos Cadernos Publicados'

    # new_df.sort_values(by=['NCR_RAI'], inplace=True)
    # df2 = RAI[['RAI', 'DISCIPLINA', 'COS', 'STATUS', 'ACAO_DELINEAMENTO']]

    # df2 = df2[df2['STATUS'] == 'Em Delineamento | Analisado']

    # analize_rai = new_df[new_df['STATUS_LIBERA'] == 'Todos Cadernos Publicados'][['NCR_RAI', 'STATUS_LIBERA']]
    # analize_rai = analize_rai[analize_rai['NCR_RAI'] != '']

    # cont = 0
    # for a in analize_rai.index:
    #     cont += 1
    #     analize_rai.rename(index={a: cont}, inplace=True)

    # lista = []
    # cont = 0
    # for a in analize_rai['NCR_RAI']:
    #     for b in df2['RAI']:
    #         if a == b:
    #             cont += 1
    #             lista.append([b, 'Liberar RAI_NCR'])

    # NCR_RAI_LIBERAR = pd.DataFrame(data=lista, columns=['NCR_RAI', 'STATUS'])

    # LIBERAR = NCR_RAI_LIBERAR[NCR_RAI_LIBERAR['NCR_RAI'] != '']
    # NCR_RAI_Libera = LIBERAR.groupby(['NCR_RAI', 'STATUS']).count()

    # if len(NCR_RAI_Libera) == 0:
    #     print('OPS')
    #     NCR_RAI = pd.DataFrame(data=[[0,'Vazio']],columns=['NCR_RAI','STATUS'])
    #     msg_df = 'Não Foram Encontradas RAIs para Deliberação!'
    #     return [NCR_RAI, msg_df]

    # else:
    #     NCR_RAI_Libera.to_excel('static/NCR_RAI_LIBERAR.xlsx', 'NCR_RAI_LIBERAR')
    #     msg_df = 'RAIs Encontradas!'
    #     return [NCR_RAI_Libera, msg_df]



#
# def db_query2():
#   return db.update({"nome": "Vitor"}, Ft.senha == 'Eller')
#
# def db_query3():
#   return db.remove(Ft.senha == 'Ell')

