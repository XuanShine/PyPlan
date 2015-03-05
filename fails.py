def mat_calendrier_dispo(participants):
    """Return a matrice"""
    calendrier = [[set() for i in range(3)] for i in range(3)]
    for personn in participants:
        for horaire in participants[personn]:
            calendrier[horaire[0]][horaire[1]].add(personn)
    return calendrier

def calendrier_dispo(participants):
    """Return a dictionnary"""
    calendrier = {(day, hour): set()
                  for day in range(days)
                  for hour in range(hours)}
    for personn in participants:
        for horaire in participants[personn]:
            try:
                calendrier[horaire].add(personn)
            except KeyError:
                calendrier[horaire] = {personn}
    return calendrier

def search_personn1(participants, planner):
    nb_taches_for_personn = {}
    for personn in participants:
        if participants[personn]:
            try:
                nb = len(planner[personn])
            except KeyError:
                nb = 0
            if not nb_taches_for_personn or \
               nb <= min(nb_taches_for_personn.keys()):
                try:
                    nb_taches_for_personn[nb].add(personn)
                except KeyError:
                    nb_taches_for_personn[nb] = {personn}
    try:
        return nb_taches_for_personn[min(nb_taches_for_personn.keys())]
    except ValueError:
        return None

def trivial_organisation(calendrier, planning, participants, planner,
                         necessary_personn):
    still_trivial = True
    concerns = search_personn(participants, planner)
    while still_trivial and concerns:
        still_trivial = False
        for personn in concerns:
            set_hours = participants[personn]
            if len(set_hours) == 1:
                still_trivial = True
                hour, = set_hours
                try:
                    if len(planning[hour]) < necessary_personn:
                        complet = False
                    else:
                        complet = True
                        # À modifier si remplacant existe.
                        for personn1 in calendrier.pop(hour):
                            participants[personn1].remove(hour)
                except KeyError:
                    complet = False
                    planning[hour] = set()
                if not complet:
                    planning[hour].add(personn)
                    try: calendrier[hour].remove(personn)
                    except: pass
                    participants[personn].remove(hour)
                    try:
                        planner[personn].add(hour)
                    except KeyError:
                        planner[personn] = {hour}
    return calendrier, planning, participants, planner

def trivial_organisation2(calendrier, planning, participants, planner,
                          necessary_personn):
    still_trivial = True
    while still_trivial and search_personn(participants, planner):
        still_trivial = False
        for personn in search_personn(participants, planner):
            set_hours = copy(participants[personn])
            for hour in set_hours:
                if hour not in calendrier:
                    #participants[personn].remove(hour)
                    continue
                if len(calendrier[hour]) == 1:
                    still_trivial = True
                    try:
                        if len(planning[hour]) < necessary_personn:
                            complet = False
                        else:
                            complet = True
                            # À modifier si remplacant existe.
                            calendrier.pop(hour)
                    except KeyError:
                        complet = False
                        planning[hour] = set()
                    if not complet:
                        planning[hour].add(personn)
                        calendrier[hour].remove(personn)
                        participants[personn].remove(hour)
                        try:
                            planner[personn].add(hour)
                        except KeyError:
                            planner[personn] = {hour}
    return calendrier, planning, participants, planner
