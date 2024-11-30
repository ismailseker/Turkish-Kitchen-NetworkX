import json
import networkx as nx
import matplotlib.pyplot as plt

# JSON dosyasını yükleme
file_path = "/Users/sekerismail/Desktop/Turkish-Kitchen-NetworkX/yemeklerr.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)


G = nx.Graph()

# Düğümleri ekleme
for yemek in data["nodes"]:
    G.add_node(
        yemek["id"],  # Düğüm kimliği
        name=yemek["name"],  # Yemek adı
        region=yemek["region"],  # Bölge
        category=yemek["category"],  # Kategori
        ingredients=yemek["ingredients"],  # Malzemeler
        description=yemek["description"]  # Açıklama
    )

# Kenarları oluşturma (ortak malzemelere göre bağlama)
for yemek1 in data["nodes"]:
    for yemek2 in data["nodes"]:
        if yemek1["id"] != yemek2["id"]:  # Aynı düğümü bağlamayın
            ortak_malzemeler = set(yemek1["ingredients"]) & set(yemek2["ingredients"])
            if ortak_malzemeler:  # Ortak malzeme varsa kenar oluştur
                G.add_edge(yemek1["id"], yemek2["id"], ortak_malzemeler=list(ortak_malzemeler))

# Graf bilgilerini yazdırma
print(f"Graf Düğüm Sayısı: {G.number_of_nodes()}")
print(f"Graf Kenar Sayısı: {G.number_of_edges()}")

# Düğümleri ve kenarları listeleme
print("Düğümler ve Özellikler:")
for node, data in G.nodes(data=True):
    print(f"{node}: {data}")

print("Kenarlar ve Özellikler:")
for edge in G.edges(data=True):
    print(edge)

# Grafiği görselleştirme
plt.figure(figsize=(12, 12))
nx.draw(
    G,
    with_labels=True,
    node_size=3000,
    font_size=10,
    node_color="lightgreen",
    font_weight="bold",
    edge_color="gray",
    alpha=0.8
)
plt.title("Türk Mutfağı Yemek Grafiği")
plt.show()