from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Search
from vendedores.models import Publicacion

def search_products(request):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    # Productos desde modelo Search (productos del sistema)
    search_products = Search.objects.all()
    if query:
        search_products = search_products.filter(name__icontains=query)
    if category:
        search_products = search_products.filter(category__icontains=category)

    # Publicaciones desde modelo Publicacion (usuarios/vendedores)
    post_products = Publicacion.objects.all()
    if query:
        post_products = post_products.filter(titulo__icontains=query)
    if category:
        post_products = post_products.filter(categoria__icontains=category)

    context = {
        'search_products': search_products,
        'post_products': post_products,
        'query': query,
        'category': category,
        'no_results': not search_products.exists() and not post_products.exists()
    }
    return render(request, 'search_results.html', context)

@csrf_exempt
def create_product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_name = data.get("name")
        if product_name and not Search.objects.filter(name=product_name).exists():
            new_product = Search.objects.create(
                name=product_name,
                category="Desconocida",
                price=0.0,
                images=[]
            )
            new_product.save()
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "error": "Producto ya existe"})
    return JsonResponse({"success": False, "error": "Método no permitido"})
