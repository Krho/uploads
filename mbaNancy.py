import mwclient
import pywikibot
from pywikibot import page

import bot_config

commonsPy = pywikibot.Site('commons', 'commons')
wikidata = pywikibot.Site("wikidata", "wikidata")
repo = wikidata.data_repository()
commons = mwclient.Site('commons.wikimedia.org')
commons.login(username=bot_config.USER, password=bot_config.PASS)

""" def importItem(line): """

def importFile():
    """ qid = item.id """
    name = "La Femme Blonde - MBAN.jpg"
    file = open('65-2-76 cop GM.jpg', 'rb')
    qid = 'Q60346305'
    text = "== {{int:filedesc}} ==\n{{Artwork|wikidata="+qid+"|source={{Template:MBA Nancy}}}}\n\n== {{int:license-header}} ==\n{{cc-by-sa-4.0}}"
    commons.upload(file, filename=name, description=text)

def importFolder(folder):
    lines
    files
    for i in range(len(lines)):
        item = importItem(lines[i])
        file = importFile(files[i], item)
        addFile(item, file)

def main():
    importFile()

if __name__ == '__main__':
    main()
