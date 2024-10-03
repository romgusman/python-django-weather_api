from django.shortcuts import render
from .api import get_weather_data, kelvin_to_celsius, kelvin_to_fahrenheit, languages

def index(request):
    weather = None
    # Obtém o idioma da sessão ou usa o padrão 'en'
    language = request.session.get('language', 'en')

    if request.method == 'POST':
        if 'city' in request.POST:  # Se o formulário da cidade for enviado
            city = request.POST.get('city')
            weather = get_weather_data(city, language)  # Busca os dados do clima
        elif 'language' in request.POST:  # Se o formulário de idioma for enviado
            language = request.POST.get('language')
            request.session['language'] = language  # Armazena o idioma na sessão

    # Se a consulta ao clima for bem-sucedida
    if weather:
        # Conversão das temperaturas
        temp_kelvin = weather['main']['temp']
        temp_celsius = kelvin_to_celsius(temp_kelvin)
        temp_fahrenheit = kelvin_to_fahrenheit(temp_kelvin)

        # Adiciona as temperaturas convertidas no dicionário
        weather['main']['temp_celsius'] = round(temp_celsius, 2)  # Arredonda para 2 casas decimais
        weather['main']['temp_fahrenheit'] = round(temp_fahrenheit, 2)

    # Renderiza o template com os dados
    return render(request, 'weather_api/index.html', {'weather': weather, 'languages': languages, 'selected_language': language})
