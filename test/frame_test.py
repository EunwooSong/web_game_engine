
class entity:
    def __init__(self):
        self.__name = "Default"
        self.__position = (0, 0, 0)
        self.__update = list()
        self.__base_color = 0
        self.__render = list()
    def __init__(self, *args, **kwargs):
        self.__name = "Default" if 'name' not in kwargs.keys() else kwargs['name']
        self.__position = (0, 0, 0) if 'position' not in kwargs.keys() else kwargs['position']
        self.__base_color = 0x00000 if 'color' not in kwargs.keys() else kwargs['color']
        self.__update = list()
        self.__base_color = 0
        self.__render = list()
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, pos: tuple):
        self.__position = pos
    @property
    def color(self):
        return self.__base_color
    @color.setter
    def color(self, color: int):
        self.__base_color = color
    @property
    def update(self):
        return self.__update
    @property
    def redner(self):
        return self.__render
    
    def b_update(self, dt: float):
        for u in self.__update:
            u(me = self, dt=dt)
    def b_render(self):
        for r in self.__render:
            r()
    
    def add_update(self, func):
        self.__update.append(func)
    
    def add_render(self, func):
        self.__render.append(func)

class system:
    def __init__(self):
        self.__project_name = ""
        self.__entitys = list()
        self.scene = None
        self.main_camera = None
        #self.main_camera.position.z = 2
        self.renderer = None
        #self.renderer.setSize(640, 480)
        self.isRun = True
        self.delta_time = 0.1
        #document.body.appendChild( self.renderer.domElement )

    def reset_system(self):
        pass
    def pause_system(self):
        self.isRun = False
    def resume_system(self):
        self.isRun = True
    def system_loop(self):
        if not self.isRun:
            return
        for e in self.__entitys:
            e.b_update(self.delta_time)
            e.b_render()
        #self.renderer.render(self.scene, self.main_camera)

    def add_entity(self, e):
        print('Add entity in system')
        self.__entitys.append(e)
demo_system = system()

class rectagle(entity):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

        #setting object geometry and material
        #self.geometry = THREE.BoxGeometry.new()
        perms = {"color": "#ff0000", "wireframe": False}
        #self.perms = Object.fromEntries(to_js(perms))
        #self.material = THREE.MeshBasicMaterial.new(self.perms)
        #self.obj = THREE.Mesh.new(self.geometry, self.material)
        demo_system.add_entity(self)
        #demo_system.scene.add(self.obj)

    def b_update(self, dt: float):
        return super().b_update(dt)
    
    def b_render(self):
        pass
        #self.obj.material.color.setHex(self.color)
        #self.obj.position.x = self.position[0]
        #self.obj.position.y = self.position[1]
        #self.obj.position.z = self.position[2]
    def add_update(self, func):
        return super().add_update(func)
    def add_render(self, func):
        return super().add_render(func)
    
rect = rectagle()
rainbow = 0.0

def test_update(me, dt):
    global rainbow
    rainbow = rainbow + dt
    print("tmp:", rainbow)
rect.add_update(test_update)

while True:
    demo_system.system_loop()
    