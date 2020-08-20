# Importation des librairies
import requests
from bs4 import BeautifulSoup
import tweepy
from datetime import datetime
from datetime import *
import lxml

# Autentification Twitter
CONSUMER_KEY = '*****************'
CONSUMER_SECRET = '**************************************************'
ACCESS_KEY = '********************************************************'
ACCESS_SECRET = '**********************************'
def Oauth() :
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        return auth
    except Exception as e:
        return None

oauth = Oauth()
api = tweepy.API(oauth)

#Liste des URL à analyser + requete : 

UrlEslCn = ''
UrlVita = 'https://www.hltv.org/team/9565/vitality#tab-matchesBox'
UrlLdlc = 'https://www.hltv.org/team/4674/ldlc#tab-matchesBox'
UrlG2 = 'https://www.hltv.org/team/5995/g2#tab-matchesBox'
UrlHere = 'https://www.hltv.org/team/8346/heretics#tab-matchesBox'

#EcnResponse = requests.get(UrlEslCn)
VitaResponse = requests.get(UrlVita)
LdlcResponse = requests.get(UrlLdlc)
G2Response = requests.get(UrlG2)
HereResponse = requests.get(UrlHere)

Yesterday = date.today() - timedelta(days=1)
fyesterday = Yesterday.strftime('%d/%m/%Y')


#Vitality
if VitaResponse.ok :
    VitaSoup = BeautifulSoup(VitaResponse.text, 'lxml')
    VitaContent = VitaSoup.findAll("tr", {"class": "team-row"})

    for tr in VitaContent :
        VitaMatchDate = tr.find("td", {"class": "date-cell"}).text
        VitaOpponent = tr.find("span", {"class": "team-2"})
        VitaOpponent = VitaOpponent.text
        VitaA = tr.find('a')
        VitaMatchLink = 'https://www.hltv.org' + VitaA['href']

        VitaLinkResponse = requests.get(VitaMatchLink)
        VitaLinkSoup = BeautifulSoup(VitaLinkResponse.text, 'lxml')
        VitaCompet = VitaLinkSoup.find("div", {"class": "event text-ellipsis"})
        VitaCompet = VitaCompet.text

        VitaScore = tr.find("div", {"class": "score-cell"}).find("span").text
        VitaOpponentScore = tr.find("div", {"class": "score-cell"}).findAll("span")[2].text


        try :
                VitaMatchDate = datetime.strptime(VitaMatchDate, "%H:%M").strftime("%H:%M")
                TodayTime = date.today()
                FormatedTodayTime = datetime.strftime(TodayTime, "%H:%M")
                if VitaMatchDate > FormatedTodayTime :
                    if VitaOpponent == "Heretics" or "G2" or "LDLC" : 
                        VitaTweet = "🇫🇷 Aujourd'hui derby français! Il oppose @TeamVitality à " + VitaOpponent + " à " + VitaMatchDate + " pour les " + VitaCompet 
                        api.update_status(VitaTweet)
                        print("Tweet posté (Derby vitality) ")
                    else : 
                        VitaTweet = "Aujourd'hui à " + str(VitaMatchDate) + " @TeamVitality joue contre " + VitaOpponent + " pour le compte des " + VitaCompet + " #VForVictory "
                        api.update_status(VitaTweet)
                        print("Tweet posté (Vita) ")

        except ValueError :
            if VitaMatchDate == fyesterday : 
                VitaScore = int(VitaScore)
                VitaOpponentScore = int(VitaOpponentScore)
                if VitaOpponent == "Heretics" or "G2" or "LDLC" : 
                    if VitaScore > VitaOpponentScore : 
                        VitaTweet = "Hier, lors du derby français contre " + VitaOpponent + "c'est @teamVitality qui l'a emporté " + str(VitaScore) + " - " + str(VitaOpponentScore) + " pour le compte des " + VitaCompet + " #VforVictory "
                        api.update_status(VitaTweet)
                    elif VitaScore < VitaOpponentScore : 
                        VitaTweet = "Hier, lors du derby français contre @TeamVitality c'est " + VitaOpponent + " qui l'a emporté " + str(VitaOpponentScore) + " - " + str(VitaScore) + " pour le compte des " + VitaCompet 
                        api.update_status(VitaTweet)
                else : 
                    if VitaScore > VitaOpponentScore : 
                        VitaTweet = "Hier, @TeamVitality a gagné " + str(VitaScore) + " - " + str(VitaOpponentScore) + " contre " + VitaOpponent + " pour le compte des " + VitaCompet 
                        api.update_status(VitaTweet)
                    elif VitaScore < VitaOpponentScore : 
                        VitaTweet = "Hier, @TeamVitality a perdu " + str(VitaScore) + " - " + str(VitaOpponentScore) + " contre " + VitaOpponent + " pour le compte des " + VitaCompet 
                        api.update_status(VitaTweet)
            else : 
                print("-")

#Ldlc
if LdlcResponse.ok :
    LdlcSoup = BeautifulSoup(LdlcResponse.text, 'lxml')
    LdlcContent = LdlcSoup.findAll("tr", {"class": "team-row"})

    for tr in LdlcContent :
        LdlcMatchDate = tr.find("td", {"class": "date-cell"}).text
        LdlcOpponent = tr.find("span", {"class": "team-2"})
        LdlcOpponent = LdlcOpponent.text
        LdlcA = tr.find('a')
        LdlcMatchLink = 'https://www.hltv.org' + LdlcA['href']

        LdlcLinkResponse = requests.get(LdlcMatchLink)
        LdlcLinkSoup = BeautifulSoup(LdlcLinkResponse.text, 'lxml')
        LdlcCompet = LdlcLinkSoup.find("div", {"class": "event text-ellipsis"})
        LdlcCompet = LdlcCompet.text

        LdlcScore = tr.find("div", {"class": "score-cell"}).find("span").text
        LdlcOpponentScore = tr.find("div", {"class": "score-cell"}).findAll("span")[2].text



        try :
                LdlcMatchDate = datetime.strptime(LdlcMatchDate, "%H:%M").strftime("%H:%M")
                TodayTime = date.today()
                FormatedTodayTime = datetime.strftime(TodayTime, "%H:%M")
                if LdlcMatchDate > FormatedTodayTime :
                    LdlcTweet = "Aujourd'hui à " + str(LdlcMatchDate) + " @LDLC_OL joue contre " + LdlcOpponent + " pour le compte des " + LdlcCompet
                    api.update_status(LdlcTweet)
                    print("Tweet posté")



        except ValueError :
            if LdlcMatchDate == fyesterday : 
                LdlcScore = int(LdlcScore)
                LdlcOpponentScore = int(LdlcOpponentScore)
                if LdlcScore > LdlcOpponentScore : 
                    LdlcTweet = "Hier, @LDLC_OL a gagné " + str(LdlcScore) + " - " + str(LdlcOpponentScore) + " contre " + LdlcOpponent + " pour le compte des " + LdlcCompet 
                    api.update_status(LdlcTweet)
                elif LdlcScore < LdlcOpponentScore : 
                    LdlcTweet = "Hier, @LDLC_OL a perdu " + str(LdlcScore) + " - " + str(LdlcOpponentScore) + " contre " + LdlcOpponent + " pour le compte des " + LdlcCompet 
                    api.update_status(LdlcTweet)
            else : 
                print("-")

#G2
if G2Response.ok :
    G2Soup = BeautifulSoup(G2Response.text, 'lxml')
    G2Content = G2Soup.findAll("tr", {"class": "team-row"})

    for tr in G2Content :
        G2MatchDate = tr.find("td", {"class": "date-cell"}).text
        G2Opponent = tr.find("span", {"class": "team-2"})
        G2Opponent = G2Opponent.text
        G2A = tr.find('a')
        G2MatchLink = 'https://www.hltv.org' + G2A['href']

        G2LinkResponse = requests.get(G2MatchLink)
        G2LinkSoup = BeautifulSoup(G2LinkResponse.text, 'lxml')
        G2Compet = G2LinkSoup.find("div", {"class": "event text-ellipsis"})
        G2Compet = G2Compet.text

         
        G2Score = tr.find("div", {"class": "score-cell"}).find("span").text
        G2OpponentScore = tr.find("div", {"class": "score-cell"}).findAll("span")[2].text
        

        try :
                G2MatchDate = datetime.strptime(G2MatchDate, "%H:%M").strftime("%H:%M")
                TodayTime = date.today()
                FormatedTodayTime = datetime.strftime(TodayTime, "%H:%M")

                if G2MatchDate > FormatedTodayTime :
                    if G2Opponent == "LDLC" or "Heretics" : 
                         G2Tweet = "🇫🇷 Aujourd'hui derby français! Il oppose @G2Esports à " + G2Opponent + " à " + G2MatchDate + " pour les " + G2Compet 
                         api.update_status(G2Tweet)
                         print("Tweet posté (Derby G2) ")
                    else : 
                        G2Tweet = "Aujourd'hui à " + str(G2MatchDate) + " @G2esports joue contre " + G2Opponent + " pour le compte des " + G2Compet + " #G2ARMY "
                        api.update_status(G2Tweet)
                        print("Tweet posté (G2) ")
        except ValueError :
            Yesterday = date.today() - timedelta(days=1)
            fyesterday = Yesterday.strftime('%d/%m/%Y')
            
                
            if G2MatchDate == fyesterday : 
                G2Score = int(G2Score)
                G2OpponentScore = int(G2OpponentScore)
                if G2Opponent == "LDLC" or "Heretics" :
                    if G2Score > G2OpponentScore : 
                        G2Tweet = "Hier, lors du derby français contre " + G2Opponent + "c'est @G2esports qui l'a emporté " + str(G2Score) + " - " + str(G2OpponentScore) + " pour le compte des " + G2Compet + " #G2ARMY "
                        api.update_status(G2Tweet)
                    elif G2Score < G2OpponentScore : 
                        G2Tweet = "Hier, lors du derby français contre @G2Esports c'est " + G2Opponent + " qui l'a emporté " + str(G2OpponentScore) + " - " + str(G2Score) + " pour le compte des " + G2Compet 
                        api.update_status(G2Tweet)
                else : 
                    if G2Score > G2OpponentScore : 
                        G2Tweet = "Hier, @G2esports a gagné " + str(G2Score) + " - " + str(G2OpponentScore) + " contre " + G2Opponent + " pour le compte des " + G2Compet + " #G2ARMY "
                        api.update_status(G2Tweet)
                    elif G2Score < G2OpponentScore : 
                        G2Tweet = "Hier, @G2esports a perdu " + str(G2Score) + " - " + str(G2OpponentScore) + " contre " + G2Opponent + " pour le compte des " + G2Compet + " #G2ARMY "
                        api.update_status(G2Tweet)
            else : 
                print("-")



#Heretics
if HereResponse.ok :
    HereSoup = BeautifulSoup(HereResponse.text, 'lxml')
    HereContent = HereSoup.findAll("tr", {"class": "team-row"})

    for tr in HereContent :
        HereMatchDate = tr.find("td", {"class": "date-cell"}).text
        HereOpponent = tr.find("span", {"class": "team-2"})
        HereOpponent = HereOpponent.text
        HereA = tr.find('a')
        HereMatchLink = 'https://www.hltv.org' + HereA['href']

        HereLinkResponse = requests.get(HereMatchLink)
        HereLinkSoup = BeautifulSoup(HereLinkResponse.text, 'lxml')
        HereCompet = HereLinkSoup.find("div", {"class": "event text-ellipsis"})
        HereCompet = HereCompet.text

        HereScore = tr.find("div", {"class": "score-cell"}).find("span").text
        HereOpponentScore = tr.find("div", {"class": "score-cell"}).findAll("span")[2].text



        try :
                HereMatchDate = datetime.strptime(HereMatchDate, "%H:%M").strftime("%H:%M")
                TodayTime = date.today()
                FormatedTodayTime = datetime.strftime(TodayTime, "%H:%M")

                if HereMatchDate > FormatedTodayTime :
                    if HereOpponent == "LDLC" : 
                        HereTweet = "🇫🇷 Aujourd'hui derby français! Il oppose @TeamHeretics à " + HereOpponent + " à " + HereMatchDate + " pour les " + HereCompet 
                        api.update_status(HereTweet)
                        print("Tweet posté (Derby Heretics) ")
                    else : 
                        HereTweet = "Aujourd'hui à " + str(HereMatchDate) + " @TeamHeretics joue contre " + HereOpponent + " pour le compte des " + HereCompet
                        api.update_status(HereTweet)
                        print("Tweet posté (Heretics) ")



        except ValueError :
            if HereMatchDate == fyesterday : 
                HereScore = int(HereScore)
                HereOpponentScore = int(HereOpponentScore)
                if HereOpponent == "LDLC" : 
                    if G2Score > G2OpponentScore : 
                        HereTweet = "Hier, lors du derby français les opposant à " + HereOpponent + "c'est @TeamHeretics qui l'a emporté " + str(HereScore) + " - " + str(HereOpponentScore) + " pour le compte des " + HereCompet 
                        api.update_status(HereTweet)
                    elif G2Score < G2OpponentScore : 
                        HerTweet = "Hier, lors du derby français les opposant à @TeamHeretics c'est " + HereOpponent + " qui l'a emporté " + str(HereOpponentScore) + " - " + str(HereScore) + " pour le compte des " + HereCompet 
                        api.update_status(HereTweet)

                else : 
                    if HereScore > HereOpponentScore : 
                        HereTweet = "Hier, @TeamHeretics a gagné " + str(HereScore) + " - " + str(HereOpponentScore) + " contre " + HereOpponent + " pour le compte des " + HereCompet 
                        api.update_status(HereTweet)
                    elif HereScore < HereOpponentScore : 
                        HereTweet = "Hier, @TeamHeretics a perdu " + str(HereScore) + " - " + str(HereOpponentScore) + " contre " + HereOpponent + " pour le compte des " + HereCompet 
                        api.update_status(HereTweet)
            else : 
                print("-")
