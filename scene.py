
class Scene:
  

    def __init__(self, director):
        self.director = director

    def on_update(self):        
        raise NotImplemented("Tiene que implementar el metodo on_update.")

    def on_event(self, event):        
        raise NotImplemented("Tiene que implementar el metodo on_event.")

    def on_draw(self, screen):        
        raise NotImplemented("Tiene que implementar el metodo on_draw.")