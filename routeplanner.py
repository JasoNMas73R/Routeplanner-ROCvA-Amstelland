import time #zet dit in iedere code waarvan je de prompt wil pauzeren want anders werkt het niet
norm = 0.6 #waittime for de normale prints in de prompt

def directions(query):

    def init_answer():
        print("\n")
        time.sleep(1)

    #print("Komt deze zin altijd boven de input?")
    if (query.lower() == "sacharovlaan"):
        init_answer()
        print("Loop aan de Zetterij naar de bushalte richting Aalsmeer.")
        time.sleep(norm)
        print("Neem bus 357 of 358 (komt afwisselend tijdens werkuren")
        time.sleep(norm)
        print("om de 7 minuten en na 18:00 om de 15 minuten) en stap uit")
        time.sleep(norm)
        print("bij de volgende halte (Sacharovlaan). De gelijknamige tramhalte")
        time.sleep(norm)
        print("voor lijn 25 richting Westwijk en Station Amsterdam Zuid zit")
        time.sleep(norm)
        print("op minder dan 1 minuut lopen van de bushalte. \n")
        time.sleep(norm)
        directions(input(">"))                           
        

    if (query.lower() == "westwijk"):
        print("Bedoelt u de tramhalte of het winkelcentrum?")
        option=input("Toets 1 voor de tramhalte en 2 voor het winkelcentrum. ") #de gebruiker geeft hier een waarde
                                                                                #aan de variabele "option". door de
                                                                                #waarde aan te passen in de prompt
        if (option == "1"):                                                     #kun je verschillende uitkomsten creeren.
            init_answer()
            print("Loop aan de Zetterij naar de bushalte richting Aalsmeer.")
            time.sleep(norm)
            print("Neem bus 357 of 358 (komt afwisselend tijdens werkuren")
            time.sleep(norm)
            print("om de 7 minuten en na 18:00 om de 15 minuten) en stap uit")
            time.sleep(norm)
            print("bij de halte Sacharovlaan. Loop vervolgens aan de Sacharov-")
            time.sleep(norm)            
            print("laan de Ko van Dijklaan in en blijf rechtdoor lopen door")
            time.sleep(norm) 
            print("de Jan Nelissenlaan en Augusta de Witlaan lopen tot U tegen")
            time.sleep(norm) 
            print("de Loethoelilaan komt en sla linksaf. Loop ca. 3 minuten")
            time.sleep(norm)         
            print("rechtdoor en recht voor u kunt u de tramhalte vinden. \n")
            time.sleep(norm)
            #option=None
            directions(input(">"))

        if (option == "2"):
            init_answer()
            print("Loop aan de Zetterij naar de bushalte richting Aalsmeer.")
            time.sleep(norm)
            print("Neem bus 357 of 358 (komt afwisselend tijdens werkuren")
            time.sleep(norm)
            print("om de 7 minuten en na 18:00 om de 15 minuten) en stap uit")
            time.sleep(norm)
            print("bij de halte Westwijkplein. Het winkelcentrum bevindt zich")
            time.sleep(norm)
            print("aan uw linkerkant. \n")
            time.sleep(norm)
            #option=None
            directions(input(">"))

        if (option.lower() == "exit"):
            exit()
        
        #if (option.lower() == "terug"):  #werkt niet zoals ik wil
            #directions(">")

        else:
            print("")
            directions("westwijk")
    

    if (query.lower() == "poortwachter"):
        init_answer()
        print("Loop aan de Zetterij naar de Bovenkerkerweg. Steek over")
        time.sleep(norm)
        print("en volg het fietspad naar rechts. Ga onder het viaduct door")
        time.sleep(norm)
        print("en bij de T-splitsing rechtdoor blijven gaan. Blijf de")
        time.sleep(norm)
        print("Bovenkerkerweg volgen tot aan de onderliggende tramtunnel")
        time.sleep(norm)
        print("en volg de fietsafslag naar links. Aan het eind van de afslag")
        time.sleep(norm)
        print("gaat u links en dan op minder dan 2 minuten lopen vindt u")
        time.sleep(norm)
        print("zowel de straat Poortwachter als de gelijknamige bus- en tram-")
        time.sleep(norm)
        print("halte met bussen naar Uithoorn en Amsterdam en tram 25 naar")
        time.sleep(norm)
        print("Westwijk en Station Amsterdam Zuid. \n")
        time.sleep(norm)
        directions(input(">"))
    

    if (query.lower() == "brink"):
        init_answer()
        print("Voor zowel de tramhalte als de straat moet u vanaf de Zetterij")
        time.sleep(norm)
        print("lopen naar de Bovenkerkerweg. Steek over en volg het fietspad")
        time.sleep(norm)
        print("naar rechts. Ga onder het viaduct door en bij de T-splitsing")
        time.sleep(norm)
        print("rechtdoor blijven gaan. Blijf de Bovenkerkerweg volgen tot aan")
        time.sleep(norm)
        print("de onderliggende tramtunnel en volg de fietsafslag naar links.")
        time.sleep(norm)
        print("Aan het eind van de afslag gaat u links en volgt u het fietspad")
        time.sleep(norm)
        print("tot aan tramhalte Poortwachter. Pak hier de tram richting Station")
        time.sleep(norm)
        print("Amsterdam Zuid (komt elke 10 minuten) en stap uit bij halte Brink.")
        time.sleep(norm)
        print("U kunt ook het fietspad bij Poortwachter blijven volgen door het")
        time.sleep(norm)
        print("park. Links van uw kant vindt u ook het winkelcentrum Middenhoven. \n")
        time.sleep(norm)
        directions(input(">"))
    

    if (query.lower() == "winkelcentrum middenhoven"):
        init_answer()
        print("Loop vanaf de Zetterij naar de Bovenkerkerweg. Steek over en volg het")
        time.sleep(norm)
        print("fietspad naar rechts. Ga onder het viaduct door en bij de T-splitsing")
        time.sleep(norm)
        print("rechtdoor blijven gaan. Blijf de Bovenkerkerweg volgen tot aan de")
        time.sleep(norm)
        print("onderliggende tramtunnel en volg de fietsafslag naar links. Aan het")
        time.sleep(norm)
        print("eind van de afslag gaat u links en volgt u het fietspad tot de tram-")
        time.sleep(norm)
        print("halte Poortwachter. Pak hier de tram richting Station Amsterdam Zuid")
        time.sleep(norm)
        print("(komt elke 10 minuten) en stap uit bij halte Brink. Links van uw kant")
        time.sleep(norm)
        print("ziet u de hoofdingang van het winkelcentrum. \n")
        time.sleep(norm)
        directions(input(">"))


    if (query.lower() == "schiphol"):
        print("Wilt u naar het vliegveld/Schiphol Plaza of een bestemming rondom Schiphol zelf?")
        option=input("Toets 1 voor het vliegveld/Schiphol Plaza en 2 voor elders. ")
        
        
        if (option == "1"):
            init_answer()
            print("Loop aan de Zetterij naar de Bovenkerkerweg. Steek over en ga naar")
            time.sleep(norm)
            print("de linksgelegen bushalte richting het Stadshart. Pak bus 357 of 358")
            time.sleep(norm)
            print("(komt afwisselend tijdens werkuren om de 7 minuten en na 18:00 om")
            time.sleep(norm)
            print("de 15 minuten) en stap uit bij halte Amstelveen Busstation. Neem bij")
            time.sleep(norm)
            print("halte F bus 300 naar Station Haarlem via Schiphol (komt van 6 uur 's")
            time.sleep(norm)
            print("ochtends tot 12 uur's nachts iedere 8 minuten) en stap uit bij halte")
            time.sleep(norm)
            print("Schiphol Airport/Plaza. Boven het winkelcentrum bevindt zich vertrek-")
            time.sleep(norm)
            print("hallen 2 en 3 en achter het winkelcentrum zijn de aankomsthallen. \n")
            time.sleep(norm)
            directions(input(">"))        
            #option=None


        if (option == "2"):         
            init_answer()
            print("Loop aan de Zetterij naar de Bovenkerkerweg. Steek over en ga naar")
            time.sleep(norm)
            print("de linksgelegen bushalte richting het Stadshart. Pak bus 357 of 358")
            time.sleep(norm)
            print("(komt afwisselend tijdens werkuren om de 7 minuten en na 18:00 om")
            time.sleep(norm)
            print("de 15 minuten) en stap uit bij halte Amstelveen Busstation. Bij halte")
            time.sleep(norm)
            print("F moet u overstappen op bus 300 richting Station Haarlem via Schiphol")
            time.sleep(norm)
            print("(komt van 6 uur 's ochtends tot 12 uur 's nachts iedere 8 minuten). Voor")
            time.sleep(norm)
            print("bestemmingen in of rondom Schiphol wordt aangeraden om uit te stappen")
            time.sleep(norm)
            print("bij Schiphol Knooppunt Noord. Hier vertrekken bussen naar diverse")
            time.sleep(norm)
            print("bestemmingen in het gebied, onder andere cirkellijn 180/181 die bij de")
            time.sleep(norm)
            print("meest belangrijke plekken en parkeergelegenheden rondom Schiphol komt. \n")
            time.sleep(norm)            
            directions(input(">"))

        if (option.lower() == "exit"):
            exit()

        else:
            print("")
            directions("schiphol")


    if (query.lower() == "osdorp"):
        init_answer()
        print("Loop aan de Zetterij naar de Bovenkerkerweg. Steek over en ga naar")
        time.sleep(norm)
        print("de linksgelegen bushalte richting het Stadshart en Amsterdam. Pak")
        time.sleep(norm)
        print("bus 357 of 358 (komt afwisselend tijdens werkuren om de 7 minuten en")   #eentje gaat er maar naar Amstelveenseweg
        time.sleep(norm)
        print("na 18:00 om de 15 minuten) en blijf in de bus zitten tot u bij de halte")
        time.sleep(norm)
        print("Amstelveenseweg komt. Stap vervolgens boven de halte over op metro 50")
        time.sleep(norm)
        print("of 51 richting Isolatorweg (komt ong. om de 8 minuten, afwisselend")
        time.sleep(norm)
        print("van elkaar). Stap daarna pas uit bij Station Lelylaan. Zodra u naar")
        time.sleep(norm)
        print("beneden loopt kun u diversen trams vinden die door Osdorp heen gaan.")
        time.sleep(norm)
        print("Als u ergens moet wezen in Osdorp Zuid of West, neem dan tram 1 naar")
        time.sleep(norm)
        print("De Aker (ca. iedere 10 minuten). Pak tram 17 naar Dijkgraafplein voor")
        time.sleep(norm)
        print("Osdorp Midden, het Osdorperplein en Osdorp Oost (overigens ook te")
        time.sleep(norm)
        print("bereiken doordeweeks in de spits met spitstram 27, rijdt iedere 7")
        time.sleep(norm)
        print("minuten van kwart voor 6 tot half 10 's ochtends). \n")
        time.sleep(norm)
        directions(input(">"))


    if (query.lower() == "bloemenveiling aalsmeer"):
        init_answer()
        print("Loop aan de Zetterij naar de bushalte richting Aalsmeer.")
        time.sleep(norm)
        print("Neem bus 357 of 358 (komt afwisselend tijdens werkuren om")
        time.sleep(norm)
        print("de 7 minuten en na 18:00 om de 15 minuten) en stap uit bij")
        time.sleep(norm)
        print("de halte FloraHolland/FloriWorld. Helaas zijn de haltes")
        time.sleep(norm)
        print("rondom de bloemenveiling zelf (FloraHolland Noord, -West en")
        time.sleep(norm)
        print("-Oost) sinds 12 december 2021 opgeheven. De nieuwe halte")
        time.sleep(norm)
        print("FloraHolland Noord zit nu aan de Zwarteweg kan nog steeds")
        time.sleep(norm)
        print("bereikt worden door Maalderij uit te lopen tot aan het tank-")
        time.sleep(norm)
        print("station, daar linksaf slaan en bus 171 pakken bij halte")
        time.sleep(norm)
        print("Maalderij (komt een keer per half uur) in de richting naar")
        time.sleep(norm)
        print("Aalsmeer.")
        time.sleep(norm)
        directions(input(">"))


    if (query.lower() == "floraholland"):
        init_answer()
        print("Loop aan de Zetterij naar de bushalte richting Aalsmeer.")
        time.sleep(norm)
        print("Neem bus 357 of 358 (komt afwisselend tijdens werkuren om")
        time.sleep(norm)
        print("de 7 minuten en na 18:00 om de 15 minuten) en stap uit bij")
        time.sleep(norm)
        print("de halte FloraHolland/FloriWorld. Helaas zijn de haltes")
        time.sleep(norm)
        print("rondom de bloemenveiling zelf (FloraHolland Noord, -West en")
        time.sleep(norm)
        print("-Oost) sinds 12 december 2021 opgeheven. De nieuwe halte")
        time.sleep(norm)
        print("FloraHolland Noord zit nu aan de Zwarteweg kan nog steeds")
        time.sleep(norm)
        print("bereikt worden door Maalderij uit te lopen tot aan het tank-")
        time.sleep(norm)
        print("station, daar linksaf slaan en bus 171 pakken bij halte")
        time.sleep(norm)
        print("Maalderij (komt een keer per half uur) in de richting naar")
        time.sleep(norm)
        print("Aalsmeer.")
        time.sleep(norm)
        directions(input(">"))


    if (query.lower() == "gondel"):
        init_answer()
        print("Helaas is er na de ombouwing van sneltramlijn naar reguliere tramlijn")
        time.sleep(norm)
        print("geen vervangende tramhalte gekomen voor het kantoorgebouw De Gondel.")
        time.sleep(norm)
        print("Gelukkig kan het met een paar extra stappen nog wel bereikt worden.")
        time.sleep(norm)
        print("Loop vanaf de Zetterij naar de Bovenkerkerweg. Steek over en volg het")
        time.sleep(norm)
        print("fietspad naar rechts. Ga onder het viaduct door en bij de T-splitsing")
        time.sleep(norm)
        print("rechtdoor blijven gaan. Blijf de Bovenkerkerweg volgen tot aan de")
        time.sleep(norm)
        print("onderliggende tramtunnel en volg de fietsafslag naar links. Aan het")
        time.sleep(norm)
        print("eind van de afslag gaat u links en volgt u het fietspad tot de tram-")
        time.sleep(norm)
        print("halte Poortwachter. Pak hier de tram richting Station Amsterdam Zuid")
        time.sleep(norm)
        print("(komt elke 10 minuten) en stap uit bij halte Brink. Rechts van uw kant")
        time.sleep(norm)
        print("ziet u de bushalte Middenhoven/Brink. Stap daar op bus 174 richting")
        time.sleep(norm)
        print("Amstelveen KLM Hoofdkantoor en stap vervolgens een paar haltes later")
        time.sleep(norm)
        print("uit bij halte Logger. Steek onderdoor het viaduct de weg over en aan uw")
        time.sleep(norm)
        print("rechterkant ziet u kantoorgebouw De Gondel. \n")
        directions(input(">"))


    if (query.lower() == "de gondel"):
        init_answer()
        print("Helaas is er na de ombouwing van sneltramlijn naar reguliere tramlijn")
        time.sleep(norm)
        print("geen vervangende tramhalte gekomen voor het kantoorgebouw De Gondel.")
        time.sleep(norm)
        print("Gelukkig kan het met een paar extra stappen nog wel bereikt worden.")
        time.sleep(norm)
        print("Loop vanaf de Zetterij naar de Bovenkerkerweg. Steek over en volg het")
        time.sleep(norm)
        print("fietspad naar rechts. Ga onder het viaduct door en bij de T-splitsing")
        time.sleep(norm)
        print("rechtdoor blijven gaan. Blijf de Bovenkerkerweg volgen tot aan de")
        time.sleep(norm)
        print("onderliggende tramtunnel en volg de fietsafslag naar links. Aan het")
        time.sleep(norm)
        print("eind van de afslag gaat u links en volgt u het fietspad tot de tram-")
        time.sleep(norm)
        print("halte Poortwachter. Pak hier de tram richting Station Amsterdam Zuid")
        time.sleep(norm)
        print("(komt elke 10 minuten) en stap uit bij halte Brink. Rechts van uw kant")
        time.sleep(norm)
        print("ziet u de bushalte Middenhoven/Brink. Stap daar op bus 174 richting")
        time.sleep(norm)
        print("Amstelveen KLM Hoofdkantoor en stap vervolgens een paar haltes later")
        time.sleep(norm)
        print("uit bij halte Logger. Steek onderdoor het viaduct de weg over en aan")
        time.sleep(norm)
        print("uw rechterkant ziet u kantoorgebouw De Gondel. \n")
        directions(input(">"))


    elif (query.lower() == "ver"):
        version()
        directions(input(">"))


    elif (query.lower() == "info"):
        about()
        directions(input(">"))
        
    
    elif (query.lower() == "disclaimer"):
        disclaimer()
        directions(input(">"))


    elif (query.lower() == "help"):
        print("\n")
        welcome()
        print("")
        print("---------------------------------------------------------------------------------------")
        print("")
        time.sleep(2.5)
        help()
        directions(input(">"))
    
    elif (query.lower() == "wis"): #quick and dirty fix, couldn't define cls or own window att
        for x in range(0,24):
            print("\n")
        
        directions(input(">"))


    elif (query.lower() == "changelog"):
        print("\n")
        changelog()
        directions(input(">"))


    elif (query.lower() == "exit"):
        exit()
    
    else:
        print("Deze bestemming of commando is ongeldig.")
        time.sleep(1)
        print("Probeer het opnieuw.") #Typ "help" voor alle mogelijke commando's en bestemmingen.
        directions(input(">"))



        
def welcome():
    print("Welkom bij de reishulp voor mensen van het ROCvA Amstelland.", no_dot)
    time.sleep(1)
    print("---------------------------------------------------------------------------------------")
    print("Voer hieronder uw bestemming in en beantwoord eventuele opties met de cijfertoetsen.")
    time.sleep(norm)
    print("Het reisadvies is berekend vanaf de school zelf (Maalderij 35).")
    print("""U kunt op ieder moment in de prompt "exit" typen om te stoppen.""")
    time.sleep(norm)
    print("""Lees de disclaimer en/of informatie met de commando's "disclaimer" """)
    print("""en "info". Voor verdere documentatie van de functies, typ "help".""")
    

def disclaimer():
    time.sleep(1)
    print("Disclaimer: de reisadviezen zijn gebasseerd op doordeweekse tijden")
    print("(dienstregelingen in de werkweek). Dit programma let niet op de")
    time.sleep(0.8)
    print("situatie tijdens de weekenden en feestdagen. Raadpleeg hiervoor meer")
    print("actuelere services zoals de die van de betreffende vervoerder")
    time.sleep(norm)
    print("of 9292 via 0900-9292 (€0,90 p/m max. €18,-), de app of de website. \n")



no = "v1.1"
no_dot = "v1.1."                                            #quick and dirty fix
ver_dmy = "donderdag 27 januari 2022"                       #omdat ik het ff niet
ver_dmy_dot = "donderdag 27 januari 2022."                  #anders kon doen
copyright = "(c) 2022? Alle rechten voorbehouden."
cr_short = "(c) 2022?"



def version():
    time.sleep(1.5)
    print("Reisplanner ROCvA Amstelland", no)
    print("Bedacht en geprogrammeerd door Jason Boon.")
    print(copyright)
    print("")
    time.sleep(norm)


def about():
    time.sleep(1.5)
    print("Deze applicatie is bedacht en geprogrammeerd door Jason Boon.")
    time.sleep(2)
    print("Met dank aan diverse leraren van het ROCvA Amstelland en online")
    time.sleep(1)
    print("research voor het helpen coderen aan dit project/eindopdracht.")
    time.sleep(1)
    print("Geïnspireerd en gebaseerd op mijn vele reizen in het OV.")
    time.sleep(1)
    print("Studenten OV FTW")
    print("")
    time.sleep(2)
    print(no, "voltooid op", ver_dmy_dot)
    time.sleep(1)
    print(copyright)
    time.sleep(1)
    print("Ik ben niet verantwoordelijk voor het kwijtraken van de weg,")
    time.sleep(1)
    print("je paraplu, je baan of mentale gezondheid door het gebruik van")
    time.sleep(1)
    print("dit programma. Prutselen aan de code op jouw eigen risico enzo. \n")


def help():
    print("Lijst met commando's:")
    time.sleep(1)
    print("""<bestemming> - Geeft reisadvies naar de betreffende bestemming""")
    print(""""changelog"  - Geeft het veranderingslogboek weer""")
    time.sleep(1)
    print(""""disclaimer" - Laat de disclaimer zien over dit programma""")
    print(""""exit"       - Stopt het programma (werkt op ieder moment)""")
    time.sleep(1)
    print(""""help"       - Toont deze lijst""")
    print(""""info"       - Meer informatie over dit project""")
    time.sleep(1)
    print(""""ver"        - Laat snel zien welke versie van het programma je gebruikt""")
    print(""""wis"        - Schoont 25 regels op \n""")


def changelog():
    time.sleep(3.5)
    print("Changelog (veranderingslogboek):")
    print("---------------------------------------------------------------------------------------")
    time.sleep(norm)    
    print("v0.8 voltooid op maandag 24 januari 2022.")
    time.sleep(norm)
    print("    -Start van de opdracht/project")
    time.sleep(norm)
    print("    -Code getest en mogelijkheden bekeken")
    time.sleep(norm)
    print("")
    time.sleep(norm)
    print("v1.0 voltooid op woensdag 26 januari 2022.")
    time.sleep(norm)
    print("    -Eerste werkende versie van het programma")
    time.sleep(norm)
    print("    -De eerste bestemmingen toegevoegd:")
    time.sleep(norm)
    print("        -Sacharovlaan")
    time.sleep(norm)
    print("        -Westwijk en winkelcentrum")
    time.sleep(norm)
    print("        -Poortwachter")
    time.sleep(norm)
    print("        -Brink en winkelcentrum")
    time.sleep(norm)
    print("        -Schiphol en omstreken")
    time.sleep(norm)
    print("")
    time.sleep(norm)
    print("v1.1 voltooid op donderdag 27 januari 2022.")
    time.sleep(norm)
    print("    -Programma opgeschoond en routines gecreëerd")
    time.sleep(norm)
    print("""    -"help" commando toegevoegd om alle gedocumeteerde""")
    time.sleep(norm)
    print("     commando's en hun functies te laten zien")
    time.sleep(norm)
    print("    -Bestemmingen toegevoegd:")
    time.sleep(norm)
    print("        -Osdorp")
    time.sleep(norm)
    print("        -De Gondel")
    time.sleep(norm)
    print("        -Bloemenveiling Aalsmeer/FloraHolland")  #voeg Uilenstede en Stadshart
    time.sleep(norm)                                        #de volgende keer toe
    print("    -500ste regel bereikt op donderdag 27 januari 2022 om 17:10!")
    time.sleep(norm)
    print("")
    time.sleep(norm)
    print("---|  end of changelog  |--- \n")
    time.sleep(3)


welcome() #genereert letterlijk alleen de welkom tekst
directions(input(">")) #wat je hier achter de > invult is de waarde van query