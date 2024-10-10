from recruitment import query_conceptnet, find_strongest_relationship
import networkx as nx
import matplotlib.pyplot as plt
import json

# ilk olarak JSON çıktısını dosyaya kaydetme işlemi yapılıyor
def save_json_to_file(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# "computer" nesnesi için ilişkileri çekiliyor.
data = query_conceptnet('computer')
iliski = find_strongest_relationship(data)

# sonra "computer" nesnesi için JSON çıktısını dosyaya kaydediliyor.
save_json_to_file('computer_relationship.json', data)

# "chair" nesnesi için ilişkileri çekiliyor.
data = query_conceptnet('chair')
iliski = find_strongest_relationship(data)

# sonrasında "chair" nesnesi için JSON çıktısını dosyaya kaydediliyor.
save_json_to_file('chair_relationship.json', data)

# "desk" nesnesi için ilişkileri çekiliyor
data = query_conceptnet('desk')
iliski = find_strongest_relationship(data)

# sonrasında "desk" nesnesi için JSON çıktısını dosyaya kaydediliyor
save_json_to_file('desk_relationship.json', data)

# İlişki türlerini sınıflandırmak için tanımlamalar yapılıyor.
konumsal_iliskiler = ['AtLocation', 'On', 'In', 'Near']
islevsel_iliskiler = ['UsedFor', 'HasPrerequisite', 'CapableOf', 'PartOf']

def iliski_turu_belirle(iliski):
    """
    Verilen ilişkiyi konumsal veya işlevsel olarak sınıflandırma işlemi yapılıyor.
    """
    relation_type = iliski['relation']
    if relation_type in konumsal_iliskiler:
        return 'Konumsal'
    elif relation_type in islevsel_iliskiler:
        return 'İşlevsel'
    else:
        return 'Diğer'

nesneler = ['computer', 'chair', 'desk' ]

# Her bir nesne için ilişkileri bulup ve sınıflandırılıyor.
for nesne in nesneler:
    data = query_conceptnet(nesne)
    iliski = find_strongest_relationship(data)

    if iliski:
        iliski_turu = iliski_turu_belirle(iliski)
        print(f"Nesne: {nesne}")
        print(f"İlişki: {iliski['relation']}")
        print(f"Surface Text: {iliski['surface_text']}")
        print(f"İlişki Türü: {iliski_turu}")
        print('-' * 30)
    else:
        print(f"Nesne: {nesne} için ilişki bulunamadı.")
        print('-' * 30)

# Grafik için networkx grafiği başlatolıyor ve ilişki haritası oluşturuluyor.
G = nx.Graph()

G.add_edge('Computer', 'Keyboard', relation='PartOf')
G.add_edge('Chair', 'Office', relation='AtLocation')
G.add_edge('Desk', 'Stapler', relation='AtLocation')

pos1 = {'Computer': [-2, 2], 'Keyboard': [2, 2]}
pos2 = {'Chair': [-2, 0], 'Office': [2, 0]}
pos3 = {'Desk': [-2, -2], 'Stapler': [2, -2]}

pos = {**pos1, **pos2, **pos3}

plt.figure(figsize=(10, 10))

nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue')
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color='black')

edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.text(0, 1.4, "İşlevsel İlişki", horizontalalignment='center', fontsize=12)
plt.text(0, -0.6, "Konumsal İlişki", horizontalalignment='center', fontsize=12)
plt.text(0, -2.6, "Konumsal İlişki", horizontalalignment='center', fontsize=12)

plt.title("İlişkisel Harita: Computer-Keyboard, Chair-Office, Desk-Stapler")
plt.axis('off')
plt.show()
