
class Objects():

    qtd_texturas = 0

    __idTextureAvailable=0
    __vertices_list = []    
    __textures_coord_list = []

    def __init__(self,model_file,texture_file):

        self.model_file = model_file
        self.texture_file = texture_file
        
        qtd_texturas+=1