class Configuraciones():
    #esta clase almacena las configuraciones del juego
    def __init__(self):
        #inicializa las configuraciones del juego
       

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #configuraciones de la nave
        self.factor_velocidad_nave = 1.5
        self.cantidad_naves = 3

        #configuraciones de balas
        self.bala_factor_velocidad = 3
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = 60, 60, 60
        self.balas_allowed = 3

        #condiguraciones de alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direccion, si es 1 representa a la derecha; si es -1 representa a la izquierda
        self.fleet_direction = 1