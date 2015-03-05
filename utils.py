
from copy import copy
from random import choice
import re

def inverse_dict_of_set(dico):
    new_dict = {}
    for key in dico:
        for value in dico[key]:
            try:
                new_dict[value].add(key)
            except KeyError:
                new_dict[value] = {key}
    return new_dict

def fill_dict_of_couple(dico):
    maxi_0 = max(dico.keys(), key= lambda t: t[0])[0]
    maxi_1 = max(dico.keys(), key= lambda t: t[1])[1]
    miss_tuple = {(x, y)
                  for x in range(maxi_0)
                  for y in range(maxi_1)
                  if (x, y) not in dico}
    dico.update({double: set() for double in miss_tuple})
    return dico

def str_to_dict(string):
    calendrier = {}
    regex = re.compile(r"[^ \n\t]+ ?[^ \n\t]*, [^ \n\t]+. ([0-9]{2}/)"
                     + r"{2}[0-9]{2} [–: 0-9]+")
    matching = regex.search(string)
    while matching:
        (start, end) = matching.span()
        #print(string[start:end], "=")
        (name, text) = string[start:end].split(",")
        (date1, text) = text.split(".")
        text = text.split()
        date2 = text[0]
        hour = "".join(text[1:])
        string = string[end:]
        try:
            calendrier[name].add((date1[1:] + "di " + date2[:2], hour))
        except KeyError:
            calendrier[name] = {(date1[1:] + "di " + date2[:2], hour)}
        matching = regex.search(string)
    return calendrier

def complete_dict_by_empty_set(main_dico, *dicos):
    for dico in dicos:
        for key in dico:
            if key not in main_dico:
                main_dico[key] = set()
    return main_dico

def clean_calendar(calendrier, participants, limit_personn):
    new_calendrier = copy(calendrier)
    planning = {}
    planner = {}
    for date in calendrier:
        nb_personn = len(calendrier[date])
        if nb_personn <= limit_personn:
            set_personn = new_calendrier.pop(date)
            # transfert all from calendrier to planning
            planning[date] = set_personn
            # add a date for each personn in planner
            # and remove in participants
            for personn in set_personn:
                try:
                    planner[personn].add(date)
                except:
                    planner[personn] = {date}
                participants[personn].remove(date)
    planning = complete_dict_by_empty_set(planning, calendrier)
    planner = complete_dict_by_empty_set(planner, participants)
    return new_calendrier, planning, participants, planner

def keys_of_min_len_in_dict(dico, plus_dico={}):
    for key in dico:
        item = dico[key]
        length = len(item)
        try:
            if length < mini:
                mini = length
                set_keys = {key}  # If there is less: create a new set.
            elif length == mini:
                set_keys.add(key)
        except NameError:
            mini = length  # Create mini with the first length of the dict.
            set_keys = {key}
    return set_keys

def search_personn(participants, planner):
    set_names = {}
    for name in planner:
        set_hours = planner[name]
        length = len(set_hours)
        try:
            if length < mini and participants[name]:
                mini = length
                set_keys = {key}  # If there is less: create a new set.
            elif length == mini and participants[name]:
                set_names.add(name)
        except NameError:
            if participants[name]:
                mini = length  # Create mini with the first length of the dict.
                set_names = {name}
    return set_names

def remove_and_add(calendrier, clanning, participants, planner,
                   name, hour, need_personn):
    # Remove.
    participants[name].remove(hour)
    calendrier[hour].remove(name)
    if len(clanning[hour]) < need_personn:
        # Then add.
        try:  # Pas l'un sans l'autre, à vérifier.
            planner[name].add(hour)
            clanning[hour].add(name)
        except KeyError:
            planner[name] = {hour}
            clanning[hour] = {name}
    return calendrier, clanning, participants, planner

def triv_org_2nd_part(calendrier, clanning, participants, planner,
                      set_hours, name, need_personn):
    for hour in set_hours:
        if len(calendrier[hour]) == 1:
            assert {name} == calendrier[hour]
            # Remove.
            participants[name].remove(hour)
            calendrier[hour].remove(name)
            if len(clanning[hour]) < need_personn:
                # Then add.
                try:  # Pas l'un sans l'autre, à vérifier.
                    planner[name].add(hour)
                    clanning[hour].add(name)
                except KeyError:
                    planner[name] = {hour}
                    clanning[hour] = {name}
                break  # Next personn.
    return calendrier, clanning, participants, planner

def trivial_organisation(calendrier, clanning, participants, planner,
                            need_personn):
    for name in search_personn(participants, planner):
        set_hours = copy(participants[name])
        if len(set_hours) == 1:
            (hour,) = set_hours
            calendrier, clanning, participants, planner = \
              remove_and_add(calendrier, clanning, participants, planner,
                             name, hour, need_personn)
        else:  # len(set_hours) > 1, still looking for a trivial solution
            calendrier, clanning, participants, planner = \
              triv_org_2nd_part(calendrier, clanning, participants, planner,
                                set_hours, name, need_personn)
    return calendrier, clanning, participants, planner

def random_organisation(calendrier, clanning, participants, planner,
                        need_personn):
    for name in search_personn(participants, planner):
        add_hour = False
        while not add_hour:
            try:
                hour = participants[name].pop()
                # Remove.
                calendrier[hour].remove(name)
                if len(clanning[hour]) < need_personn:
                    # Then add.
                    try:  # Pas l'un sans l'autre, à vérifier.
                        planner[name].add(hour)
                        clanning[hour].add(name)
                    except KeyError:
                        planner[name] = {hour}
                        clanning[hour] = {name}
                    add_hour = True
            except KeyError:
                add_hour = True
    return calendrier, clanning, participants, planner

def print_clanning(clanning):
    res = ""
    a = [(key, clanning[key]) for key in clanning]
    a.sort(key=lambda e: e[0][0][-2:] + "." + e[0][1][:2])
    for date, names in a:
        res_name = ""
        for name in names:
            res_name = res_name + name + " "
        hour = date[1][:2]
        if hour == "11":
            res += date[0] + "\n - Ouverture: "
        elif hour == "12":
            res += " - Perm: "
        else:
            res += " - Fermeture: "
        res += res_name + "\n"
    return res
