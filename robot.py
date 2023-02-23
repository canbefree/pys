import matplotlib.pyplot as plt
import maps.geojson as geojson
 
#解析GeoJSON文件
with open('x.geojson') as f:
    data = geojson.load(f)

print(data['features'][0]['geometry']['coordinates'])

#绘制图形
plt.axes().set_aspect('equal', 'datalim')
plt.title('My GeoJSON Map')
coodrs = zip(data['features'][0]['geometry']['coordinates'][0][0])
plt.scatter(coodrs)


#显示图形
plt.show()
