import requests

def query_conceptnet(term):
    url = f"http://api.conceptnet.io/c/en/{term}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def find_strongest_relationship(data):
    """
    ConceptNet'ten gelen JSON verisinde, en yüksek ağırlıklı ilişkiyi bulur.

    Args:
        data (dict): ConceptNet'ten gelen JSON yanıtı

    Returns:
        dict: En yüksek ağırlıklı ilişkinin bilgilerini döndürür (start, end, relation, weight, surface_text)
    """
    strongest_relationship = None
    max_weight = -1  # En yüksek ağırlık için başlangıç değeri

    if "edges" in data:
        for edge in data['edges']:
            weight = edge.get('weight', 0)  # Ağırlık değerini al

            if weight > max_weight:
                max_weight = weight
                # En yüksek ağırlıklı ilişkiyi sakla
                strongest_relationship = {
                    'start': edge['start']['label'],
                    'end': edge['end']['label'],
                    'relation': edge['rel']['label'],
                    'weight': weight,
                    'surface_text': edge.get('surfaceText', None)
                }
    return strongest_relationship
