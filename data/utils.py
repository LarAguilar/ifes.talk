from csv import DictReader


def obter_relacao_campus_link():
    with open('data/relacao-campus-site.csv', encoding='utf-8') as file:
        relacao_campus_site = list()
        reader = DictReader(file)

        for line in reader:
            campus = dict()

            campus['nome'] = line['campus']
            campus['site'] = line['link']

            relacao_campus_site.append(campus)

        return relacao_campus_site


def obter_campus_pelo_nome(nome_do_campus, lista_de_campus):
    for campus in lista_de_campus:
        if campus['nome'] == nome_do_campus:
            return campus
