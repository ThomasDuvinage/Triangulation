from PIL import Image
# ouverture d’une image au format pgm binaire :
imageSource=Image.open("manger.png")
# remarque : imageSource est un nom de variable , vous pouvez mettre un autre nom à la place . # sa largeur et sa hauteur en pixels :
largeur , hauteur= imageSource.size
# ouverture d ’une nv image
# pour l ’option "L", voir http://www.pythonware.com/library/pil/handbook/concepts.htm
# et pour Image.new() , voir http://www.pythonware.com/library/pil/handbook/image.htm 
imageBut=Image.new("L" ,(largeur ,hauteur))
# remarque : imageBut est un nom de variable , vous pouvez mettre un autre nom à la place .
# pour chaque ligne :
for y in range ( hauteur ) : #pour chaque colonne : 
    for x in range(largeur):
        # code du pixel (niveau de gris)
        p = imageSource.getpixel((x,y))
        # inversion du niveau de gris :
        q = 255 - p
        imageBut.putpixel((x,y) ,q)

# création du pixel correspondant dans la nv image : imageBut.putpixel((x,y) ,q)
# sauvegarde de l ’image créée :
imageBut.save("InversionAvecPil.pgm")
# on montre l ’ image :
imageBut.show()