from models.langs import LangsModel

list_langs = []
language = LangsModel.get_data()

if bool(language):
	for langu in language:
		list_langs.append(langu['lang_short'])