
# ----------- /// -----------
# Importações!

# Importa as funções auxiliares
from aux import *

# ----------- /// -----------

class Object:

    qtd_texturas = 0

    __idTextureAvailable=0
    __vIniAvailable=0
    vertices_list = []
    textures_coord_list = []

    def __init__(self,model_file,texture_file):

        self.model_file = model_file
        self.texture_file = texture_file
        self.ID = self.setId()

        self.vIni = -1
        self.vCount = -1
        
        self.qtd_texturas+=1

    def load(self):

        self.vIni = self.__vIniAvailable

        modelo = load_model_from_file(self.model_file)

        for face in modelo['faces']:
            for vertice_id in face[0]:
                self.vertices_list.append( modelo['vertices'][vertice_id-1] )
            for texture_id in face[1]:
                self.textures_coord_list.append( modelo['texture'][texture_id-1] )

        self.__vIniAvailable = len(self.vertices_list) + 1
        self.vCount = len(self.vertices_list) - self.vIni

        load_texture_from_file(self.ID,self.texture_file)

    def setId(self):

        self.__idTextureAvailable += 1 # incrementa o Id

        return (self.__idTextureAvailable - 1)
    
    def desenha(self):

        # faz o bind da textura
        glBindTexture(GL_TEXTURE_2D, self.ID)
    
        # desenha o modelo
        glDrawArrays(GL_TRIANGLES, self.vIni, self.vCount)

# ----------- /// -----------