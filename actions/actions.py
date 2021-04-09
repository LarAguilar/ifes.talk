from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType

#inicio sessao
class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]

        return events

## Função que de acordo com o intent anterior do usuário, pega seu campus, e manda uma resposta junto do link do calendário acadêmico do site do seu campus
class ActionLinkCampus(Action):

    def name(self) -> Text:
        return "action_campus_link_calendario_academico"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ## Resposta se o intent for mudar_curso
        if tracker.get_slot("check_mudar_curso") == True:

                ## Verifica se o campus do usuário já foi informado.
                if tracker.get_slot("campus") == None:

                        ## Preenche variável campus como vazio
                        campus = None
                else:
                        
                        ## Preenche variável campus como o valor do slot campus em string de apenas letras minúsculas
                        campus = str.lower(tracker.get_slot("campus"))

                ## Caso campus não esteja vazio, dependendo de qual campus seja o valor do campus, vai responder sobre a mudança de campus com o link apropriado, sempre retornando também o slot check_mudar_curso como vazio.
                if campus == "alegre":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://alegre.ifes.edu.br/index.php/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "aracruz":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=3.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "barra de são francisco" or campus == "barra de sao francisco":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://saofrancisco.ifes.edu.br/index.php/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "cachoeiro de itapemirim":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=5.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "cariacica":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=6.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "centro-serrano" or campus == "centro serrano":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://centroserrano.ifes.edu.br/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "colatina":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=8.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "guarapari":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://guarapari.ifes.edu.br/index.php/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "ibatiba":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=10.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "itapina":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://itapina.ifes.edu.br/index.php/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "linhares":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://linhares.ifes.edu.br/component/content/article?id=16804.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "montanha":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://montanha.ifes.edu.br/index.php/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "nova venécia" or campus == "nova venecia":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://novavenecia.ifes.edu.br/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "piúma" or campus == "piuma":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://piuma.ifes.edu.br/index.php/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "santa teresa":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=16.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "são mateus" or campus == "sao mateus":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: http://saomateus.ifes.edu.br/noticias/684-calendario-academico-2020.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "serra":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://serra.ifes.edu.br/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "venda nova do imigrante":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=19.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "viana":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=20.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "vila velha":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=21.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]
                elif campus == "vitória" or campus == "vitoria":
                        dispatcher.utter_message("A mudança de curso só poderá ser feita uma única vez e deverá ser requerida dentro do prazo estabelecido no calendário acadêmico do curso, encontrada no link: https://vitoria.ifes.edu.br/calendario-academico.\nA mudança depende da disponibilidade de vagas e da viabilidade didático-pedagógica.\nPara poder mudar de curso, você tem que ter cumprido no mínimo 15% e no máximo 50% da carga horária do curso em que você está matriculado.\nOs documentos necessários para a mudança são o histórico escolar e a ementa das disciplinas que você já cursou.\nCaso a mudança seja aprovada, a confirmação da matrícula no novo curso deverá ser atualizada no prazo máximo de dois dias após a divulgação dos resultados.\nPara mais informações, basta consultar os artigos 52 a 57 do ROD.")
                        return [SlotSet("check_mudar_curso", None)]

                ## Se o campus que o usuário informou tiver sido digitado errado, ele vai ser identificado aqui, e o bot pedirá a ele reescrever
                elif campus != None:
                        dispatcher.utter_message("Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
                        return []

                ## Se o usuário não tiver ainda informado seu campus para o bot, aqui ele vai perguntar de qual ele pertence
                elif campus == None:
                        dispatcher.utter_message("Para acessar essa informação, digite o seu Campus:")
                        return[]

        ## Resposta se o intent for modalidade
        if tracker.get_slot("check_modalidade") == True:

                ## Verifica se o campus do usuário já foi informado.
                if tracker.get_slot("campus") == None:

                        ## Preenche variável campus como vazio
                        campus = None
                else:

                        ## Preenche variável campus como o valor do slot campus em string de apenas letras minúsculas
                        campus = str.lower(tracker.get_slot("campus"))

                ## Caso campus não esteja vazio, dependendo de qual campus seja o valor do campus, vai responder sobre a modalidade com o link apropriado, sempre retornando também o slot check_modalidade como vazio.
                if campus == "alegre":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://alegre.ifes.edu.br/index.php/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "aracruz":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=3.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "barra de são francisco" or campus == "barra de sao francisco":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://saofrancisco.ifes.edu.br/index.php/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "cachoeiro de itapemirim":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=5.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "cariacica":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=6.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "centro-serrano" or campus == "centro serrano":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://centroserrano.ifes.edu.br/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "colatina":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=8.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "guarapari":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://guarapari.ifes.edu.br/index.php/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "ibatiba":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=10.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "itapina":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://itapina.ifes.edu.br/index.php/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "linhares":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://linhares.ifes.edu.br/component/content/article?id=16804.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "montanha":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://montanha.ifes.edu.br/index.php/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "nova venécia" or campus == "nova venecia":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://novavenecia.ifes.edu.br/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "piúma" or campus == "piuma":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://piuma.ifes.edu.br/index.php/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "santa teresa":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=16.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "são mateus" or campus == "sao mateus":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: http://saomateus.ifes.edu.br/noticias/684-calendario-academico-2020.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "serra":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://serra.ifes.edu.br/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "venda nova do imigrante":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=19.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "viana":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=20.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "vila velha":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=21.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]
                elif campus == "vitória" or campus == "vitoria":
                        dispatcher.utter_message("A mudança de modalidade (Presencial/Distância) pode ser requerida uma única vez por curso e deve ser feito dentro do prazo descrito no calendário acadêmico do seu campus, encontrado no link: https://vitoria.ifes.edu.br/calendario-academico.\nA mudança só será executada se houver vagas disponíveis.\nOs documentos necessários para a realização são: o histórico escolar e a ementa do curso.\nPara mais informações, basta consultar os artigos 49, 50 e 51 do ROD.")
                        return [SlotSet("check_modalidade", None)]

               ## Se o campus que o usuário informou tiver sido digitado errado, ele vai ser identificado aqui, e o bot pedirá a ele reescrever
                elif campus != None:
                        dispatcher.utter_message("Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
                        return []

                ## Se o usuário não tiver ainda informado seu campus para o bot, aqui ele vai perguntar de qual ele pertence
                elif campus == None:
                        dispatcher.utter_message("Para acessar essa informação, digite o seu Campus:")
                        return[]

        ## Resposta se o intent for aproveitamento_disciplinas
        if tracker.get_slot("check_aproveitamento_disciplinas") == True:

                ## Verifica se o campus do usuário já foi informado.
                if tracker.get_slot("campus") == None:

                        ## Preenche variável campus como vazio
                        campus = None
                else:

                        ## Preenche variável campus como o valor do slot campus em string de apenas letras minúsculas
                        campus = str.lower(tracker.get_slot("campus"))

                ## Caso campus não esteja vazio, dependendo de qual campus seja o valor do campus, vai responder sobre o aproveitamento de disciplinas com o link apropriado, sempre retornando também o slot check_aproveitamento_disciplinas como vazio.
                if campus == "alegre":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://alegre.ifes.edu.br/index.php/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "aracruz":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=3.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "barra de são francisco" or campus == "barra de sao francisco":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://saofrancisco.ifes.edu.br/index.php/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "cachoeiro de itapemirim":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=5.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "cariacica":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=6.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "centro-serrano" or campus == "centro serrano":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://centroserrano.ifes.edu.br/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "colatina":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=8.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "guarapari":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://guarapari.ifes.edu.br/index.php/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "ibatiba":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=10.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "itapina":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://itapina.ifes.edu.br/index.php/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "linhares":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://linhares.ifes.edu.br/component/content/article?id=16804.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "montanha":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://montanha.ifes.edu.br/index.php/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "nova venécia" or campus == "nova venecia":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://novavenecia.ifes.edu.br/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "piúma" or campus == "piuma":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://piuma.ifes.edu.br/index.php/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "santa teresa":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=16.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "são mateus" or campus == "sao mateus":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: http://saomateus.ifes.edu.br/noticias/684-calendario-academico-2020.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "serra":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://serra.ifes.edu.br/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "venda nova do imigrante":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=19.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "viana":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=20.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "vila velha":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=21.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                elif campus == "vitória" or campus == "vitoria":
                        dispatcher.utter_message("Os estudantes dos cursos técnicos concomitantes, subsequentes e dos cursos técnicos integrados na modalidade EJA podem requerer o aproveitamento de até 50% das matérias do curso, e caso sejam matérias já cursadas no ifes, você pode passar desses 50%.\nO requerimento deverá ser feito via protocolo acadêmico, dentro do prazo que está no calendário acadêmico, encontrado no link: https://vitoria.ifes.edu.br/calendario-academico.\nOs documentos necessários são: o histórico escolar e a ementa das matérias que serão aproveitadas.\nAs matérias precisam ter no mínimo 75% de similaridade nos conteúdos e na carga horária para serem aproveitadas.\nPara mais informações, basta consultar os artigos 42 a 45 do ROD.")
                        return [SlotSet("check_aproveitamento_disciplinas", None)]
                
                ## Se o campus que o usuário informou tiver sido digitado errado, ele vai ser identificado aqui, e o bot pedirá a ele reescrever
                elif campus != None:
                        dispatcher.utter_message("Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
                        return []
                        
                ## Se o usuário não tiver ainda informado seu campus para o bot, aqui ele vai perguntar de qual ele pertence
                elif campus == None:
                        dispatcher.utter_message("Para acessar essa informação, digite o seu Campus:")
                        return[]

        ## Resposta se o intent for trancamento_matricula_sobre
        if tracker.get_slot("check_trancamento_matricula_sobre") == True:
               
                ## Verifica se o campus do usuário já foi informado.
                if tracker.get_slot("campus") == None:

                        ## Preenche variável campus como vazio
                        campus = None
                else:

                        ## Preenche variável campus como o valor do slot campus em string de apenas letras minúsculas
                        campus = str.lower(tracker.get_slot("campus"))

                ## Caso campus não esteja vazio, dependendo de qual campus seja o valor do campus, vai responder sobre o trancamento de matrícula com o link apropriado, sempre retornando também o slot check_trancamento_matricula_sobre como vazio.
                if campus == "alegre":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://alegre.ifes.edu.br/index.php/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "aracruz":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=3.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "barra de são francisco" or campus == "barra de sao francisco":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://saofrancisco.ifes.edu.br/index.php/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "cachoeiro de itapemirim":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=5.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "cariacica":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=6.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "centro-serrano" or campus == "centro serrano":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://centroserrano.ifes.edu.br/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "colatina":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=8.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "guarapari":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://guarapari.ifes.edu.br/index.php/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "ibatiba":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=10.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "itapina":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://itapina.ifes.edu.br/index.php/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "linhares":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://linhares.ifes.edu.br/component/content/article?id=16804.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "montanha":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://montanha.ifes.edu.br/index.php/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "nova venécia" or campus == "nova venecia":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://novavenecia.ifes.edu.br/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "piúma" or campus == "piuma":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://piuma.ifes.edu.br/index.php/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "santa teresa":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=16.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "são mateus" or campus == "sao mateus":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: http://saomateus.ifes.edu.br/noticias/684-calendario-academico-2020.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "serra":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://serra.ifes.edu.br/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "venda nova do imigrante":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=19.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "viana":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=20.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "vila velha":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=21.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                elif campus == "vitória" or campus == "vitoria":
                        dispatcher.utter_message("Primeiramente você precisará verificar no calendário acadêmico as datas reservadas para o trancamento, porque você só poderá pedir o trancamento da sua matrícula dentro do prazo que está no calendário, que poderá ser encontraodo no link: https://vitoria.ifes.edu.br/calendario-academico.\n\nO trancamento da matrícula terá validade de um período letivo, sendo que você só pode efetuar o trancamento da matrícula no máximo 2 vezes, então pode trancar 2 períodos, que podem ser 2 consecutivas ou 2 períodos distantes.\n\nPara alunos do EJA com curso de duração superior a 2 anos, podem haver até 3 trancamentos.\n\nCaso você tenha trancado a sua matrícula, você deverá pedir a reabertura dela no prazo que está no calendário acadêmico, senão ela pode ser cancelada.\n\nPara mais informações, basta consultar os artigos 33 e 34 do ROD.")
                        return [SlotSet("check_trancamento_matricula_sobre", None)]
                
                ## Se o campus que o usuário informou tiver sido digitado errado, ele vai ser identificado aqui, e o bot pedirá a ele reescrever
                elif campus != None:
                        dispatcher.utter_message("Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
                        return []
                        
                ## Se o usuário não tiver ainda informado seu campus para o bot, aqui ele vai perguntar de qual ele pertence
                elif campus == None:
                        dispatcher.utter_message("Para acessar essa informação, digite o seu Campus:")
                        return[]

        ## Resposta se o intent for chamada_suplentes
        if tracker.get_slot("check_chamada_suplentes") == True:
                
                ## Verifica se o campus do usuário já foi informado.
                if tracker.get_slot("campus") == None:

                        ## Preenche variável campus como vazio
                        campus = None
                else:

                        ## Preenche variável campus como o valor do slot campus em string de apenas letras minúsculas
                        campus = str.lower(tracker.get_slot("campus"))

                ## Caso campus não esteja vazio, dependendo de qual campus seja o valor do campus, vai responder sobre a chamada de suplentes com o link apropriado, sempre retornando também o slot check_chamada_suplentes como vazio.
                if campus == "alegre":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://alegre.ifes.edu.br/index.php/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "aracruz":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=3./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "barra de são francisco" or campus == "barra de sao francisco":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://saofrancisco.ifes.edu.br/index.php/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "cachoeiro de itapemirim":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=5./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "cariacica":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=6./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "centro-serrano" or campus == "centro serrano":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://centroserrano.ifes.edu.br/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "colatina":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=8./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "guarapari":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://guarapari.ifes.edu.br/index.php/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "ibatiba":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=10./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "itapina":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://itapina.ifes.edu.br/index.php/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "linhares":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://linhares.ifes.edu.br/component/content/article?id=16804./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "montanha":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://montanha.ifes.edu.br/index.php/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "nova venécia" or campus == "nova venecia":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://novavenecia.ifes.edu.br/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "piúma" or campus == "piuma":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://piuma.ifes.edu.br/index.php/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "santa teresa":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=16./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "são mateus" or campus == "sao mateus":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: http://saomateus.ifes.edu.br/noticias/684-calendario-academico-2020./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "serra":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://serra.ifes.edu.br/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "venda nova do imigrante":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=19./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "viana":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=20./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "vila velha":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=21./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                elif campus == "vitória" or campus == "vitoria":
                        dispatcher.utter_message("A chamada de suplentes ocorre até preencher todas as vagas./nOs suplentes serão chamados em até 4 semanas a partir do primeiro dia de aula, que estão definidos direitinho no calendário acadêmico, encontrado no link: https://vitoria.ifes.edu.br/calendario-academico./nJá para o EAD, o prazo é de 2 semanas após o início das aulas./nPara mais informações, basta consultar o artigo 30 do ROD.")
                        return [SlotSet("check_chamada_suplentes", None)]
                
                ## Se o campus que o usuário informou tiver sido digitado errado, ele vai ser identificado aqui, e o bot pedirá a ele reescrever
                elif campus != None:
                        dispatcher.utter_message("Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
                        return []
                        
                ## Se o usuário não tiver ainda informado seu campus para o bot, aqui ele vai perguntar de qual ele pertence
                elif campus == None:
                        dispatcher.utter_message("Para acessar essa informação, digite o seu Campus:")
                        return[]
        
        ## Resposta se o intent for calendario_academico_localizacao
        if tracker.get_slot("check_calendario_academico_localizacao") == True:
                
                ## Verifica se o campus do usuário já foi informado.
                if tracker.get_slot("campus") == None:

                        ## Preenche variável campus como vazio
                        campus = None
                else:

                        ## Preenche variável campus como o valor do slot campus em string de apenas letras minúsculas
                        campus = str.lower(tracker.get_slot("campus"))

                ## Caso campus não esteja vazio, dependendo de qual campus seja o valor do campus, vai responder sobre a localização do calendário acadêmico com o link apropriado, sempre retornando também o slot check_calendario_academico_localizacao como vazio.
                if campus == "alegre":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://alegre.ifes.edu.br/index.php/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "aracruz":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=3. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "barra de são francisco" or campus == "barra de sao francisco":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://saofrancisco.ifes.edu.br/index.php/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "cachoeiro de itapemirim":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=5. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "cariacica":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=6. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "centro-serrano" or campus == "centro serrano":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://centroserrano.ifes.edu.br/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "colatina":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=8. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "guarapari":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://guarapari.ifes.edu.br/index.php/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "ibatiba":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=10. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "itapina":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://itapina.ifes.edu.br/index.php/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "linhares":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://linhares.ifes.edu.br/component/content/article?id=16804. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "montanha":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://montanha.ifes.edu.br/index.php/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "nova venécia" or campus == "nova venecia":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://novavenecia.ifes.edu.br/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "piúma" or campus == "piuma":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://piuma.ifes.edu.br/index.php/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "santa teresa":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=16. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "são mateus" or campus == "sao mateus":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: http://saomateus.ifes.edu.br/noticias/684-calendario-academico-2020. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "serra":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://serra.ifes.edu.br/calendario-academico. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "venda nova do imigrante":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=19. \nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "viana":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=20.\nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "vila velha":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=21.\nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                elif campus == "vitória" or campus == "vitoria":
                        dispatcher.utter_message("Os calendários acadêmicos estarão publicados no site do IFES do seu campus. O seu pode ser encontrado aqui: https://vitoria.ifes.edu.br/calendario-academico.\nCaso você esteja no celular, ele estará ao final da página no tópico ‘Ifes’.\nE se você estiver no computador, estará na coluna lateral esquerda, é só procurar lá!\nPara mais informações, basta consultar o artigo 22 § 5ºdo ROD.")
                        return [SlotSet("check_calendario_academico_localizacao", None)]
                
                ## Se o campus que o usuário informou tiver sido digitado errado, ele vai ser identificado aqui, e o bot pedirá a ele reescrever
                elif campus != None:
                        dispatcher.utter_message("Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
                        return []
                        
                ## Se o usuário não tiver ainda informado seu campus para o bot, aqui ele vai perguntar de qual ele pertence
                elif campus == None:
                        dispatcher.utter_message("Para acessar essa informação, digite o seu Campus:")
                        return[]

        ## Resposta se o intent for reintegracao_matricula_condicoes
        if tracker.get_slot("check_reintegracao_matricula_condicoes") == True:
                
                ## Verifica se o campus do usuário já foi informado.
                if tracker.get_slot("campus") == None:

                        ## Preenche variável campus como vazio
                        campus = None
                else:

                        ## Preenche variável campus como o valor do slot campus em string de apenas letras minúsculas
                        campus = str.lower(tracker.get_slot("campus"))

                ## Caso campus não esteja vazio, dependendo de qual campus seja o valor do campus, vai responder sobre as condições para a reintegração da matrícula com o link apropriado, sempre retornando também o slot check_reintegracao_matricula_condicoes como vazio.
                if campus == "alegre":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://alegre.ifes.edu.br/index.php/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "aracruz":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=3.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "barra de são francisco" or campus == "barra de sao francisco":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://saofrancisco.ifes.edu.br/index.php/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "cachoeiro de itapemirim":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=5.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "cariacica":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=6.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "centro-serrano" or campus == "centro serrano":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://centroserrano.ifes.edu.br/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "colatina":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=8.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "guarapari":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://guarapari.ifes.edu.br/index.php/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "ibatiba":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=10.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "itapina":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://itapina.ifes.edu.br/index.php/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "linhares":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://linhares.ifes.edu.br/component/content/article?id=16804.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "montanha":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://montanha.ifes.edu.br/index.php/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "nova venécia" or campus == "nova venecia":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://novavenecia.ifes.edu.br/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "piúma" or campus == "piuma":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://piuma.ifes.edu.br/index.php/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "santa teresa":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=16.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "são mateus" or campus == "sao mateus":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: http://saomateus.ifes.edu.br/noticias/684-calendario-academico-2020.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "serra":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://serra.ifes.edu.br/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "venda nova do imigrante":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=19.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "viana":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=20.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "vila velha":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=21.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                elif campus == "vitória" or campus == "vitoria":
                        dispatcher.utter_message("Você pode requerer a reintegração da matrícula se teve a matrícula cancelada por não obter a frequência obrigatória de 75% num curso ou por não realizar a reabertura da matrícula quando esse foi trancado.\nSe for pedir a reintegração da matrícula tem que ser dentro do prazo previsto no calendário acadêmico, que se encontra no link: https://vitoria.ifes.edu.br/calendario-academico.\nO requerimento da reintegração deve ser entrado no Protocolo Acadêmico, CRA do campus, SA do Cefor ou no polo presencial, para serem analisados de acordo com a existência de vagas e alguns critérios de desempate.\nPara mais informações, basta consultar o artigo 37 do ROD.")
                        return [SlotSet("check_reintegracao_matricula_condicoes", None)]
                
                ## Se o campus que o usuário informou tiver sido digitado errado, ele vai ser identificado aqui, e o bot pedirá a ele reescrever
                elif campus != None:
                        dispatcher.utter_message("Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
                        return []
                        
                ## Se o usuário não tiver ainda informado seu campus para o bot, aqui ele vai perguntar de qual ele pertence
                elif campus == None:
                        dispatcher.utter_message("Para acessar essa informação, digite o seu Campus:")
                        return[]
        
        ## Resposta se o intent for reuniao_pedagogica_quantidade
        if tracker.get_slot("check_reuniao_pedagogica_quantidade") == True:
               
                ## Verifica se o campus do usuário já foi informado.
                if tracker.get_slot("campus") == None:

                        ## Preenche variável campus como vazio
                        campus = None
                else:

                        ## Preenche variável campus como o valor do slot campus em string de apenas letras minúsculas
                        campus = str.lower(tracker.get_slot("campus"))

                ## Caso campus não esteja vazio, dependendo de qual campus seja o valor do campus, vai responder sobre a quantidade de reuniões pedagógicas com o link apropriado, sempre retornando também o slot check_reuniao_pedagogica_quantidade como vazio.
                if campus == "alegre":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://alegre.ifes.edu.br/index.php/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "aracruz":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=3.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "barra de são francisco" or campus == "barra de sao francisco":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://saofrancisco.ifes.edu.br/index.php/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "cachoeiro de itapemirim":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=5.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "cariacica":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=6.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "centro-serrano" or campus == "centro serrano":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://centroserrano.ifes.edu.br/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "colatina":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=8.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "guarapari":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://guarapari.ifes.edu.br/index.php/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "ibatiba":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=10.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "itapina":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://itapina.ifes.edu.br/index.php/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "linhares":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://linhares.ifes.edu.br/component/content/article?id=16804.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "montanha":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://montanha.ifes.edu.br/index.php/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "nova venécia" or campus == "nova venecia":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://novavenecia.ifes.edu.br/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "piúma" or campus == "piuma":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://piuma.ifes.edu.br/index.php/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "santa teresa":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=16.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "são mateus" or campus == "sao mateus":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: http://saomateus.ifes.edu.br/noticias/684-calendario-academico-2020.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "serra":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://serra.ifes.edu.br/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "venda nova do imigrante":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=19.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "viana":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?start=20.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "vila velha":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://www.ifes.edu.br/calendario-academico/18875-calendario-academico-2020?showall=&start=21.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                elif campus == "vitória" or campus == "vitoria":
                        dispatcher.utter_message("Considerando cada curso, as reuniões pedagógicas devem estar especificadas no calendário acadêmico. Para visualizar o do seu campus, acesse o link: https://vitoria.ifes.edu.br/calendario-academico.\n\nPara aqueles de regime semestral ou modular, deve ter no mínimo 3 reuniões.\nPara aqueles de regime anual organizados em bimestres ou semestres, deve ter no mínimo 5 reuniões pedagógicas.\nPara aqueles de regime anual organizados em trimestre, deve ter no mínimo 4 reuniões pedagógicas.\nPara aqueles de cursos a distância, deve ter no mínimo 2 reuniões presenciais por período letivo.\nConsidere que a 1ª reunião é a Reunião Pedagógica Inicial, o última é a Final, e os que tiver entre esses são as Intermediárias.\n\nPara mais informações, basta consultar os artigos 98 e 99 do ROD.")
                        return [SlotSet("check_reuniao_pedagogica_quantidade", None)]
                
                ## Se o campus que o usuário informou tiver sido digitado errado, ele vai ser identificado aqui, e o bot pedirá a ele reescrever
                elif campus != None:
                        dispatcher.utter_message("Parece que você escreveu seu campus errado, poderia digitar de novo por favor?")
                        return []
                        
                ## Se o usuário não tiver ainda informado seu campus para o bot, aqui ele vai perguntar de qual ele pertence
                elif campus == None:
                        dispatcher.utter_message("Para acessar essa informação, digite o seu Campus:")
                        return[]

## Funçao para ativar como verdadeiro o slot uncheck_all se nenhum outro slot de check de links de campus estiver ativado
class ActionCheckUncheckAll(Action):

    def name(self) -> Text:
        return "action_uncheck_all"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("check_mudar_curso") == None and tracker.get_slot("check_modalidade") == None and tracker.get_slot("check_aproveitamento_disciplinas") == None and tracker.get_slot("check_trancamento_matricula_sobre") == None and tracker.get_slot("check_chamada_suplentes") == None and tracker.get_slot("check_calendario_academico_localizacao") == None and tracker.get_slot("check_reintegracao_matricula_condicoes") == None and tracker.get_slot("check_reuniao_pedagogica_quantidade") == None:
                return[SlotSet("uncheck_all", True)]

## Funçao para ativar como falso o slot uncheck_uncheck_all      
class ActionUncheckUncheckAll(Action):

    def name(self) -> Text:
        return "action_uncheck_uncheck_all"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("uncheck_all", None)]

## Funçao para ativar como verdadeiro o slot check_mudar_curso
class ActionCheckMudarCurso(Action):

    def name(self) -> Text:
        return "action_check_mudar_curso"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_mudar_curso", True)]

## Funçao para ativar como verdadeiro o slot check_modalidade
class ActionCheckModalidade(Action):

    def name(self) -> Text:
        return "action_check_modalidade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_modalidade", True)]

## Funçao para ativar como verdadeiro o slot check_aproveitamento_disciplinas
class ActionCheckAproveitmaentoDisciplinas(Action):

    def name(self) -> Text:
        return "action_check_aproveitamento_disciplinas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_aproveitamento_disciplinas", True)]

## Funçao para ativar como verdadeiro o slot check_trancamento_matricula_sobre
class ActionCheckTrancamentoMatriculaSobre(Action):

    def name(self) -> Text:
        return "action_check_trancamento_matricula_sobre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_trancamento_matricula_sobre", True)]

## Funçao para ativar como verdadeiro o slot check_chamada_suplentes
class ActionCheckChamadaSuplentes(Action):

    def name(self) -> Text:
        return "action_check_chamada_suplentes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_chamada_suplentes", True)]

## Funçao para ativar como verdadeiro o slot check_calendario_academico_localizacao
class ActionCheckCalendarioAcademicoLocalizacao(Action):

    def name(self) -> Text:
        return "action_check_calendario_academico_localizacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_calendario_academico_localizacao", True)]

## Funçao para ativar como verdadeiro o slot check_reintegracao_matricula_condicoes
class ActionCheckReintegracaoMatriculaCondicoes(Action):

    def name(self) -> Text:
        return "action_check_reintegracao_matricula_condicoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_reintegracao_matricula_condicoes", True)]

## Funçao para ativar como verdadeiro o slot check_reuniao_pedagogica_quantidade
class ActionCheckReuniaoPedagogicaQuantidade(Action):

    def name(self) -> Text:
        return "action_check_reuniao_pedagogica_quantidade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("check_reuniao_pedagogica_quantidade", True)]