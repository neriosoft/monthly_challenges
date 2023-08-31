from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!!!",
    "february":"Walk for at least 20 minutes every day!!!",
    "march": "Learn Django for at least 30 minutes daily!!!",
    "april": "Evaluate yourself before you sleep daily!!!",
    "may": "Get yourself some fruits to eat in the morning",
    "june": "Try send some job proposal thrice a week to potential clients",
    "july": "Do follow up calls to your students on their assignments",
    "august": "Get yourself some new trousers to look takeaway!!!",
    "september": "Ensure your electronics are turned off before going to bed daily!!!",
    "october": "Always check your to-do list before you go out daily!!!",
    "november": "Make new friends to engage at your leisure time daily!!!",
    "december": "Finally you can rest and merry!!!"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("The number is out of range for the intended month!!!")
    
    redirect_month = months[month-1]
    redirect_url = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)

    
def monthly_challenge(request, month):  
    
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month not supported!!!")
    
   

 