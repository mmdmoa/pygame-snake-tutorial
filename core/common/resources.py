from core.common.names import *
from core.event_holder import EventHolder

screen: Optional[Surface] = None
event_holder: Optional[EventHolder] = None
game = None
fps_font: Optional[pg.font.Font] = None