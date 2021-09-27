from django.shortcuts import render
import requests
API_KEY='8d23f684b30346e9b902caca1550c665'

# Create your views here.
# def home(request):
#     country=request.GET.get('country')
#     category=request.GET.get('category')
#     if country:
#             url=f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
#             r =requests.get(url)
#             data=r.json()
#             articles=data['articles']
#     else:    
#             url=f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
#             r =requests.get(url)
#             data=r.json()
#             articles=data['articles']
   

#     context={
#         'articles': articles
#     }
#     return render(request,'home.html',context)

def index(request):
     return render(request,'index.html')
    


         
           
            
#  country
def india(request): 
    url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'india.html',context)

def america(request): 
    url=f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'america.html',context)   

def russia(request): 
    url=f'https://newsapi.org/v2/top-headlines?country=ru&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'russia.html',context)        
                
#language


def hindi(request): 
    url=f'https://newsapi.org/v2/top-headlines?language=hi&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'hindi.html',context)        
                
def english(request): 
    url=f'https://newsapi.org/v2/top-headlines?language=en&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'english.html',context)        

def russian(request): 
    url=f'https://newsapi.org/v2/top-headlines?language=ru&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'russian.html',context)        
                                                


#catogary
def business(request): 
    url=f'https://newsapi.org/v2/top-headlines?category=business&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'business.html',context) 


def entertainment(request): 
    url=f'https://newsapi.org/v2/top-headlines?category=entertainment&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'entertainment.html',context) 

def general(request): 
    url=f'https://newsapi.org/v2/top-headlines?category=general&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'general.html',context) 

def health(request): 
    url=f'https://newsapi.org/v2/top-headlines?category=health&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'health.html',context) 

def science(request): 
    url=f'https://newsapi.org/v2/top-headlines?category=Science&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'science.html',context)   

def sports(request): 
    url=f'https://newsapi.org/v2/top-headlines?category=Sports&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'sports.html',context) 

def technology(request): 
    url=f'https://newsapi.org/v2/top-headlines?category=technology&apiKey={API_KEY}'
    r =requests.get(url)
    data=r.json()
    articles=data['articles']  
    context={
        'articles': articles
    }
    return render(request,'technology.html',context) 

