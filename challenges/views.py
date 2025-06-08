from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

month_challenges={
    "january":"This is January",
    "february":"This is February",
    "march":"This is March",
    "april":"This is April",
    "may":"This is May",
    "june":"This is June",
    "july":"This is July",
    "august":"This is August",
    "september":"This is September",
    "october":"This is October",
    "november":"This is November",
    "december":"This is December"
}

def monthly_challenge_by_number(request,month):
  months=list(month_challenges.keys() )  
  if (month > len(months) or month < 1):
    return HttpResponseNotFound("This month is not supported")
  redirect_month=months[month-1]
  # Using reverse to get the URL for the month
  redirect_month_url = reverse("month-challenge",args=[redirect_month])
  
  return HttpResponseRedirect(redirect_month_url)
  
def monthly_challenge(request,month):
    try:
      challenge_text = month_challenges[month]

      return render(request,"challenges/challenge.html",{
        "text":challenge_text,
        })
      
    except KeyError:
        return HttpResponseNotFound("This month is not supported")
  