import scrapy

class NoticiasSpider(scrapy.Spider):
    name = 'noticias_spider'
    start_urls = [
        'https://www.primicias.ec/noticias/sucesos/aluvion-desaparecidos-heridos-viviendas-afectadas-alausi/',
        'https://www.elcomercio.com/actualidad/ecuador/30-familias-afectadas-por-un-aluvion-en-el-canton-alausi.html',
        'https://www.primicias.ec/noticias/sociedad/alausi-aluvion-declaracion-emergencia-multitud/',
        'https://www.lahora.com.ec/pais/alausi-aluvion-alud-muertos-heridos/',
        'https://elmercurio.com.ec/2024/04/21/nuevo-aluvion-en-alausi-deja-heridos-y-viviendas-destruidas/',
        'https://www.elcomercio.com/actualidad/ecuador/deslave-alausi-viviendas-afectadas.html',
        'https://www.teleamazonas.com/aluvion-alausi-personas-afectadas-heridos/',
        'https://www.metroecuador.com.ec/noticias/2024/04/21/por-que-se-dio-el-aluvion-en-la-parroquia-multitud-en-alausi/',
        'https://laprensa.com.ec/aluvion-en-alausi-que-se-registro-este-21-de-abril/',
        'https://diariocorreo.com.ec/97407/portada/declaran-emergencia-en-alausi-por-aluvion-que-deja-200-afectados-y-6-viviendas-destruidas',
        'https://www.vistazo.com/actualidad/nacional/nuevo-aluvion-en-alausi-hay-al-menos-30-familias-afectadas-DB7201511',
        'https://www.eltelegrafo.com.ec/noticias/seguridad/44/55-familias-reciben-atencion-despues-del-aluvion-en-alausi',
        'https://www.eltelegrafo.com.ec/noticias/nacionales/44/aluvion-en-alausi-la-secretaria-de-riesgos-atiende-la-emergencia-en-el-sector',
    ]

    def parse(self, response):
        if "primicias.ec" in response.url:
            titulo = response.xpath('//h1/text()').get(default='').strip()
            fecha = response.xpath('//time/@datetime').get(default='').strip()
            descripcion = ' '.join(response.xpath('//div[contains(@class, "contenido")]/p/text()').getall()).strip()
        elif "elcomercio.com" in response.url:
            titulo = response.xpath('//h1/text()').get(default='').strip()
            fecha = response.xpath('//meta[@property="article:published_time"]/@content').get(default='').strip()
            descripcion = ' '.join(response.xpath('//div[@class="contenido"]//p/text()').getall()).strip()
        elif "lahora.com.ec" in response.url:
            titulo = response.xpath('//h1/text()').get(default='').strip()
            fecha = response.xpath('//time/@datetime').get(default='').strip()
            descripcion = ' '.join(response.xpath('//div[contains(@class, "content-body")]//p/text()').getall()).strip()
        else:
            titulo = response.xpath('//h1/text()').get(default='').strip()
            fecha = response.xpath('//time/@datetime').get(default='').strip()
            descripcion = ' '.join(response.xpath('//article//p/text()').getall()).strip()

        # Unir imágenes en una sola cadena separada por ";"
        imagenes = ';'.join(response.xpath('//img/@src').getall())

        # Unir fuentes en una sola cadena separada por ";"
        fuentes = ';'.join(response.xpath('//a[contains(@href, "http")]/@href').getall())

        # Extraer afectados y fallecidos con mejor XPath
        afectados = response.xpath('string(//p[contains(text(), "afectadas")])').get(default='').strip()
        fallecidos = response.xpath('string(//p[contains(text(), "fallecidos")])').get(default='').strip()

        yield {
            'id_evento': response.url,
            'nombre': titulo,
            'fecha': fecha,
            'hora': '',
            'tipo_evento': 'Aluvión',
            'descripcion': descripcion,
            'provincia': 'Chimborazo',
            'canton': 'Alausí',
            'parroquia': '',
            'latitud': '',
            'longitud': '',
            'afectados': afectados,
            'fallecidos': fallecidos,
            'infraestructura': '',
            'area_afectada': '',
            'volumen_afectado': '',
            'multimedia': imagenes,
            'fuentes': fuentes,
            'acciones_tomadas': '',
            'estado_actual': '',
        }