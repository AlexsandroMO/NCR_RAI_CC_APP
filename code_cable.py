import pandas as pd

def read_cables():
  rev_old = pd.read_excel('static/ANEXO-OLD.xls','Complete Routing')
  rev_new = pd.read_excel('static/ANEXO-NEW.xls','Complete Routing')

  #rev_old= rev_old.head(50)
  #rev_new = rev_new.head(50)

  read = []
  for a in range(0, len(rev_new['COL4'])):
    for b in range(0, len(rev_old['COL4'])):
      if rev_old['COL4'][b] == rev_new['COL4'][a]:
        status = []
        if rev_old['COL3'][b] != rev_new['COL3'][a]:
          status.append('{} = ({} : {})'.format('COL3', rev_old['COL3'][b], rev_new['COL3'][a]))
        if rev_old['COL5'][b] != rev_new['COL5'][a]:
          status.append('{} = ({} : {})'.format('COL5', rev_old['COL5'][b], rev_new['COL5'][a]))
        if rev_old['COL6'][b] != rev_new['COL6'][a]:
          status.append('{} = ({} : {})'.format('COL6', rev_old['COL6'][b], rev_new['COL6'][a]))
        if rev_old['COL7'][b] != rev_new['COL7'][a]:
          status.append('{} = ({} : {})'.format('COL7', rev_old['COL7'][b], rev_new['COL7'][a]))
        if rev_old['COL8'][b] != rev_new['COL8'][a]:
          status.append('{} = ({} : {})'.format('COL8', rev_old['COL8'][b], rev_new['COL8'][a]))
        if rev_old['COL9'][b] != rev_new['COL9'][a]:
          status.append('{} = ({} : {})'.format('COL9', rev_old['COL9'][b], rev_new['COL9'][a]))
        if rev_old['COL10'][b] != rev_new['COL10'][a]:
          status.append('{} = ({} : {})'.format('COL10', rev_old['COL10'][b], rev_new['COL10'][a]))
        if rev_old['COL11'][b] != rev_new['COL11'][a]:
          status.append('{} = ({} : {})'.format('COL11', rev_old['COL11'][b], rev_new['COL11'][a]))
        if rev_old['COL12'][b] != rev_new['COL12'][a]:
          status.append('{} = ({} : {})'.format('COL12', rev_old['COL12'][b], rev_new['COL12'][a]))
        if rev_old['COL13'][b] != rev_new['COL13'][a]:
          status.append('{} = ({} : {})'.format('COL13', rev_old['COL13'][b], rev_new['COL13'][a]))
        if rev_old['COL14'][b] != rev_new['COL14'][a]:
          status.append('{} = ({} : {})'.format('COL14', rev_old['COL14'][b], rev_new['COL14'][a]))
        if rev_old['COL15'][b] != rev_new['COL15'][a]:
          status.append('{} = ({} : {})'.format('COL15', rev_old['COL15'][b], rev_new['COL15'][a]))
        if rev_old['COL16'][b] != rev_new['COL16'][a]:
          status.append('{} = ({} : {})'.format('COL16', rev_old['COL16'][b], rev_new['COL16'][a]))

        if rev_old['COL17'][b] != rev_new['COL17'][a]:
          status.append('{} = ({} : {})'.format('COL17', rev_old['COL17'][b], rev_new['COL17'][a]))
        if rev_old['COL18'][b] != rev_new['COL18'][a]:
          status.append('{} = ({} : {})'.format('COL18', rev_old['COL18'][b], rev_new['COL18'][a]))
        if rev_old['COL19'][b] != rev_new['COL19'][a]:
          status.append('{} = ({} : {})'.format('COL19', rev_old['COL19'][b], rev_new['COL19'][a]))
        if rev_old['COL20'][b] != rev_new['COL20'][a]:
          status.append('{} = ({} : {})'.format('COL20', rev_old['COL20'][b], rev_new['COL20'][a]))
        if rev_old['COL21'][b] != rev_new['COL21'][a]:
          status.append('{} = ({} : {})'.format('COL21', rev_old['COL21'][b], rev_new['COL21'][a]))
        if rev_old['COL22'][b] != rev_new['COL22'][a]:
          status.append('{} = ({} : {})'.format('COL22', rev_old['COL22'][b], rev_new['COL22'][a]))
        if rev_old['COL23'][b] != rev_new['COL23'][a]:
          status.append('{} = ({} : {})'.format('COL23', rev_old['COL23'][b], rev_new['COL23'][a]))
        if rev_old['COL24'][b] != rev_new['COL24'][a]:
          status.append('{} = ({} : {})'.format('COL24', rev_old['COL24'][b], rev_new['COL24'][a]))
        if rev_old['COL25'][b] != rev_new['COL25'][a]:
          status.append('{} = ({} : {})'.format('COL25', rev_old['COL25'][b], rev_new['COL25'][a]))
        if rev_old['COL26'][b] != rev_new['COL26'][a]:
          status.append('{} = ({} : {})'.format('COL26', rev_old['COL26'][b], rev_new['COL26'][a]))
        if rev_old['COL27'][b] != rev_new['COL27'][a]:
          status.append('{} = ({} : {})'.format('COL27', rev_old['COL27'][b], rev_new['COL27'][a]))
        if rev_old['COL28'][b] != rev_new['COL28'][a]:
          status.append('{} = ({} : {})'.format('COL28', rev_old['COL28'][b], rev_new['COL28'][a]))
        if rev_old['COL29'][b] != rev_new['COL29'][a]:
          status.append('{} = ({} : {})'.format('COL29', rev_old['COL29'][b], rev_new['COL29'][a]))
        if rev_old['COL30'][b] != rev_new['COL30'][a]:
          status.append('{} = ({} : {})'.format('COL30', rev_old['COL30'][b], rev_new['COL30'][a]))

        if rev_old['COL57'][b] != rev_new['COL57'][a]:
          status.append('{} = ({} : {})'.format('COL57', rev_old['COL57'][b], rev_new['COL57'][a]))
        if rev_old['COL58'][b] != rev_new['COL58'][a]:
          status.append('{} = ({} : {})'.format('COL58', rev_old['COL58'][b], rev_new['COL58'][a]))

        if rev_old['COL61'][b] != rev_new['COL61'][a]:
          status.append('{} = ({} : {})'.format('COL61', rev_old['COL61'][b], rev_new['COL61'][a]))
        if rev_old['COL62'][b] != rev_new['COL62'][a]:
          status.append('{} = ({} : {})'.format('COL62', rev_old['COL62'][b], rev_new['COL62'][a]))
        if rev_old['COL63'][b] != rev_new['COL63'][a]:
          status.append('{} = ({} : {})'.format('COL63', rev_old['COL63'][b], rev_new['COL63'][a]))
        if rev_old['COL64'][b] != rev_new['COL64'][a]:
          status.append('{} = ({} : {})'.format('COL64', rev_old['COL64'][b], rev_new['COL64'][a]))
        if rev_old['COL65'][b] != rev_new['COL65'][a]:
          status.append('{} = ({} : {})'.format('COL65', rev_old['COL65'][b], rev_new['COL65'][a]))
        if rev_old['COL66'][b] != rev_new['COL66'][a]:
          status.append('{} = ({} : {})'.format('COL66', rev_old['COL66'][b], rev_new['COL66'][a]))
        if rev_old['COL67'][b] != rev_new['COL67'][a]:
          status.append('{} = ({} : {})'.format('COL67', rev_old['COL67'][b], rev_new['COL67'][a]))

        if len(status) > 0:
          read.append([rev_old['COL4'][a], status])
            #print('>>>>>>>', [rev_old['COL4'][a], status])

  return read