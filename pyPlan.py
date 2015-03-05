# 20/02/2015 par XuanShine


from utils import *
bépo = """
Doriane
		Doriane, lun. 09/02/15 12:15 – 13:00: Oui 		Doriane, mar. 10/02/15 11:30 – 12:15: Oui 				Doriane, mer. 11/02/15 12:15 – 13:00: Oui 					Doriane, ven. 13/02/15 11:30 – 12:15: Oui 	Doriane, ven. 13/02/15 12:15 – 13:00: Oui 			Doriane, lun. 16/02/15 12:15 – 13:00: Oui 								Doriane, jeu. 19/02/15 11:30 – 12:15: Oui 		
Tat
		Tat, lun. 09/02/15 12:15 – 13:00: Oui 	Tat, lun. 09/02/15 13:00 – 13:30: Oui 		Tat, mar. 10/02/15 12:15 – 13:00: Oui 	Tat, mar. 10/02/15 13:00 – 13:30: Oui 		Tat, mer. 11/02/15 12:15 – 13:00: Oui 			Tat, jeu. 12/02/15 12:15 – 13:00: Oui 						Tat, lun. 16/02/15 12:15 – 13:00: Oui 						Tat, mer. 18/02/15 12:15 – 13:00: Oui 			Tat, jeu. 19/02/15 12:15 – 13:00: Oui 	
Charlotte
											Charlotte, jeu. 12/02/15 12:15 – 13:00: Oui 	Charlotte, jeu. 12/02/15 13:00 – 13:30: Oui 					Charlotte, lun. 16/02/15 12:15 – 13:00: Oui 	Charlotte, lun. 16/02/15 13:00 – 13:30: Oui 		Charlotte, mar. 17/02/15 12:15 – 13:00: Oui 	Charlotte, mar. 17/02/15 13:00 – 13:30: Oui 					Charlotte, jeu. 19/02/15 12:15 – 13:00: Oui 	Charlotte, jeu. 19/02/15 13:00 – 13:30: Oui
XuanShine
			XuanShine, lun. 09/02/15 13:00 – 13:30: Oui 			XuanShine, mar. 10/02/15 13:00 – 13:30: Oui 			XuanShine, mer. 11/02/15 13:00 – 13:30: Oui 			XuanShine, jeu. 12/02/15 13:00 – 13:30: Oui 			XuanShine, ven. 13/02/15 13:00 – 13:30: Oui 			XuanShine, lun. 16/02/15 13:00 – 13:30: Oui 			XuanShine, mar. 17/02/15 13:00 – 13:30: Oui 			XuanShine, mer. 18/02/15 13:00 – 13:30: Oui 			XuanShine, jeu. 19/02/15 13:00 – 13:30: Oui
Alexandre
											Alexandre, jeu. 12/02/15 12:15 – 13:00: Oui 	Alexandre, jeu. 12/02/15 13:00 – 13:30: Oui 														Alexandre, jeu. 19/02/15 12:15 – 13:00: Oui 	Alexandre, jeu. 19/02/15 13:00 – 13:30: Oui
Jeremy-J.
	Jeremy-J., lun. 09/02/15 11:30 – 12:15: Oui 	Jeremy-J., lun. 09/02/15 12:15 – 13:00: Oui 			Jeremy-J., mar. 10/02/15 12:15 – 13:00: Oui 		Jeremy-J., mer. 11/02/15 11:30 – 12:15: Oui 	Jeremy-J., mer. 11/02/15 12:15 – 13:00: Oui 		Jeremy-J., jeu. 12/02/15 11:30 – 12:15: Oui 	Jeremy-J., jeu. 12/02/15 12:15 – 13:00: Oui 					Jeremy-J., lun. 16/02/15 11:30 – 12:15: Oui 	Jeremy-J., lun. 16/02/15 12:15 – 13:00: Oui 		Jeremy-J., mar. 17/02/15 11:30 – 12:15: Oui 	Jeremy-J., mar. 17/02/15 12:15 – 13:00: Oui 		Jeremy-J., mer. 18/02/15 11:30 – 12:15: Oui 	Jeremy-J., mer. 18/02/15 12:15 – 13:00: Oui 		Jeremy-J., jeu. 19/02/15 11:30 – 12:15: Oui 	Jeremy-J., jeu. 19/02/15 12:15 – 13:00: Oui 	
Ellena
	Ellena, lun. 09/02/15 11:30 – 12:15: Oui 			Ellena, mar. 10/02/15 11:30 – 12:15: Oui 											Ellena, ven. 13/02/15 13:00 – 13:30: Oui 	Ellena, lun. 16/02/15 11:30 – 12:15: Oui 			Ellena, mar. 17/02/15 11:30 – 12:15: Oui 								
Elodie G
														Elodie G, ven. 13/02/15 12:15 – 13:00: Oui 	Elodie G, ven. 13/02/15 13:00 – 13:30: Oui 												
Thomas G
			Thomas G, lun. 09/02/15 13:00 – 13:30: Oui 	Thomas G, mar. 10/02/15 11:30 – 12:15: Oui 						Thomas G, jeu. 12/02/15 11:30 – 12:15: Oui 								Thomas G, lun. 16/02/15 13:00 – 13:30: Oui 			Thomas G, mar. 17/02/15 13:00 – 13:30: Oui 				Thomas G, jeu. 19/02/15 11:30 – 12:15: Oui 		
Fanny
									Fanny, mer. 11/02/15 13:00 – 13:30: Oui 	Fanny, jeu. 12/02/15 11:30 – 12:15: Oui 					Fanny, ven. 13/02/15 13:00 – 13:30: Oui 												Fanny, jeu. 19/02/15 13:00 – 13:30: Oui
Anouck
		Anouck, lun. 09/02/15 12:15 – 13:00: Oui 	Anouck, lun. 09/02/15 13:00 – 13:30: Oui 		Anouck, mar. 10/02/15 12:15 – 13:00: Oui 																						
Chloé
							Chloé, mer. 11/02/15 11:30 – 12:15: Oui 	Chloé, mer. 11/02/15 12:15 – 13:00: Oui 														Chloé, mer. 18/02/15 11:30 – 12:15: Oui 	Chloé, mer. 18/02/15 12:15 – 13:00: Oui 				
Thomas M
																											
pascaline
				pascaline, mar. 10/02/15 11:30 – 12:15: Oui 	pascaline, mar. 10/02/15 12:15 – 13:00: Oui 	pascaline, mar. 10/02/15 13:00 – 13:30: Oui 	pascaline, mer. 11/02/15 11:30 – 12:15: Oui 		pascaline, mer. 11/02/15 13:00 – 13:30: Oui 				pascaline, ven. 13/02/15 11:30 – 12:15: Oui 	pascaline, ven. 13/02/15 12:15 – 13:00: Oui 													
Florent j
							Florent j, mer. 11/02/15 11:30 – 12:15: Oui 	Florent j, mer. 11/02/15 12:15 – 13:00: Oui 	Florent j, mer. 11/02/15 13:00 – 13:30: Oui 	Florent j, jeu. 12/02/15 11:30 – 12:15: Oui 												Florent j, mer. 18/02/15 11:30 – 12:15: Oui 	Florent j, mer. 18/02/15 12:15 – 13:00: Oui 	Florent j, mer. 18/02/15 13:00 – 13:30: Oui 	Florent j, jeu. 19/02/15 11:30 – 12:15: Oui 		
Pierre-Antoine
										Pierre-Antoine, jeu. 12/02/15 11:30 – 12:15: Oui 	Pierre-Antoine, jeu. 12/02/15 12:15 – 13:00: Oui 	Pierre-Antoine, jeu. 12/02/15 13:00 – 13:30: Oui 		Pierre-Antoine, ven. 13/02/15 12:15 – 13:00: Oui 													
	lun. 09/02/15 11:30 – 12:15 	lun. 09/02/15 12:15 – 13:00 	lun. 09/02/15 13:00 – 13:30 	mar. 10/02/15 11:30 – 12:15 	mar. 10/02/15 12:15 – 13:00 	mar. 10/02/15 13:00 – 13:30 	mer. 11/02/15 11:30 – 12:15 	mer. 11/02/15 12:15 – 13:00 	mer. 11/02/15 13:00 – 13:30 	jeu. 12/02/15 11:30 – 12:15 	jeu. 12/02/15 12:15 – 13:00 	jeu. 12/02/15 13:00 – 13:30 	ven. 13/02/15 11:30 – 12:15 	ven. 13/02/15 12:15 – 13:00 	ven. 13/02/15 13:00 – 13:30 	lun. 16/02/15 11:30 – 12:15 	lun. 16/02/15 12:15 – 13:00 	lun. 16/02/15 13:00 – 13:30 	mar. 17/02/15 11:30 – 12:15 	mar. 17/02/15 12:15 – 13:00 	mar. 17/02/15 13:00 – 13:30 	mer. 18/02/15 11:30 – 12:15 	mer. 18/02/15 12:15 – 13:00 	mer. 18/02/15 13:00 – 13:30 	jeu. 19/02/15 11:30 – 12:15 	jeu. 19/02/15 12:15 – 13:00 	jeu. 19/02/15 13:00 – 13:30
"""
with open("input.txt", "r", encoding="utf-8") as f_in:
    bépo = f_in.read()

# participants: {<Name>: {<Hour>}}
# planner: {<Name>: {<Hour>}}
# calendrier: {<Hour>: {<Name>}}
# clanning: {<Hour>: {<Name>}}

def main():
    participants = str_to_dict(bépo)
    necessary_personn = 2

    calendrier = inverse_dict_of_set(participants)

    # cleaning: looking for (ultra) trivial organisation.
    calendrier, clanning, participants, planner = \
      clean_calendar(calendrier, participants, necessary_personn)

    while search_personn(participants, planner):
        # Trivial
        if search_personn(participants, planner):
            calendrier, clanning, participants, planner = \
              trivial_organisation(calendrier, clanning, participants,
                           planner, necessary_personn)

        # Random
        if search_personn(participants, planner):
            calendrier, clanning, participants, planner = \
              random_organisation(calendrier, clanning, participants,
                          planner, necessary_personn)

    assert inverse_dict_of_set(clanning) == planner
    text = print_clanning(clanning)
    with open("OUTPUT.txt", "w", encoding="utf-8") as f_out:
        f_out.write(text)

if __name__ == "__main__":
    main()
