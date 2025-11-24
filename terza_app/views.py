from django.shortcuts import render


# Create your views here.
def diff(request):
    context={
        'n1' :15,
        'n2' :10,
        'diff': 15-10,
    }
    return render (request, "pari.html", context)
def pari(request):
    context={
        'n1' :15,
        'n2' :10,
         'n3' :16,
        'n4' :17,
         'n5' :18,
        'n6' :19,
         'n7' :1,
        'n8' :2,
         'n9' :3,
        'n10' :4,
         'n11' :5,
        'n12' :6,
         'n13' :7,
        'n14' :8,
         'n15' :9,
        
         
    }
    return render (request, "pari.html", context)
 