from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from data import utils


class ActionLinkCampus(Action):

    def name(self) -> Text:
        return "action_campus_link_calendario_academico"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        relacao_campus_link = utils.obter_relacao_campus_link()

        # Links campus para a mudança de campus
        if tracker.get_slot("check_mudar_curso") == True:
            nome_do_campus = None if tracker.get_slot("campus") == None else str(tracker.get_slot("campus"))
            nome_do_campus = str(nome_do_campus).lower()

            if nome_do_campus != None:
                campus = utils.obter_campus_pelo_nome(
                    nome_do_campus, relacao_campus_link)

                mensagem_padrao = f"""
                A mudança de curso só poderá ser feita uma única vez e deverá ser requerida 
                dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no
                link: {campus['site']}.
                \nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.
                \nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.
                \nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.
                \nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.
                \nPara mais informações, basta consultar os artigos 52 a 57 do ROD.
                """

                dispatcher.utter_message(mensagem_padrao)
                return [SlotSet("check_mudar_curso", None)]
            elif nome_do_campus == None:
                dispatcher.utter_message(
                    "Para falar sobre o que você pediu com informações completas, poderia me informar seu campus por favor?")
            else:
                dispatcher.utter_message(
                    "Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
            return []

        # Links campus para a mudança de modalidade
        if tracker.get_slot("check_modalidade") == True:
            nome_do_campus = None if tracker.get_slot("campus") == None else str(tracker.get_slot("campus"))
            nome_do_campus = str(nome_do_campus).lower()

            if nome_do_campus != None:
                campus = utils.obter_campus_pelo_nome(
                    nome_do_campus, relacao_campus_link)

                mensagem_padrao = f"""
                A mudança de modalidade (Presencial/Distância) pode ser requerida 
                uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, 
                encontrado no link: {campus['site']}.
                \nA mudança só será executada se houver vagas disponíveis.
                \nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.
                \nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.
                """

                dispatcher.utter_message(mensagem_padrao)
                return [SlotSet("check_modalidade", None)]
            elif nome_do_campus == None:
                dispatcher.utter_message(
                    "Para falar sobre o que você pediu com informações completas, poderia me informar seu campus por favor?")
            else:
                dispatcher.utter_message(
                    "Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
            return []

        # Links campus para o aproveitamento de disciplinas
        if tracker.get_slot("check_aproveitamento_disciplinas") == True:
            nome_do_campus = None if tracker.get_slot("campus") == None else str(tracker.get_slot("campus"))
            nome_do_campus = str(nome_do_campus).lower()

            if nome_do_campus != None:
                campus = utils.obter_campus_pelo_nome(
                    nome_do_campus, relacao_campus_link)

                mensagem_padrao = f"""
                Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer 
                o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, 
                você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, 
                dentro do prazo que está no calendário acadêmico, encontrado no 
                link: {campus['site']}.
                \nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.
                \nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.
                \nPara mais informações, basta consultar os artigos 42 a 45 do ROD.
                """

                dispatcher.utter_message(mensagem_padrao)
                return [SlotSet("check_aproveitamento_disciplinas", None)]
            elif nome_do_campus == None:
                dispatcher.utter_message(
                    "Para falar sobre o que você pediu com informações completas, poderia me informar seu campus por favor?")
            else:
                dispatcher.utter_message(
                    "Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
            return []

        # Links campus para o sobre do trancamento de matrículas
        if tracker.get_slot("check_trancamento_matricula_sobre") == True:
            nome_do_campus = None if tracker.get_slot("campus") == None else str(tracker.get_slot("campus"))
            nome_do_campus = str(nome_do_campus).lower()

            if nome_do_campus != None:
                campus = utils.obter_campus_pelo_nome(
                    nome_do_campus, relacao_campus_link)

                mensagem_padrao = f"""
                Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, 
                porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, 
                que poderá ser encontraodo no link: {campus['site']}.
                \nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.
                """

                dispatcher.utter_message(mensagem_padrao)
                return [SlotSet("check_trancamento_matricula_sobre", None)]
            elif nome_do_campus == None:
                dispatcher.utter_message(
                    "Para falar sobre o que você pediu com informações completas, poderia me informar seu campus por favor?")
            else:
                dispatcher.utter_message(
                    "Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
            return []

        # Links campus para o sobre a chamada de suplentes
        if tracker.get_slot("check_chamada_suplentes") == True:
            nome_do_campus = None if tracker.get_slot("campus") == None else str(tracker.get_slot("campus"))
            nome_do_campus = str(nome_do_campus).lower()

            if nome_do_campus != None:
                campus = utils.obter_campus_pelo_nome(
                    nome_do_campus, relacao_campus_link)

                mensagem_padrao = f"""
                A chamada de suplentes ocorre até preencher todas as vagas.
                \nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, 
                que estão definidos direitinho no calendário acadêmico, encontrado no 
                link: {campus['site']}.
                \nJá para o EAD, o prazo é de 2 semanas após o início das aulas.
                \nPara mais informações, basta consultar o artigo 30 do ROD.
                """

                dispatcher.utter_message(mensagem_padrao)
                return [SlotSet("check_chamada_suplentes", None)]
            elif nome_do_campus == None:
                dispatcher.utter_message(
                    "Para falar sobre o que você pediu com informações completas, poderia me informar seu campus por favor?")
            else:
                dispatcher.utter_message(
                    "Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
            return []

        # Links campus para a localizacão do calendário acadêmico
        if tracker.get_slot("check_calendario_academico_localizacao") == True:
            nome_do_campus = None if tracker.get_slot("campus") == None else str(tracker.get_slot("campus"))
            nome_do_campus = str(nome_do_campus).lower()

            if nome_do_campus != None:
                campus = utils.obter_campus_pelo_nome(
                    nome_do_campus, relacao_campus_link)

                mensagem_padrao = f"""
                Os calendários acadêmicos estarão publicados no site do IFES do seu campus. 
                O seu pode ser encontrado aqui: {campus['site']}. 
                \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.
                \nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!
                \nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.
                """

                dispatcher.utter_message(mensagem_padrao)
                return [SlotSet("check_calendario_academico_localizacao", None)]
            elif nome_do_campus == None:
                dispatcher.utter_message(
                    "Para falar sobre o que você pediu com informações completas, poderia me informar seu campus por favor?")
            else:
                dispatcher.utter_message(
                    "Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
            return []

        # Links campus para as condições da reintegração da matrícula
        if tracker.get_slot("check_reintegracao_matricula_condicoes") == True:
            nome_do_campus = None if tracker.get_slot("campus") == None else str(tracker.get_slot("campus"))
            nome_do_campus = str(nome_do_campus).lower()

            if nome_do_campus != None:
                campus = utils.obter_campus_pelo_nome(
                    nome_do_campus, relacao_campus_link)

                mensagem_padrao = f"""
                Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por 
                não obter a frequência obrigatória de 75% num curso ou por não realizar a 
                reabertura da matrícula quando esse foi trancado.
                \nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, 
                que se encontra no link: {campus['site']}.
                \nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, 
                SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns 
                critérios de desempate.
                \nPara mais informações, basta consultar o artigo 37 do ROD.
                """

                dispatcher.utter_message(mensagem_padrao)
                return [SlotSet("check_reintegracao_matricula_condicoes", None)]
            elif nome_do_campus == None:
                dispatcher.utter_message(
                    "Para falar sobre o que você pediu com informações completas, poderia me informar seu campus por favor?")
            else:
                dispatcher.utter_message(
                    "Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
            return []

        # Links campus para a quantidade de reuniões pedagógicas
        if tracker.get_slot("check_reuniao_pedagogica_quantidade") == True:
            nome_do_campus = None if tracker.get_slot("campus") == None else str(tracker.get_slot("campus"))
            nome_do_campus = str(nome_do_campus).lower()

            if nome_do_campus != None:
                campus = utils.obter_campus_pelo_nome(
                    nome_do_campus, relacao_campus_link)

                mensagem_padrao = f"""
                vConsiderando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. 
                Para visualizar o do seu campus, acesse o 
                link: {campus['site']}.
                \nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.
                \nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 
                5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 
                4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 
                2 reuniões presenciais por período letivo.
                \nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.
                \nPara mais informações, basta consultar os artigos 98 e 99 do ROD.
                """

                dispatcher.utter_message(mensagem_padrao)
                return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
            elif nome_do_campus == None:
                dispatcher.utter_message(
                    "Para falar sobre o que você pediu com informações completas, poderia me informar seu campus por favor?")
            else:
                dispatcher.utter_message(
                    "Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
            return []

# Ativar como verdadeiro slot uncheck_all se nenhum check de links de campus estiver ativado


class ActionCheckUncheckAll(Action):

    def name(self) -> Text:
        return "action_uncheck_all"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("check_mudar_curso") == None and tracker.get_slot("check_modalidade") == None and tracker.get_slot("check_aproveitamento_disciplinas") == None and tracker.get_slot("check_trancamento_matricula_sobre") == None and tracker.get_slot("check_chamada_suplentes") == None and tracker.get_slot("check_calendario_academico_localizacao") == None and tracker.get_slot("check_reintegracao_matricula_condicoes") == None and tracker.get_slot("check_reuniao_pedagogica_quantidade") == None:
            return[SlotSet("uncheck_all", True)]


class ActionUncheckUncheckAll(Action):

    def name(self) -> Text:
        return "action_uncheck_uncheck_all"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("uncheck_all", None)]


class ActionCheckMudarCurso(Action):

    def name(self) -> Text:
        return "action_check_mudar_curso"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_mudar_curso", True)]


class ActionCheckModalidade(Action):

    def name(self) -> Text:
        return "action_check_modalidade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_modalidade", True)]


class ActionCheckAproveitmaentoDisciplinas(Action):

    def name(self) -> Text:
        return "action_check_aproveitamento_disciplinas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_aproveitamento_disciplinas", True)]


class ActionCheckTrancamentoMatriculaSobre(Action):

    def name(self) -> Text:
        return "action_check_trancamento_matricula_sobre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_trancamento_matricula_sobre", True)]


class ActionCheckChamadaSuplentes(Action):

    def name(self) -> Text:
        return "action_check_chamada_suplentes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_chamada_suplentes", True)]


class ActionCheckCalendarioAcademicoLocalizacao(Action):

    def name(self) -> Text:
        return "action_check_calendario_academico_localizacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_calendario_academico_localizacao", True)]


class ActionCheckReintegracaoMatriculaCondicoes(Action):

    def name(self) -> Text:
        return "action_check_reintegracao_matricula_condicoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_reintegracao_matricula_condicoes", True)]


class ActionCheckReuniaoPedagogicaQuantidade(Action):

    def name(self) -> Text:
        return "action_check_reuniao_pedagogica_quantidade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_reuniao_pedagogica_quantidade", True)]
