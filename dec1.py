with open 
with open(path, 'r', encoding='utf-8') as json_file:
        wrap: Wrapper = handler.read_json(json_file)
        publication: Publication = wrap.content
        text = ''
        for article in publication.articles:
            text = ' '.join(para.value for para in article.paragraphs if para.value is not None)
